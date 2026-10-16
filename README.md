# Industrial Frontier — protótipo HTML

Esta é a versão jogável independente de **Industrial Frontier**, desenvolvida em HTML, CSS e JavaScript. Ela é a base de desenvolvimento deste repositório; não depende do protótipo Streamlit do outro repositório.

## Executar localmente

Abra `index.html` em um navegador moderno. Não é necessário instalar Python, Node.js ou um servidor para jogar.

## Validação automática

O workflow do GitHub Actions valida a estrutura básica do HTML e verifica a sintaxe do JavaScript incorporado. Para executar localmente, use Python 3 e Node.js:

```bash
python scripts/validate_html.py
```

Essas verificações não substituem os testes manuais das mecânicas do jogo.

## Hospedagem e acesso

O repositório atual é público. GitHub Pages para um repositório público também disponibiliza o jogo publicamente; um link difícil de adivinhar não é controle de acesso. A publicação em Pages deve ser habilitada somente depois de decidir se uma versão pública atende ao teste ou se será necessário um serviço com autenticação.
