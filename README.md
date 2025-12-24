# Bankrupt Lead App - Telegram Channel Promotion System

## Overview
Automated system for promoting the Спеши Списать (@SpishiSpisat) Telegram channel with lead generation and analytics.

## Features
- **Lead Generation**: Web-based form for collecting bankrupt case leads
- **Telegram Bot Integration**: Automated bot for channel engagement
- **Web App**: Embedded web application for lead capture
- **Analytics**: Tracking and conversion monitoring

## Project Structure
```
├── bot_automation.py       # Telegram bot automation script
├── lead_processor.py       # Lead data processing and storage
├── web_app/               # Web application files
│   ├── index.html        # Lead form interface
│   └── styles.css        # Form styling
└── config.json            # Configuration file
```

## Components

### 1. Telegram Channel
- **Handle**: @SpishiSpisat
- **Topic**: Bankruptcy Consultation
- **Subscribers**: 300+
- **Content**: Case studies, legal templates, expert advice

### 2. Telegram Bot
- **Handle**: @tg_profii_bot
- **Web App**: profii
- **Function**: Lead distribution and bot responses

### 3. Lead Generation Form
- **URL**: https://output.jsbin.com/jificuvixi/1/latest
- **Fields**: Name, Phone, Email, Debt Amount, Situation
- **Backend**: JSON-based storage

## Getting Started

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Configure environment variables
4. Run bot automation: `python bot_automation.py`

## Configuration
Edit `config.json` with your API credentials and settings.

## License
Private project for lead generation and channel promotion
