from html.parser import HTMLParser
from pathlib import Path
import shutil
import subprocess
import tempfile

GAME = Path("index.html")
source = GAME.read_text(encoding="utf-8")

class GameHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = []
        self.in_title = False
        self.script_depth = 0
        self.inline_scripts = []
        self.current_script = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "title":
            self.in_title = True
        elif tag == "script":
            self.script_depth += 1
            self.current_script = []
            self.current_script_external = bool(attrs.get("src"))

    def handle_data(self, data):
        if self.in_title:
            self.title.append(data)
        if self.script_depth and not getattr(self, "current_script_external", False):
            self.current_script.append(data)

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False
        elif tag == "script" and self.script_depth:
            if not getattr(self, "current_script_external", False):
                self.inline_scripts.append("".join(self.current_script))
            self.script_depth -= 1
            self.current_script = []

parser = GameHTMLParser()
parser.feed(source)
parser.close()

assert source.lstrip().lower().startswith("<!doctype html>"), "DOCTYPE HTML ausente"
assert "".join(parser.title).strip() == "Industrial Frontier", "Título inesperado ou ausente"
assert parser.inline_scripts, "Nenhum JavaScript incorporado encontrado"
assert "setInterval" in source, "Loop principal do jogo não encontrado"
assert "SP=.5,tab=0,lastLog=null;" in source, "Velocidade padrão deve ser 1 hora de jogo a cada 2 minutos reais"
assert '[[0,"⏸"],[.5,"1×"],[1,"2×"],[2,"4×"]]' in source, "Controles de velocidade esperados não encontrados"
assert 'v+" hora(s) de jogo por minuto real"' in source, "Descrição da velocidade não corresponde ao relógio do jogo"
assert "function init" in source or "init=()=>{" in source or "function init(" in source, "Inicialização do jogo não encontrada"

node = shutil.which("node")
if not node:
    raise SystemExit("Node.js é necessário para validar a sintaxe do JavaScript.")

with tempfile.NamedTemporaryFile("w", suffix=".js", encoding="utf-8", delete=False) as js:
    js.write("\n".join(parser.inline_scripts))
    js_path = Path(js.name)

try:
    result = subprocess.run([node, "--check", str(js_path)], text=True, capture_output=True)
    if result.returncode:
        print(result.stdout, end="")
        print(result.stderr, end="")
        raise SystemExit(result.returncode)
finally:
    js_path.unlink(missing_ok=True)

print("OK: estrutura HTML, elementos essenciais e sintaxe JavaScript validados.")
