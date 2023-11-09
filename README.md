# Simple template Telegram bot 
## using:
- docker-compose
- poetry
- loguru
- aiogram

## Preparation
```sh
mkdir bot && cd $_
git clone https://github.com/akmalovaa/telegrambot-template-docker .
cd bot
cp env.example .env
nano .env
```
Change .env past your TOKEN from BotFather (save and quit)


## Starting
```sh
docker-compose up -d
```


### Сhecking the work
```sh
docker ps
tail -f logs/bot.log
```

### Project plans
- Make Gitlab CI/CD
- Add data base
- Add Flask web intefaces
