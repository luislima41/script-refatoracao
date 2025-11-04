import os
import openai
import shutil
import logging

# ------------------ CONFIGURAÇÕES GERAIS ------------------ #
openai.api_key = "SUA_CHAVE_API_GPT_AQUI"

BASE_PATH = "mvc_source"  
OUTPUT_PATH = "clean_architecture_output" 
LOG_PATH = "logs/refatoracao.log"

# Criação das pastas de saída e logs, se não existirem
os.makedirs(OUTPUT_PATH, exist_ok=True)
os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)

# ------------------ CONFIGURAÇÃO DE LOG ------------------ #
logging.basicConfig(
    filename=LOG_PATH,
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s]: %(message)s",
)

# ------------------ MÓDULO DE LEITURA ------------------ #
def ler_arquivo(caminho):
    """Lê o conteúdo de um arquivo de texto."""
    try:
        with open(caminho, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        logging.error(f"Erro ao ler arquivo {caminho}: {e}")
        return None

# ------------------ MÓDULO DE SALVAMENTO ------------------ #
def salvar_arquivo(caminho, conteudo):
    """Salva o conteúdo em um arquivo, criando diretórios se necessário."""
    try:
        os.makedirs(os.path.dirname(caminho), exist_ok=True)
        with open(caminho, 'w', encoding='utf-8') as f:
            f.write(conteudo)
        logging.info(f"Arquivo salvo: {caminho}")
    except Exception as e:
        logging.error(f"Erro ao salvar arquivo {caminho}: {e}")

# ------------------ MÓDULO DE COMUNICAÇÃO COM GPT ------------------ #
def refatorar_codigo(codigo, nome_arquivo):
    prompt = f"""
Você é um engenheiro de software especializado em Clean Architecture.
Analise o código a seguir, originalmente estruturado em MVC, e refatore-o
seguindo os princípios da Clean Architecture, mantendo a lógica de negócio
e separando as responsabilidades de forma adequada.

Arquivo: {nome_arquivo}
Código original:
{codigo}

Retorne o código refatorado e uma breve explicação das modificações realizadas.
"""
    try:
        resposta = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1800,
            temperature=0.3
        )
        conteudo = resposta.choices[0].message["content"]
        logging.info(f"Refatoração concluída para {nome_arquivo}")
        return conteudo

    except Exception as e:
        logging.error(f"Erro na comunicação com a API para o arquivo {nome_arquivo}: {e}")
        return None

# ------------------ MÓDULO PRINCIPAL DE PROCESSAMENTO ------------------ #
def processar_diretorio(base_dir):
    logging.info("Iniciando processo de refatoração automatizada...")
    for root, _, files in os.walk(base_dir):
        for file in files:
            if file.endswith(".py"):
                caminho_entrada = os.path.join(root, file)
                codigo = ler_arquivo(caminho_entrada)

                if codigo:
                    print(f"Refatorando {file} ...")
                    novo_codigo = refatorar_codigo(codigo, file)

                    if novo_codigo:
                        caminho_saida = caminho_entrada.replace(BASE_PATH, OUTPUT_PATH)
                        salvar_arquivo(caminho_saida, novo_codigo)
                    else:
                        logging.warning(f"Falha ao refatorar {file}.")
    logging.info("Processo de refatoração finalizado com sucesso.")

# ------------------ EXECUÇÃO ------------------ #
if __name__ == "__main__":
    try:
        processar_diretorio(BASE_PATH)
        print("Refatoração automatizada concluída com sucesso!")
    except Exception as e:
        logging.critical(f"Erro fatal na execução do script: {e}")
        print("Ocorreu um erro durante a execução. Consulte o arquivo de log.")
