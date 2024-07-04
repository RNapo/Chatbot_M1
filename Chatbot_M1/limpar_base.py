# Trecho de código criado para limpeza da base de dados caso necessário.

from chatterbot import ChatBot

bot = ChatBot('ChatBot')

bot.storage.drop()