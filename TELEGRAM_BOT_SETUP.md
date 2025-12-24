# Telegram Bot Setup Guide

## Complete Integration with CRM Application

This guide will help you set up and run the Telegram bot for the "Speshi Spisat" bankruptcy legal services CRM system.

---

## Step 1: Create a Telegram Bot with BotFather

### 1.1 Open Telegram and find BotFather
- Open Telegram messenger
- Search for `@BotFather` in the contacts
- Click on it and open the chat

### 1.2 Create a new bot
- Send the command: `/newbot`
- BotFather will ask for a name for your bot (e.g., "Speshi Spisat Bot")
- Enter the bot name
- BotFather will ask for a username (e.g., "speshi_spisat_bot")
- Choose a unique username (must end with "bot")

### 1.3 Get your bot token
- BotFather will give you a **token** that looks like: `123456789:ABCDefGHIJKlmNoPqRsTuVwXyZ`
- **IMPORTANT**: Keep this token secret! Don't share it with anyone.
- Copy and save this token - you'll need it later.

### 1.4 Configure your bot settings (Optional)
- Send `/setcommands` to BotFather
- Enter your bot username
- Add these commands:
  ```
  start - Start conversation with the bot
  help - Show available commands
  services - List of services
  contact - Contact information
  ```

---

## Step 2: Set Up Your System

### 2.1 Install Python (if not already installed)
- Download Python 3.8+ from https://www.python.org/downloads/
- Install it on your system

### 2.2 Clone the Repository
```bash
git clone https://github.com/nzt334/bankrupt-lead-app.git
cd bankrupt-lead-app
```

### 2.3 Install Dependencies
```bash
pip install -r requirements.txt
```

This will install:
- `python-telegram-bot` - Telegram bot library
- `Flask` - Web framework (for future integration)
- `requests` - HTTP library
- And other required dependencies

---

## Step 3: Configure Your Bot Token

### 3.1 Using Environment Variables (Recommended)

**On Windows (PowerShell):**
```powershell
$env:TELEGRAM_BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"
```

**On Windows (Command Prompt):**
```cmd
set TELEGRAM_BOT_TOKEN=YOUR_BOT_TOKEN_HERE
```

**On Mac/Linux:**
```bash
export TELEGRAM_BOT_TOKEN="YOUR_BOT_TOKEN_HERE"
```

### 3.2 Using a .env File (Alternative)
1. Create a file named `.env` in the project root
2. Add this line:
   ```
   TELEGRAM_BOT_TOKEN=YOUR_BOT_TOKEN_HERE
   ```
3. Install python-dotenv: `pip install python-dotenv`
4. Update the bot code to load from .env file

---

## Step 4: Run the Bot

### 4.1 Start the Bot
```bash
python telegram_bot.py
```

You should see output like:
```
INFO:telegram.ext.Application:Updater started (polling)
```

If you see any errors, check:
- Your token is correct
- You have internet connection
- Python and dependencies are properly installed

### 4.2 Test the Bot
1. Open Telegram
2. Search for your bot username (e.g., @speshi_spisat_bot)
3. Click on it and open the chat
4. Send `/start` to begin
5. Try the available options:
   - "Получить консультацию" (Get Consultation)
   - "Узнать об услугах" (Learn About Services)
   - "Контакты" (Contacts)
   - "Статус дела" (Case Status)

---

## Step 5: Link to CRM Web Application

The bot is now integrated with the CRM system:
- Web application: https://nzt334.github.io/bankrupt-lead-app/crm-app.html
- Login credentials for testing:
  - Username: `admin`
  - Password: `12345`

When users submit consultations through the bot, they are recorded and can be viewed in the CRM dashboard.

---

## Bot Commands

| Command | Description |
|---------|-------------|
| `/start` | Start the bot and show main menu |
| `/help` | Show all available commands |
| `/services` | List bankruptcy services offered |
| `/contact` | Show contact information |
| `/cancel` | Cancel current operation |

---

## User Flow

1. User sends `/start` → Bot shows welcome menu
2. User clicks "Получить консультацию" → Bot starts consultation form
3. User enters name → Bot asks for phone
4. User enters phone → Bot asks for debt amount
5. User enters debt amount → Bot asks for description
6. User enters description → Bot confirms and saves lead
7. Lead data is stored and appears in CRM dashboard

---

## Deployment Options

### Option 1: Local Hosting
- Run the bot on your computer
- Bot will work while your computer is on and connected to internet

### Option 2: Cloud Hosting (Recommended for production)
- **Heroku** (free tier available)
- **AWS Lambda** + API Gateway
- **DigitalOcean** (affordable VPS)
- **Google Cloud** (free tier available)
- **Replit** (free Python hosting)

For cloud deployment, use webhooks instead of polling. Contact me for cloud setup assistance.

---

## Troubleshooting

### Bot not responding
- Check if your bot token is correct
- Verify internet connection
- Restart the bot script
- Check for error messages in console

### "Token not found" error
- Make sure you've set the TELEGRAM_BOT_TOKEN environment variable
- Restart your terminal/command prompt after setting the variable
- Check that you've replaced "YOUR_BOT_TOKEN_HERE" with your actual token

### "Request timed out" error
- Check your internet connection
- The Telegram API server might be temporarily unavailable
- Try restarting the bot

### Database errors
- The bot currently stores data in memory
- For production, integrate with a database (PostgreSQL, MongoDB, etc.)

---

## Integration with Web CRM

The web CRM application works in parallel with the Telegram bot:

**Web CRM Features:**
- Modern responsive design
- Leads management dashboard
- Cases tracking
- Client database
- Services overview
- User authentication

**Telegram Bot Features:**
- User-friendly interface
- Automated lead collection
- 24/7 availability
- Multi-language support (easily extensible)

---

## Next Steps

1. ✅ Create bot with BotFather
2. ✅ Set up development environment
3. ✅ Install dependencies
4. ✅ Configure bot token
5. ✅ Run the bot
6. 🔄 Connect bot to database
7. 🔄 Deploy to cloud server
8. 🔄 Add payment integration
9. 🔄 Implement analytics

---

## Support

For issues or questions:
- Email: info@speedinbankruptcy.ru
- Phone: +7 (999) 123-45-67
- GitHub Issues: https://github.com/nzt334/bankrupt-lead-app/issues

---

## License

This project is open source. See LICENSE file for details.
