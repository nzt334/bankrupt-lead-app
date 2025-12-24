#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Telegram Bot for Bankruptcy Legal Services CRM
Integrates with the web-based CRM application
"""

import logging
import os
import json
from datetime import datetime
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, ConversationHandler

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# States for conversation
ASKING_NAME, ASKING_PHONE, ASKING_DEBT, ASKING_DESCRIPTION = range(4)

# Store leads data (in production, use a database)
leads_data = []

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    welcome_text = (
        f"Привет, {user.first_name}!\n\n"
        f"Добро пожаловать в систему консультаций по банкротству 'Спеши Списать'.\n\n"
        f"Я помогу вам получить бесплатную консультацию от опытных юристов по вопросам банкротства.\n\n"
        f"Какие услуги вас интересуют?"
    )
    
    keyboard = [
        ['Получить консультацию'],
        ['Узнать об услугах'],
        ['Статус дела'],
        ['Контакты']
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    
    await update.message.reply_text(welcome_text, reply_markup=reply_markup)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    help_text = (
        "Доступные команды:\n\n"
        "/start - Начать разговор\n"
        "/help - Справка\n"
        "/services - Список услуг\n"
        "/contact - Контактная информация\n"
        "/status - Статус вашего дела\n"
    )
    await update.message.reply_text(help_text)

async def services_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Show available services."""
    services_text = (
        "📋 Наши услуги по банкротству:\n\n"
        "1️⃣ Консультация - Бесплатная первичная консультация (от 30 минут)\n"
        "2️⃣ Подготовка документов - Полное оформление всех необходимых документов\n"
        "3️⃣ Представление в суде - Полное представление ваших интересов в суде\n"
        "4️⃣ Мониторинг дела - Постоянное отслеживание развития вашего дела\n\n"
        "💰 Цены уточняйте у наших менеджеров"
    )
    await update.message.reply_text(services_text)

async def contact_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Show contact information."""
    contact_text = (
        "📞 Контактная информация:\n\n"
        "📱 Телефон: +7 (999) 123-45-67\n"
        "📧 Email: info@speedinbankruptcy.ru\n"
        "🕒 Время работы: Пн-Пт 09:00-18:00 (МСК)\n"
        "📍 Адрес: г. Москва, ул. Примера, д. 1\n\n"
        "💬 Или нажмите 'Получить консультацию' для заполнения формы"
    )
    await update.message.reply_text(contact_text)

async def consultation_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Start the consultation form."""
    await update.message.reply_text(
        "Спасибо за интерес к нашим услугам!\n\n"
        "Заполните форму консультации:\n\n"
        "Укажите ваше полное имя:",
        reply_markup=ReplyKeyboardRemove()
    )
    return ASKING_NAME

async def ask_phone(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Ask for phone number."""
    context.user_data['name'] = update.message.text
    await update.message.reply_text(
        f"Спасибо, {context.user_data['name']}!\n\n"
        "Укажите ваш номер телефона в формате +7 (XXX) XXX-XX-XX:"
    )
    return ASKING_PHONE

async def ask_debt(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Ask for debt amount."""
    context.user_data['phone'] = update.message.text
    await update.message.reply_text(
        "Укажите общую сумму вашего долга (например: 500000 руб):"
    )
    return ASKING_DEBT

async def ask_description(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Ask for description."""
    context.user_data['debt'] = update.message.text
    await update.message.reply_text(
        "Кратко опишите вашу ситуацию (необязательно):\n"
        "(Или напишите '-' для пропуска)"
    )
    return ASKING_DESCRIPTION

async def save_consultation(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Save consultation request."""
    description = update.message.text if update.message.text != '-' else ''
    context.user_data['description'] = description
    
    # Save to leads data
    lead = {
        'id': len(leads_data) + 1,
        'name': context.user_data.get('name'),
        'phone': context.user_data.get('phone'),
        'debt': context.user_data.get('debt'),
        'description': description,
        'date': datetime.now().isoformat(),
        'status': 'Новый'
    }
    leads_data.append(lead)
    
    # Log the lead
    logger.info(f"New lead: {lead}")
    
    # Send confirmation
    confirmation_text = (
        "✅ Спасибо! Ваша заявка принята.\n\n"
        f"📋 Ваши данные:\n"
        f"Имя: {lead['name']}\n"
        f"Телефон: {lead['phone']}\n"
        f"Сумма долга: {lead['debt']}\n\n"
        f"Наш менеджер свяжется с вами в течение 30 минут.\n\n"
        f"Спасибо, что выбрали нас!"
    )
    
    keyboard = [
        ['Получить консультацию'],
        ['Узнать об услугах'],
        ['Контакты']
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    
    await update.message.reply_text(confirmation_text, reply_markup=reply_markup)
    return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Cancel the consultation form."""
    await update.message.reply_text(
        "Форма отменена.\n"
        "Свяжитесь с нами по телефону +7 (999) 123-45-67",
        reply_markup=ReplyKeyboardRemove()
    )
    return ConversationHandler.END

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle regular messages."""
    text = update.message.text
    
    if 'Получить консультацию' in text:
        return await consultation_start(update, context)
    elif 'Узнать об услугах' in text:
        await services_command(update, context)
    elif 'Контакты' in text:
        await contact_command(update, context)
    elif 'Статус дела' in text:
        await update.message.reply_text(
            "Для проверки статуса дела обратитесь к менеджеру:\n"
            "+7 (999) 123-45-67\n"
            "или посетите сайт: https://nzt334.github.io/bankrupt-lead-app/"
        )
    else:
        await update.message.reply_text(
            "Выберите один из предложенных вариантов или используйте команду /help"
        )

def main() -> None:
    """Start the bot."""
    # Create the Application
    token = os.getenv('TELEGRAM_BOT_TOKEN', 'YOUR_BOT_TOKEN_HERE')
    application = Application.builder().token(token).build()
    
    # Add conversation handler for consultation
    conv_handler = ConversationHandler(
        entry_points=[MessageHandler(filters.Regex('^(Получить консультацию)$'), consultation_start)],
        states={
            ASKING_NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, ask_phone)],
            ASKING_PHONE: [MessageHandler(filters.TEXT & ~filters.COMMAND, ask_debt)],
            ASKING_DEBT: [MessageHandler(filters.TEXT & ~filters.COMMAND, ask_description)],
            ASKING_DESCRIPTION: [MessageHandler(filters.TEXT & ~filters.COMMAND, save_consultation)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )
    
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('help', help_command))
    application.add_handler(CommandHandler('services', services_command))
    application.add_handler(CommandHandler('contact', contact_command))
    application.add_handler(conv_handler)
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Run the bot
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
