#!/usr/bin/env python3
"""Telegram Bot Automation for Bankrupt Lead App

Automates lead generation and channel promotion for @SpishiSpisat
"""

import requests
import json
import logging
from datetime import datetime
from typing import Optional, Dict, List

# Configuration
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"  # Get from BotFather
CHANNEL_ID = "-1001234567890"  # @SpishiSpisat channel ID
WEB_APP_URL = "https://output.jsbin.com/gixadekugi/latest"

# Logger setup
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class BotAutomation:
    """Manages Telegram bot automation for lead generation"""
    
    def __init__(self, bot_token: str, channel_id: str):
        self.bot_token = bot_token
        self.channel_id = channel_id
        self.api_url = f"https://api.telegram.org/bot{bot_token}"
        self.leads = []
    
    def send_message(self, chat_id: str, text: str, **kwargs) -> Optional[Dict]:
        """Send message to Telegram chat"""
        try:
            data = {
                'chat_id': chat_id,
                'text': text,
                'parse_mode': 'HTML'
            }
            data.update(kwargs)
            
            response = requests.post(f"{self.api_url}/sendMessage", data=data)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logger.error(f"Failed to send message: {e}")
            return None
    
    def post_to_channel(self, text: str, **kwargs) -> Optional[Dict]:
        """Post message to channel"""
        return self.send_message(self.channel_id, text, **kwargs)
    
    def process_lead(self, lead_data: Dict) -> bool:
        """Process incoming lead from form"""
        try:
            # Validate lead data
            required_fields = ['name', 'phone', 'email', 'debt_amount']
            if not all(field in lead_data for field in required_fields):
                logger.warning(f"Invalid lead data: {lead_data}")
                return False
            
            # Add timestamp
            lead_data['timestamp'] = datetime.now().isoformat()
            lead_data['status'] = 'new'
            
            self.leads.append(lead_data)
            logger.info(f"Lead processed: {lead_data['name']} - {lead_data['phone']}")
            
            # Post notification to channel
            notification = self._format_lead_notification(lead_data)
            self.post_to_channel(notification)
            
            return True
        except Exception as e:
            logger.error(f"Error processing lead: {e}")
            return False
    
    def _format_lead_notification(self, lead: Dict) -> str:
        """Format lead data for channel notification"""
        return f"""
<b>킣킲킵킴킾큃c킻킵큃d킽큄b킹 큁b킸킴</b>

<b>Имя:</b> {lead.get('name', 'N/A')}
<b>Телефон:</b> {lead.get('phone', 'N/A')}
<b>Email:</b> {lead.get('email', 'N/A')}
<b>Объём долга:</b> {lead.get('debt_amount', 'N/A')} руб
<b>Время:</b> {lead.get('timestamp', 'N/A')}
"""
    
    def get_leads(self) -> List[Dict]:
        """Return all processed leads"""
        return self.leads
    
    def save_leads_to_file(self, filename: str = 'leads.json') -> bool:
        """Save leads to JSON file"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.leads, f, ensure_ascii=False, indent=2)
            logger.info(f"Leads saved to {filename}")
            return True
        except Exception as e:
            logger.error(f"Failed to save leads: {e}")
            return False


def main():
    """Main automation function"""
    logger.info("Starting Bankrupt Lead Bot Automation")
    
    # Initialize bot
    bot = BotAutomation(BOT_TOKEN, CHANNEL_ID)
    
    # Example: Process test lead
    test_lead = {
        'name': 'Клиент',
        'phone': '+7-999-123-45-67',
        'email': 'client@example.com',
        'debt_amount': '500000',
        'situation': 'Кредитные обязательства'
    }
    
    # Process lead
    bot.process_lead(test_lead)
    
    # Save leads
    bot.save_leads_to_file()
    
    logger.info(f"Total leads processed: {len(bot.get_leads())}")


if __name__ == "__main__":
    main()
