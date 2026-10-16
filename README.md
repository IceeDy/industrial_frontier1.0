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

## Teste online com GitHub Pages

O workflow `.github/workflows/deploy-pages.yml` publica o conteúdo estático da raiz do repositório quando há push em `main`, ou quando o workflow é acionado manualmente. Para que a publicação funcione, em **Settings → Pages**, selecione **GitHub Actions** como origem de build/deploy, caso ainda não esteja configurado.

A URL esperada do projeto é `https://iceedy.github.io/industrial_frontier1.0/`, depois que a primeira implantação terminar com sucesso.

**Atenção:** este repositório é público. O jogo e os arquivos publicados serão acessíveis publicamente; um link difícil de adivinhar não restringe o acesso. O deploy não deve ser confundido com teste de gameplay: após a publicação, valide manualmente as ações no navegador e reporte os erros antes de avançarmos nas mecânicas.
