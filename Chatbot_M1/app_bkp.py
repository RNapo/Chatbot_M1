#importando bibliotecas necessárias para o projeto

from flask import Flask, render_template, request, jsonify
import os
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from requests import get
from bs4 import BeautifulSoup

app = Flask(__name__)

bot= ChatBot('ChatBot')

trainer = ListTrainer(bot)

# Nesse bloco contém um FOR para percorrer as listas de treinamento localizado no diretorio /data/ 

for file in os.listdir('C:/Users/User/Documents/Chat/Chatbot_M1/data/'):

    chats = open('C:/Users/User/Documents/Chat/Chatbot_M1/data/' + file, 'r').readlines()

    trainer.train(chats)

# Rota home (index) para abrir a página html
@app.route("/")
def home():
    return render_template('index.html')

# Rota para realizar pesquisa no wikipedia, realiza pesquisa conforme a palavra digitada no bot.
@app.route("/pesquisa", methods=['POST'])
def pesquisa():

    message = str(request.form['messageText'])

    bot_response = bot.get_response(message)

    while True:

        if bot_response.confidence > 0.1:

            bot_response = str(bot_response)      
            print(bot_response)
            return jsonify({'status':'OK','answer':bot_response})
 
        elif message == ("até logo"):

            bot_response='Esperamos vê-lo em breve!'

            print(bot_response)
            return jsonify({'status':'OK','answer':bot_response})

            break

        else:
        
            try:
                url  = "https://pt.wikipedia.org/wiki/"+ message
                page = get(url).text
                soup = BeautifulSoup(page,"html.parser")
                p    = soup.find_all("p")
                return jsonify({'status':'OK','answer':p[1].text})

            except IndexError as error:

                bot_response = 'Desculpe, ainda não posso responder isso!'
            
                print(bot_response)
                return jsonify({'status':'OK','answer':bot_response})

if __name__ == "__main__":
    app.run()