
import os
import json
import requests
import time

from copilot import Copilot
from dotenv import load_dotenv

from telegram import (
    ReplyKeyboardMarkup,
    Update,
    KeyboardButton,
)
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
    )

(ENTRY_STATE,
QUESTION_STATE,
) = range(2)
