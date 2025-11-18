import os
import time
import keyboard
from google import genai
from google.genai import types
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv(dotenv_path="api.env")
global a
a = 0
# Define a função que escreve na tela.
def ered(texto):
    if (a == 1):
        os.system("cls")
        print(texto)
        res = input("\nDeseja escrever automaticamente a redação? sim / não\n")
        if res == "sim":
            time.sleep(2)
            for parte in texto.split(" "):
                keyboard.write(parte + " ", delay=0.01)
                time.sleep(0.02)
            else:
                input("\nPressione enter para sair!")
    else:
        os.system("cls")
        print(texto)
        res = input("\nDeseja escrever automaticamente a redação? sim / não\n")
        if res == "sim":
            time.sleep(2)
            for parte in texto.split(" "):
                keyboard.write(parte + " ", delay=0.01)
                time.sleep(0.02)
            else:
                input("\nPressione enter para sair!")


# Define a função do ChatGPT.
def chatgpt():
    print(os.environ.get("OPENAI_API_KEY"))
    inn = input("Insira o tema da redação: ")
    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),
    )
    response = client.responses.create(
    model="gpt-5-nano",
    instructions="Você tem o vocabulário de um adolescente do ensino médio que tenta ser formal para um redação, e irá escrever uma redação sobre o tema, gênero, e numero de palávras fornecido" "Não faça perguntas, não peça mais detalhes e não inicie diálogos. "
        "Somente escreva a redação completa.",
    input=inn
    )
    global a
    a = 1
    texto = response.output_text
    ered(texto)

# Define a função do Gemini.
def gemini():
    print(os.environ.get("GEMINI_API_KEY"))
    inn = input("Insira o tema da redação: ")
    client = genai.Client()
    response = client.models.generate_content(
            model='gemini-2.5-flash', contents=inn,
            config=types.GenerateContentConfig(system_instruction="Você tem o vocabulário de um adolescente do ensino médio que tenta ser formal para um redação, e irá escrever uma redação sobre o tema, gênero, e numero de palávras fornecido" "Não faça perguntas, não peça mais detalhes e não inicie diálogos. "
        "Somente escreva a redação completa.")
    )
    global a
    a = 2
    client.close()
    texto = response.text
    ered(texto)

# Define alguns erros.
def erros():
    if (not os.path.exists('api.env')):
        os.system("cls")
        print("Não foi possivel iniciar o programa: Arquivo api.env inexistente.")
        input("Pressione qualquer tecla para sair...")
        raise Exception("Inexistencia de arquivo: api.env")
    
    if (os.environ.get("OPENAI_API_KEY") == "" and resposta == 1):
        os.system("cls")
        print("Não foi possivel inciar o programa: Sem chave de API OpenAI.")
        input("Pressione qualquer tecla para sair...")
        raise Exception("Falta de chave API OpenAI")
    
    if (os.environ.get("GEMINI_API_KEY") == "" and resposta == 2):
        os.system("cls")
        print("Não foi possivel inciar o programa: Sem chave de API Gemini.")
        input("Pressione qualquer tecla para sair...")
        raise Exception("Falta de chave API Gemini")



# Pergunta qual a IA desejada.
resposta = int(input("Deseja utilizar a API do Gemini ou do Chat-gpt?   1-Chatgpt / 2-Gemini\n"))
if (resposta == 1):
    erros()
    chatgpt()
else:
    erros()
    gemini()