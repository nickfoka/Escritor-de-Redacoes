import os
import time
import keyboard
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv(dotenv_path=r"\api.env")

inn = input("Insira o tema da redação: ")
client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),
)
response = client.responses.create(
    model="gpt-5-nano",
    instructions="Você tem o vocabulário de um adolescente do ensino médio e irá escrever uma redação sobre o tema, gênero, e numero de palávras fornecido",
    input=inn
)

with open("Redação.txt", "w", encoding="utf-8") as f:
    f.write(response.output_text)

    os.system("cls")
    print(response.output_text)
    res = input("\nDeseja escrever automaticamente a redação? sim / não\n")
    texto = response.output_text.encode("utf-8").decode("utf-8")
    if res == "sim":
        time.sleep(2)
        for parte in texto.split(" "):
            keyboard.write(parte + " ", delay=0.05)
            time.sleep(0.02)
    else:
        input("\nPressione enter para sair!")
