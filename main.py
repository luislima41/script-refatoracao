import os
import openai
import shutil

openai.api_key = "SUA_CHAVE_API_GPT_AQUI"
BASE_PATH = "mvc_source"
OUTPUT_PATH = "clean_architecture_output"
os.makedirs(OUTPUT_PATH, exist_ok=True)

def ler_arquivo(caminho):
    with open(caminho, 'r', encoding='utf-8') as f:
        return f.read()

def salvar_arquivo(caminho, conteudo):
    os.makedirs(os.path.dirname(caminho), exist_ok=True)
    with open(caminho, 'w', encoding='utf-8') as f:
        f.write(conteudo)

def refatorar_codigo(codigo, nome_arquivo):
    prompt = f'''
Você é um engenheiro de software especializado em Clean Architecture.
Analise o seguinte código MVC e reorganize-o conforme os princípios da Clean Architecture,
preservando a lógica de negócio e separando responsabilidades.

Código original ({nome_arquivo}):
{codigo}

Retorne o código transformado e explique brevemente as modificações realizadas.
'''
    resposta = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1800,
        temperature=0.3
    )
    return resposta.choices[0].message["content"]

def processar_diretorio(base_dir):
    for root, _, files in os.walk(base_dir):
        for file in files:
            if file.endswith(".py"):
                caminho_entrada = os.path.join(root, file)
                codigo = ler_arquivo(caminho_entrada)
                print(f"Refatorando {file} ...")
                novo_codigo = refatorar_codigo(codigo, file)
                caminho_saida = caminho_entrada.replace(BASE_PATH, OUTPUT_PATH)
                salvar_arquivo(caminho_saida, novo_codigo)

if __name__ == "__main__":
    processar_diretorio(BASE_PATH)
    print("Refatoração automatizada concluída com sucesso!")
