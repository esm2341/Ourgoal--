#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import logging
from dotenv import load_dotenv
from telegram import BotCommand, MenuButton, MenuButtonCommands
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, ConversationHandler, filters
from handlers import (
    start_command,
    menu_command,
    team_selection_callback,
    handle_reason_input,
    handle_experience_input,
    cancel_command,
    stats_command,
    clear_applications_command,
    handle_admin_reply,
    handle_admin_decision,
    handle_end_conversation,
    handle_unknown_message
)
from config import ASKING_REASON, ASKING_EXPERIENCE, ADMIN_GROUP_ID

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", 
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

def main():
    """Start the bot."""
    # Get bot token from environment
    bot_token = os.getenv("BOT_TOKEN")
    if not bot_token:
        logger.error("BOT_TOKEN environment variable is required!")
        return
    
    # Create application
    application = Application.builder().token(bot_token).build()
    
    # Set up menu button and commands after bot initialization
    async def post_init(application):
        """Setup bot commands and menu button after bot is ready."""
        commands = [
            BotCommand("start", "بدء استخدام البوت والتقديم للتيمز"),
            BotCommand("menu", "عرض القائمة الرئيسية والخيارات المتاحة"),
            BotCommand("cancel", "إلغاء العملية الحالية"),
            BotCommand("stats", "إحصائيات التقديمات (للإدارة فقط)"),
            BotCommand("clear", "مسح جميع التقديمات (للإدارة فقط)")
        ]
        
        # Set commands
        await application.bot.set_my_commands(commands)
        
        # Set menu button
        menu_button = MenuButtonCommands()
        await application.bot.set_chat_menu_button(menu_button=menu_button)
    
    # Set post init callback
    application.post_init = post_init
    
    # Define conversation handler for team applications
    conversation_handler = ConversationHandler(
        entry_points=[
            CallbackQueryHandler(team_selection_callback, pattern="^team_")
        ],
        states={
            ASKING_REASON: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, handle_reason_input)
            ],
            ASKING_EXPERIENCE: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, handle_experience_input)
            ],
        },
        fallbacks=[
            CommandHandler("cancel", cancel_command),
            CommandHandler("start", start_command)
        ],
        allow_reentry=True
    )
    
    # Add handlers
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("menu", menu_command))
    application.add_handler(CommandHandler("stats", stats_command))
    application.add_handler(CommandHandler("clear", clear_applications_command))
    application.add_handler(CommandHandler("cancel", cancel_command))
    application.add_handler(conversation_handler)
    
    # Handle admin decision buttons
    application.add_handler(CallbackQueryHandler(handle_admin_decision, pattern="^(accept_|reject_)"))
    
    # Handle end conversation button
    application.add_handler(CallbackQueryHandler(handle_end_conversation, pattern="^end_chat_"))
    
    # Handle admin replies (only from admin group)
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND & filters.Chat(ADMIN_GROUP_ID), handle_admin_reply))
    
    # Handle unknown messages
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_unknown_message))
    
    # Log startup
    logger.info("Bot started successfully!")
    
    # Run the bot
    application.run_polling(allowed_updates=["message", "callback_query"])

if __name__ == "__main__":
    main()
