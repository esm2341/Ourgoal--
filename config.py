#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Bot configuration
BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_GROUP_ID = int(os.getenv("ADMIN_GROUP_ID", "0"))

# Conversation states
ASKING_REASON = 1
ASKING_EXPERIENCE = 2

# Team definitions
TEAMS = {
    "team_exams": "تيم الاختبارات",
    "team_collections": "تيم التجميعات", 
    "team_social": "تيم السوشيال",
    "team_support": "تيم الدعم الفني"
}

# Data files
APPLICATIONS_FILE = "applications.json"
USERS_FILE = "users.json"
STATS_FILE = "stats.json"

# Messages in Arabic (Egyptian dialect)
WELCOME_MESSAGE = """
مرحباً بك في بوت التقديم لتيمز Our Goal! 🎯

يسعدنا إنك حابب تكون جزء من فريقنا وتشاركنا في تحقيق النجاح.

اختار التيم اللي حابب تنضم له من الأزرار اللي تحت:

💡 <b>نصيحة:</b> يمكنك استخدام /menu لعرض القائمة الرئيسية في أي وقت
"""

TEAM_SELECTION_MESSAGE = """
ممتاز! اختارك لـ {team_name} 👏

عشان نقدر نقيم طلبك بشكل أفضل، محتاجين نسألك كام سؤال:

السؤال الأول: ليه عايز تنضم لـ {team_name}؟ 
إيه اللي خلاك تختار التيم دا تحديداً؟

أكتب إجابتك بكل صراحة وصدق 😊
"""

EXPERIENCE_QUESTION = """
شكراً لإجابتك! 🙏

السؤال التاني: عندك أي خبرة أو مهارات متعلقة بشغل {team_name}؟

لو عندك خبرة، اكتب عنها بالتفصيل.
لو مش عندك خبرة، متقلقش وقول كدا عادي - الأهم هو الحماس والاستعداد للتعلم! 💪
"""

APPLICATION_SUBMITTED = """
تم تسليم طلبك بنجاح! 🎉

شكراً ليك على اهتمامك بالانضمام لـ {team_name}. 
هيتم مراجعة طلبك وهنرد عليك قريباً إن شاء الله.

نتمنى نشوفك معانا في التيم! 🤝

يمكنك الضغط على /start للتقديم على تيم تاني لو عايز.
"""

ALREADY_APPLIED = """
أنت قدمت على {team_name} قبل كدا! 😊

يمكنك الضغط على /start لتقديم على تيم تاني.
"""

CANCEL_MESSAGE = """
تم إلغاء طلب التقديم. 

يمكنك الضغط على /start للبدء من جديد.
"""

UNKNOWN_MESSAGE = """
مرحبا بك في Our Goal! 🎯

يمكنك الضغط على /start للبدء من جديد أو /menu لعرض القائمة الرئيسية.
"""

NO_STATS_PERMISSION = """
معذرة، الأمر دا مخصص للادمن بس.
"""

STATS_HEADER = """
📊 إحصائيات طلبات التقديم

إجمالي الطلبات: {total_applications}
عدد المتقدمين: {total_users}

التفاصيل حسب التيم:
"""

STATS_TEAM_FORMAT = """
🔹 {team_name}: {count} طلب
"""

NO_APPLICATIONS_YET = """
لسه مفيش طلبات تقديم.
"""
