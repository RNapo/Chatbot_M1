import pytest
import sys
import os
from flask import Flask
from flask.testing import FlaskClient

# Adiciona o diretório raiz ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app_bkp import app

# Configura uma fixture do pytest que cria um cliente de teste para o Flask
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client  # Fornece o client para os testes

# Testa a rota home
def test_home(client: FlaskClient):
    """Testa a rota home"""
    response = client.get('/')  # Faz uma solicitação GET para a rota home
    assert response.status_code == 200 
    assert b'Chatbot' in response.data  # Verifica se o texto 'Chatbot' está presente na resposta

# Testa a resposta do chatbot
def test_chatbot_response(client: FlaskClient):
    """Testa a resposta do chatbot"""
    response = client.post('/pesquisa', data={'messageText': 'Oi'})  # Faz uma solicitação POST para a rota /pesquisa
    json_data = response.get_json()
    assert response.status_code == 200
    assert json_data['status'] == 'OK'
    assert json_data['answer'] in ["Ola", "Como vai voce?"]  # Verifica se a resposta do chatbot é uma das esperadas

