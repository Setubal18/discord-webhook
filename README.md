# WebHook-discord
### Versão 0.0.0
Simples, webhook para discord


## Dev 
### Run Local
Para rodar local basta executar o comando `python -m flask run` ou `flask run`

### Dependências 
 Todos as dependências necessárias estão no requiriments.txt, 
 para baixa-las basta `pip install -r requirements.txt`."

### Ambientes
Lemprese de criar o ambiente virtual python com comando `python -m venv [nome do ambiente]`, ative o ambiente usando
`source [nome do ambiente]/bin/activate`.<br>
No projeto tambem temos o .env e .flaskenv

## .env
```txt
URL = url do webhook do discord
WEBHOOK_TOKEN = token do webhook
WEBHOOK_ID = id do webhook
```

## .flaskenv
```
FLASK_APP= arquivo principal
FLASK_ENV=ambiente
FLASK_DEBUG= se esta em debug, em dev recomendo utilizar
```