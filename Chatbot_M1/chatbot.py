from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# necessário para corrigir o bug do spacy
from spacy.cli import download

download("en_core_web_sm")

class ENGSM:
    ISO_639_1 = 'en_core_web_sm'

chatbot = ChatBot('M1 Chatbot', tagger_language=ENGSM)

conversa = ['Oi', 'Olá', 'Tudo bem?', 'Tudo ótimo', 'Você gostaria de ver o catálogo?', 'Sim, por favor']

trainer = ListTrainer(chatbot)
trainer.train(conversa)

# loop criado para interagir com o bot

while True:
    pergunta = input("Usuário: ")
    if pergunta == "parar":
        break
    resposta = chatbot.get_response(pergunta)
    print(resposta)