Projeto de Chatbot da M1 Motors referente ao teste

As tecnologias utilizadas nesse projeto foram:

**Python (Versão 3.6.8)**,
**Javascript**,
**HTML**,
**CSS**,
**Bootstrap**

Bibliotecas 

**chatterbot**,
**Flask**,
**BeautifulSoup**

O chatbot foi desenvolvido com intuito de conseguir responder ao usuario, pesquisar na web algumas palavras chaves (específicas)

Para o treinamento do bot foram criadas duas listas em arquivos .yml localizadas no diretório /data

Foi criado o arquivo limpar_base.py para caso necessário a limpeza da base de dados, se por algum motivo a base ficar muito poluída ou algo do tipo.

**pytest**

Utilização da ferramenta pytest para realizar alguns testes de funcionalidade do bot

Testando o app e página principal:

Verifica se a página inicial carrega corretamente.
Verifica se um texto específico está presente na resposta.
Testando a Resposta do Chatbot (test_chatbot_response):

Envia uma mensagem "Oi" para a rota /pesquisa.
Verifica se a resposta do chatbot é adequada.
Testando a Funcionalidade de Pesquisa no Wikipedia (test_chatbot_fallback):

Usado monkeypatch para simular uma resposta do Wikipedia.
Verifica se a resposta do chatbot ao não saber responder está correta.

Rodando o teste, usar comando abaixo:

pytest tests\test_app.py

**Rodando o app**

Abaixo instruções para rodar o projeto:

Primeiramente clonar o projeto no Github:

git clone https://github.com/RNapo/Chatbot_M1.git

Após clonar, digite no terminal:

cd Chatbot_M1\

Criar um ambiente virtual, comando abaixo:

py -m venv venv

Ativar o ambiente virtual antes de prosseguir (Deve aparecer algo parecido com  (venv) em verde no seu terminal, isso quer dizer que esta ativo)

digitar o seguinte comando para ativar:  venv\Scripts\activate

Obs: caso tenha dificuldade na ativação do ambiente com o comando acima, navegar até o diretorio Script dentro da pasta venv criada automaticamente e digitar activate no terminal e enter, assim irá habilitar o ambiente.

Com o ambiente virtual ativo, seguir com o comando abaixo para instalação das dependencias necessarias

pip install -r requirements.txt

Após isso, rodar o projeto com os comandos abaixo

Flask run app.py   ou   py app.py
