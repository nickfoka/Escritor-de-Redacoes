# Escritor de Redações

Um programa escrito em python capaz de escrever redações através de IA, e escrever a redação em um site Anti-Cópia, sendo possivel utilizar:
- Chat-gpt
- Gemini

## Como utilizar
Para utilizar o programa, insira sua(s) chave(s) API dentro do arquivo api.env.
Exemplo:

OPENAI_API_KEY=sk-.......aw

GEMINI_API_KEY=Ars......jsk

E execute!

Eu recomendo utilizar o Gemini, já que é quase 3 vezes mais rápido para fazer redações,
e também que as redações do Chat-gpt são muito artificiais, mas é claro, isso pode variar bastante.

Um comparativo de tempo para fazer uma redação do mesmo tema:
- Gemini: 14 Segundos
- Chat-gpt: 48 Segundos


### Alguns erros que podem ocorrer:

"Não foi possivel iniciar o programa: Arquivo api.env inexistente."
- Está faltando o arquivo "api.env" na pasta local do programa, necessário para informar a chave api para o funcionamento do script.

"Não foi possivel inciar o programa: Sem chave de API OpenAI."
- Isso quer dizer que foi escolhido usar o Chat-gpt, mas não foi inserido a chave de API da OpenAI(Chat-gpt) no arquivo api.env.

"Não foi possivel inciar o programa: Sem chave de API Gemini."
- Isso quer dizer que foi escolhido usar o Gemini, mas não foi inserido a chave de API no arquivo api.env.

Site para a criação das APIs:
OpenAI(Chat-gpt):
https://platform.openai.com/welcome?step=create

Gemini:
https://aistudio.google.com/api-keys
