from flask import Flask, render_template, request, jsonify, session
import os
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from requests import get
from bs4 import BeautifulSoup
import logging

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Uso de sessões em Flask

# Configuração do logging para gravar em um arquivo
log_file = 'app.log'
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

bot = ChatBot('ChatBot')
trainer = ListTrainer(bot)

# Treinamento do chatbot com os arquivos de dados
data_path = 'C:/Users/User/Documents/Chat/Chatbot_M1/data/'
for file in os.listdir(data_path):
    file_path = os.path.join(data_path, file)
    with open(file_path, 'r') as f:
        chats = f.readlines()
    trainer.train(chats)
    logger.info(f"Treinado com o arquivo: {file_path}")

# Rota home (index) para abrir a página HTML
@app.route("/")
def home():
    logger.info("Acesso à rota home")
    return render_template('index.html')

# Rota para realizar pesquisa no Wikipedia e responder ao usuário
@app.route("/pesquisa", methods=['POST'])
def pesquisa():
    message = str(request.form['messageText'])
    logger.info(f"Mensagem recebida: {message}")

    # Inicializa a sessão se não estiver definida
    if 'first_message_sent' not in session:
        session['first_message_sent'] = False

    if not session['first_message_sent']:
        session['first_message_sent'] = True
        logger.info("Primeira mensagem do usuário")
        return jsonify({
            'status': 'OK',
            'answer': "Olá! Como posso ajudar você hoje? Escolha uma opção abaixo:"
        })

    # Lógica para lidar com mensagens específicas
    if message in ['Ola', 'preciso de ajuda', 'Preciso de ajuda', 'Quero tirar uma duvida', 'quero tirar uma duvida']:
        logger.info("Resposta padrão para mensagens de ajuda")
        return jsonify({
            'status': 'OK',
            'answer': "Olá! Como posso ajudar você hoje? Escolha uma opção abaixo ou digite algo:"
        })

    elif message == 'Financiamento de carro':
        logger.info("Informações sobre financiamento de carro")
        return jsonify({
            'status': 'OK',
            'answer': "Para informações sobre financiamento de carro, entre em contato conosco pelo telefone (xx) xxxx-xxxx ou visite nosso site. https://m1motors.com.br/"
        })

    elif message == 'Falar com atendente':
        logger.info("Informações para falar com atendente")
        return jsonify({
            'status': 'OK',
            'answer': "Você pode falar com um atendente pelo telefone (xx) xxxx-xxxx. Estamos aqui para ajudar!"
        })

    elif message == 'Link do site':
        logger.info("Solicitação de link do site")
        return jsonify({
            'status': 'OK',
            'answer': "Aqui está o link para o nosso site: https://m1motors.com.br/"
        })

    elif message == 'Endereço':
        logger.info("Solicitação de endereço")
        return jsonify({
            'status': 'OK',
            'answer': "Nosso escritório está localizado na Avenida Sete de Setembro, 2451 - Rebouças, Curitiba - PR, Andar 7, temos lojas nos shopping Mueller, Jockey, São José, Boulevard e Crystal."
        })

    # Resposta do chatbot
    bot_response = bot.get_response(message)

    if bot_response.confidence > 0.1:
        bot_response_text = str(bot_response)
        logger.info(f"Resposta do bot: {bot_response_text}")
        return jsonify({'status': 'OK', 'answer': bot_response_text})

    elif message.lower() == "até logo":
        bot_response_text = 'Esperamos vê-lo em breve!'
        logger.info(f"Resposta do bot: {bot_response_text}")
        return jsonify({'status': 'OK', 'answer': bot_response_text})

    else:
        try:
            url = "https://pt.wikipedia.org/wiki/" + message
            page = get(url).text
            soup = BeautifulSoup(page, "html.parser")
            p = soup.find_all("p")
            response_text = p[1].text
            logger.info(f"Resposta da Wikipedia: {response_text}")
            return jsonify({'status': 'OK', 'answer': response_text})
        except IndexError:
            bot_response_text = 'Desculpe, ainda não posso responder isso!'
            logger.error(f"Erro ao acessar a Wikipedia para: {message}")
            logger.info(f"Resposta do bot: {bot_response_text}")
            return jsonify({'status': 'OK', 'answer': bot_response_text})

if __name__ == "__main__":
    app.run()
