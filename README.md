# Our Goal Telegram Bot

A comprehensive Telegram bot for the "Our Goal" student group that manages team applications with full two-way communication between users and administrators.

## Features

### For Users
- 🎯 **Team Application System**: Apply to join specific teams with a simple interface
- 📝 **Multi-step Application Process**: Answer questions about motivation and experience
- 💬 **Two-way Communication**: Chat directly with admins after application submission
- 🔄 **Reapplication Support**: Apply again after admin clears applications
- 📱 **Arabic Language Support**: Full interface in Arabic (Egyptian dialect)

### For Administrators
- 📊 **Application Statistics**: View detailed stats with `/stats` command
- ✅ **Quick Decision Making**: Accept/reject applications with inline buttons
- 💬 **Direct Communication**: Reply to applicants and maintain ongoing conversations
- 🗑️ **Application Management**: Clear all applications with `/clear` command
- 📢 **Admin Group Integration**: All notifications sent to designated admin group

## Available Teams

- **تيم الاختبارات** (Testing Team)
- **تيم التجميعات** (Collections Team)  
- **تيم السوشيال** (Social Media Team)
- **تيم الدعم الفني** (Technical Support Team)

## Commands

### User Commands
- `/start` - Begin application process
- `/menu` - Show main menu options
- `/cancel` - Cancel current application

### Admin Commands (Admin Group Only)
- `/stats` - View application statistics
- `/clear` - Clear all applications and reset system

## Setup

### Prerequisites
- Python 3.7+
- Telegram Bot Token from [@BotFather](https://t.me/BotFather)
- Admin Group ID

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ourgoal-telegram-bot.git
cd ourgoal-telegram-bot
```

2. Install dependencies:
```bash
pip install python-telegram-bot python-dotenv
```

3. Create environment file:
```bash
cp .env.example .env
```

4. Configure environment variables in `.env`:
```
BOT_TOKEN=your_bot_token_here
ADMIN_GROUP_ID=your_admin_group_id_here
```

5. Run the bot:
```bash
python main.py
```

## Architecture

The bot follows a modular architecture:

- **`main.py`** - Application entry point and handler registration
- **`config.py`** - Configuration management and Arabic message templates
- **`handlers.py`** - Message handlers and conversation flow logic
- **`data_manager.py`** - Data persistence and application management
- **`applications.json`** - Application data storage (created at runtime)
- **`users.json`** - User data storage (created at runtime)

## Data Flow

1. User starts with `/start` command
2. Bot displays team selection with inline buttons
3. User selects team → Bot asks for application reason
4. User provides reason → Bot asks for experience
5. User provides experience → Application saved and forwarded to admin
6. Admin can accept/reject with buttons or start conversation
7. Users can reply to admin messages creating ongoing chat

## Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `BOT_TOKEN` | Telegram bot token from BotFather | Yes |
| `ADMIN_GROUP_ID` | Telegram group ID for admin notifications | Yes |

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support and questions, please contact the Our Goal team or create an issue in this repository.