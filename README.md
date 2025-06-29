# busgv_bot

Bot do Telegram que informa os horários de saída dos ônibus da Grande Vitória - ES

[![GitHub license](https://img.shields.io/github/license/estevao90/busgv_bot.svg)](https://github.com/estevao90/busgv_bot/blob/master/LICENSE)
[![Tests](https://github.com/estevao90/busgv_bot/workflows/Tests/badge.svg)](https://github.com/estevao90/busgv_bot/actions?query=workflow%3ATests)
[![Release](https://github.com/estevao90/busgv_bot/workflows/Release/badge.svg)](https://github.com/estevao90/busgv_bot/actions?query=workflow%3ARelease)

---

## Sumário

- [1. Introdução](#1-introdução)
- [2. Bot no Telegram](#2-bot-no-telegram)
- [3. Parte Original do Projeto](#3-parte-original-do-projeto)
- [4. Parte Experimental](#4-parte-experimental)
- [5. Testes e Observações](#5-testes-e-observações)
- [6. Referências e Autor](#6-referências-e-autor)

---

## 1. Introdução

Este projeto consiste em um bot para o Telegram que permite consultar horários de ônibus da Grande Vitória (ES), utilizando dados da CETURB. O projeto possui uma arquitetura modular, incluindo funcionalidades originais e módulos experimentais para expansão futura.

---

## 2. Bot no Telegram

- **Bot:** [https://t.me/busgv_bot](https://t.me/busgv_bot)
- O bot responde códigos de linha e informa horários em tempo real conforme disponibilidade.
- Para testar horários, utilize códigos de 3 dígitos (ex: 124, 825).
- Linhas do Seletivo não funcionam mais, pois foram desativadas pela CETURB.

### Comandos úteis do Telegram

```shell
# Registrar webhook
curl https://api.telegram.org/bot$TELEGRAM_BOT_TOKEN/setWebHook?url=<ENDPOINT_AWS>

# Verificar status do webhook
curl https://api.telegram.org/bot$TELEGRAM_BOT_TOKEN/getWebhookInfo

# Remover webhook
curl https://api.telegram.org/bot$TELEGRAM_BOT_TOKEN/deleteWebhook

# Obtendo mensagens
curl https://api.telegram.org/bot$TELEGRAM_BOT_TOKEN/getUpdates

# Para obter apenas as novas mensagens
curl https://api.telegram.org/bot$TELEGRAM_BOT_TOKEN/getUpdates?offset=<result[-1].update_id + 1>
```

---

## 3. Parte Original do Projeto

### Instalação do Serverless Framework

```shell
# Necessário Node
sudo npm install -g serverless
sls config tabcompletion install
```

### Ambiente de desenvolvimento

```shell
pipenv install --dev
```

### Deploy

```shell
# Criar arquivo .env com base em .env.default
cp .env.default .env

# Entrar no ambiente pipenv
pipenv shell

# Deploy na AWS
sls deploy

# Excluir deploy
sls remove
```

### Testes

```shell
# Ambiente pipenv
pipenv shell

# Executando testes
python -m pytest -v
```

### Comandos úteis

```shell
# Testar função na AWS
sls invoke -f <function> [-p <event_file_path> -x <context_file_path>]

# Testar função localmente
sls invoke local -f <function> [-p <event_file_path> -x <context_file_path>]

# Lint
pylint funcs/* app/*
```

---

## 4. Parte Experimental

Esta seção contém funcionalidades em desenvolvimento e testes para modularização do bot.

### Como rodar a versão experimental

1. Instale as dependências:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
2. Configure o arquivo `.env` com seu token.
3. Execute:
   ```bash
   python main.py
   ```
4. Expanda funcionalidades criando novos handlers em `handlers/` e serviços em `services/`.

---

## 5. Testes e Observações

- Teste no Telegram com códigos como: 124 (Estrelinha/Jardim da Penha), 825 (Terminal Laranjeiras/Nova Carapina I e II)
- [1] Precisa de 3 algarismos (0xx, 1xx) para testar horários
- [2] Linhas do Seletivo desativadas
- [3] Códigos de consulta conforme disponibilidade da CETURB (0xx a 9xx)

---

## 6. Referências e Autor

- **Fontes:** [https://ceturb.es.gov.br](https://ceturb.es.gov.br)
- **Autor:** [https://github.com/estevao90](https://github.com/estevao90)
