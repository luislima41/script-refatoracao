🐍 Script de Refatoração Automatizada

Este repositório contém o script Python desenvolvido para automatizar o processo de refatoração de sistemas legados estruturados em MVC para o padrão Clean Architecture, com auxílio de técnicas de Inteligência Artificial.

Descrição Geral

O script realiza análise estrutural e semântica de um projeto em MVC, identifica dependências entre camadas e reorganiza o código conforme os princípios da Clean Architecture. Utiliza heurísticas e prompts otimizados para geração de código assistida por LLMs (ex.: GPT).

Estrutura do Projeto

auto-refactor-script/
├── main.py

Requisitos

Python 3.10+

Biblioteca openai (se utilizar a API oficial) ou outra biblioteca HTTP adequada

Bibliotecas padrão: os, json, re, etc.

Instalação (exemplo):

pip install -r requirements.txt

Execução (exemplo)

Clone o repositório, ajuste configurações e execute:

git clone https://github.com/SEU_USUARIO/auto-refactor-script.git

cd auto-refactor-

editar configurações (API key, paths) em config.json ou env

python main.py --input ../mvc-legacy-system --output ../clean-architecture-system


Parâmetros comuns:

--input : caminho para o projeto MVC de entrada

--output: caminho para o diretório onde os artefatos refatorados serão salvos

Fluxo de Funcionamento

Leitura e segmentação do código-fonte do sistema MVC.

Geração de prompts e envio à API de LLM (ou mecanismo local).

Recebimento das respostas e construção dos novos artefatos (entidades, casos de uso, adaptadores).

Escrita dos arquivos no diretório de saída e geração de logs.

Observações de Segurança

NÃO inclua chaves de API no repositório. Utilize variáveis de ambiente ou arquivos de configuração ignorados pelo Git (.gitignore).

Registre e audite as interações com a API (logs) sem expor dados sensíveis.




