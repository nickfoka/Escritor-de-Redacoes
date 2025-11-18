import os
import time
import keyboard
from google import genai
from google.genai import types
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv(dotenv_path="api.env")
# Define a função do ChatGPT.
def chatgpt():
    print(os.environ.get("OPENAI_API_KEY"))
    inn = input("Insira o tema da redação: ")
    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),
    )
    response = client.responses.create(
    model="gpt-5-nano",
    instructions="Você tem o vocabulário de um adolescente do ensino médio e irá escrever uma redação sobre o tema, gênero, e numero de palávras fornecido",
    input=inn
    )
    # Escreve automaticamente na tela a redação.
    os.system("cls")
    print(response.output_text)
    res = input("\nDeseja escrever automaticamente a redação? sim / não\n")
    texto = response.output_text.encode("utf-8").decode("utf-8")
    if res == "sim":
        time.sleep(2)
        for parte in texto.split(" "):
            keyboard.write(parte + " ", delay=0.01)
            time.sleep(0.02)
    else:
        input("\nPressione enter para sair!")

# Define a função do Gemini.
def gemini():
    print(os.environ.get("GEMINI_API_KEY"))
    inn = input("Insira o tema da redação: ")
    client = genai.Client()
    response = client.models.generate_content(
            model='gemini-2.5-flash', contents=inn,
            config=types.GenerateContentConfig(system_instruction="Você tem o vocabulário de um adolescente do ensino médio e irá escrever uma redação sobre o tema, gênero, e numero de palávras fornecido")
    )
    client.close()
    os.system("cls")
    print(response.text)
    res = input("\nDeseja escrever automaticamente a redação? sim / não\n")
    texto = response.text
    if res == "sim":
        time.sleep(2)
        for parte in texto.split(" "):
            keyboard.write(parte + " ", delay=0.01)
            time.sleep(0.02)
    else:
        input("\nPressione enter para sair!")

# Pergunta qual a IA desejada.
a = int(input("Deseja utilizar a API do Gemini ou do Chat-gpt?   1-Chatgpt / 2-Gemini\n"))
if (a == 1):
    chatgpt()
else:
    gemini()
