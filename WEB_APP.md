# Web App - Спеши Списать

## Overview
Это web application для сбора лидов по банкротству через Telegram Web App.

## Live URL
https://jsbin.com/jificuvixi/1

https://output.jsbin.com/jificuvixi/1

## Bot Integration
- Bot: @tg_profii_bot
- Bot Token: 8531981853:AAFJdULpNyW90EFE9oS9Lgx0ZyxHnXoR48
- Channel: @SpishiSpisat
- Web App Name: profii

## Features
- Название: Спеши Списать
- Описание: Бесплатная консультация по банкротству
- Lead form с полями:
  - Полное имя (обязательно)
  - Номер телефона (обязательно)
  - Email (опционально)
  - Объем долга (обязательно)
  - Конкретная ситуация (опционально)

## Data Submission
При нажатии кнопки "ПОЛУЧИТЬ КОНСУЛЬТАЦИЮ" данные отправляются:
1. На Telegram Bot API: https://api.telegram.org/bot{TOKEN}/sendMessage
2. В канал: @SpishiSpisat
3. С форматированным сообщением, содержащим все данные лида

## Success Message
После успешной отправки показывается сообщение: "Спасибо! Мы получили вашу заявку"

## Technical Stack
- HTML5
- CSS3 (с градиентом и адаптивным дизайном)
- JavaScript (Fetch API для отправки на Telegram)
- LocalStorage для временного хранения

## Deployment
Деплойман на JSBin: https://jsbin.com/jificuvixi/1
