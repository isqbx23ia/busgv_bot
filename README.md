*Testes no Telegram: 124 (Estrelinha/Jardim da Penha), 825 (Terminal Larnajeiras/Nova Carapina I e II);*
*Bot:  [https://t.me/busgv_bot] ;
Notas: 1: Precisa de 3 algarismos (0xx,1xx) para testar os horários;
       2: Linhas do Seletivo não funcionam mais, pois foram desativadas;
       3: Códigos de consulta referentes à disponiblidade da Ceturb (0xx a 9xx);

Fontes:[https://ceturb.es.gov.br/]
Autor:[ ](https://github.com/estevao90)
--------------------------------------------------------------------------------------------------------------------------------------------------
# busgv_bot

Bot do Telegram que informa os horários de saída dos ônibus da Grande Vitória - ES

[![GitHub license](https://img.shields.io/github/license/estevao90/busgv_bot.svg)](https://github.com/estevao90/busgv_bot/blob/master/LICENSE)
[![Tests](https://github.com/estevao90/busgv_bot/workflows/Tests/badge.svg)](https://github.com/estevao90/busgv_bot/actions?query=workflow%3ATests)
[![Release](https://github.com/estevao90/busgv_bot/workflows/Release/badge.svg)](https://github.com/estevao90/busgv_bot/actions?query=workflow%3ARelease)

## Instalação do Serverless Framework

```shell
# Instalando serverless
# Necessário Node
sudo npm install -g serverless

# Instalando autocomplete
sls config tabcompletion install
```

## Ambiente de DEV

```shell
# Pipenv
pipenv install --dev
```

## Deploy

```shell
# Criar arquivo .env com base em .env.default
# Indicar o valor das variáveis
cp .env.default .env

# Pipenv
pipenv shell

# Deploy na AWS
sls deploy

# Excluir deploy
sls remove
```

## Telegram

```shell
# Registrar webhook
curl https://api.telegram.org/bot$TELEGRAM_BOT_TOKEN/setWebHook?url=<ENDPOINT_AWS>

# Verificar status do webhook
curl https://api.telegram.org/bot$TELEGRAM_BOT_TOKEN/getWebhookInfo
```

## Desenvolvimento

```shell
# Remover webhook
curl https://api.telegram.org/bot$TELEGRAM_BOT_TOKEN/deleteWebhook

# Obtendo mensagens
curl https://api.telegram.org/bot$TELEGRAM_BOT_TOKEN/getUpdates

# Para obter apenas as novas mensagens
curl https://api.telegram.org/bot$TELEGRAM_BOT_TOKEN/getUpdates?offset=<result[-1].update_id + 1>
```

### Testes

```shell
# Ambiente pipenv
pipenv shell

# Executando testes
python -m pytest -v
```

## Comandos úteis

```shell
# Testar função na AWS
sls invoke -f <function> [-p <event_file_path> -x <context_file_path>]

# Testar função localmente
sls invoke local -f <function> [-p <event_file_path> -x <context_file_path>]

# Lint
pylint funcs/* app/*
```
