# 🧠 Script Automatizador de Refatoração MVC → Clean Architecture

## 📘 Descrição Geral

Este script foi desenvolvido como parte de uma pesquisa aplicada em **Engenharia de Software**, cujo objetivo é **automatizar a refatoração de sistemas legados baseados no padrão MVC** (Model-View-Controller) para o **padrão Clean Architecture**, utilizando técnicas de **Inteligência Artificial** via **API do GPT**.

A ferramenta foi implementada em **Python** e constitui o **núcleo operacional da metodologia** apresentada no trabalho. Sua estrutura modular e orientada a tarefas permite que o processo de transformação ocorra de maneira controlada, rastreável e extensível, sendo facilmente adaptável a diferentes contextos de projeto.

---

## ⚙️ Estrutura do Script

O código é composto por **módulos independentes**, responsáveis por diferentes etapas do processo automatizado:

1. **Leitura e segmentação dos artefatos de código**  
   Percorre o diretório do sistema legado (`mvc_source`), identificando arquivos-fonte relevantes (extensão `.py`).

2. **Comunicação com a API do GPT**  
   Envia o conteúdo de cada arquivo para o modelo GPT, que realiza a refatoração segundo os **princípios da Clean Architecture**, mantendo a lógica de negócio e separando as responsabilidades.

3. **Geração e reintegração dos artefatos**  
   Os arquivos refatorados são gravados automaticamente em um diretório de saída (`clean_architecture_output`), preservando a estrutura de diretórios original.

4. **Registro e rastreabilidade (Logging)**  
   Todas as ações, exceções e respostas da API são registradas em `logs/refatoracao.log`, permitindo auditoria e depuração do processo.

5. **Controle de exceções e continuidade**  
   Mecanismos de tratamento de erros garantem que falhas pontuais em um arquivo não interrompam a execução geral do processo.

---

## 🧩 Funcionalidades Principais

- Identificação automática dos arquivos Python de um projeto MVC.
- Envio dos artefatos de código para refatoração via **API do GPT**.
- Armazenamento estruturado dos códigos refatorados em diretório separado.
- Geração de logs detalhados para auditoria.
- Estrutura modular, extensível e de fácil manutenção.

---

## 🧰 Tecnologias Utilizadas

- **Python 3.10+**
- **Biblioteca OpenAI** (`openai`)
- **Módulos padrão:** `os`, `shutil`, `logging`

---

## 📦 Estrutura de Diretórios

auto-refactor-script/
│
├── mvc_source/ # Código-fonte original (MVC)
│ └── ... # Arquivos .py a serem refatorados
│
├── clean_architecture_output/ # Código refatorado gerado pela IA
│ └── ... # Estrutura replicada e atualizada
│
├── logs/
│ └── refatoracao.log # Registro detalhado das operações
│
└── refatorador.py # Script principal

---

## 🚀 Como Executar

1. **Instale as dependências:**
   ```bash
   pip install openai
Configure sua chave da API OpenAI:
Edite a linha no início do script:

openai.api_key = "SUA_CHAVE_API_GPT_AQUI"
Coloque seu projeto MVC dentro da pasta mvc_source.

Execute o script:

python refatorador.py
Verifique os resultados:

Código refatorado estará em clean_architecture_output/.

Logs de execução estarão em logs/refatoracao.log.

🧪 Resultados Esperados
Estrutura reorganizada conforme os princípios da Clean Architecture.

Separação clara entre camadas de domínio, aplicação e infraestrutura.

Redução da acoplamento e aumento da testabilidade.

Histórico completo das interações entre o script e a API.

🧭 Aplicabilidade e Extensão
O design modular do script possibilita:

Ajustar granularidade de refatoração (por arquivo, módulo ou componente);

Integrar o processo a pipelines DevOps e CI/CD;

Expandir o suporte para múltiplas linguagens de programação;

Realizar experimentos adicionais com diferentes modelos de linguagem.

📄 Licença
Este projeto é distribuído sob a licença MIT.
Sinta-se livre para usar, modificar e aprimorar o código para fins acadêmicos ou de pesquisa.


