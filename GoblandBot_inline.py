import os
import logging
from dotenv import load_dotenv 
load_dotenv()
from telegram import Update, InlineQueryResultVoice
from telegram.ext import Application, InlineQueryHandler, ContextTypes

# Настройка логирования для отладки
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# ВСТАВЬТЕ ВАШ ТОКЕН И ССЫЛКУ
TOKEN = os.environ.get("BOT_TOKEN")
VOICE_FILE_URL = "https://files.catbox.moe/7st33j.ogg"  # Публичная ссылка на OGG файл

async def inline_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Эта функция вызывается, когда пользователь вводит @username_бота в любом чате.
    Она возвращает варианты (результаты), которые пользователь может выбрать.
    """
    query = update.inline_query.query  # Текст, который пользователь ввел после @username
    logger.info(f"Получен inline-запрос: '{query}' от пользователя {update.inline_query.from_user.id}")

    # Создаем один вариант результата - голосовое сообщение
    voice_result = InlineQueryResultVoice(
        id="1",  # Уникальный идентификатор результата (строка)
        voice_url=VOICE_FILE_URL,  # ОБЯЗАТЕЛЬНО: прямая ссылка на OGG файл
        title="Я Король",  # Заголовок, который увидят пользователи
       # caption="Слушайте внимательно!"  # Необязательная подпись к отправленному сообщению
    )

    # Отправляем массив результатов (здесь только один) в Telegram
    await update.inline_query.answer([voice_result], cache_time=0)

def main():
    """Запускаем бота."""
    # Создаем Application
    application = Application.builder().token(TOKEN).build()

    # Регистрируем обработчик inline-запросов
    application.add_handler(InlineQueryHandler(inline_handler))

    # Запускаем бота в режиме опроса серверов Telegram
    print("Inline-бот запущен и ожидает запросы через @username...")
    application.run_polling()

if __name__ == '__main__':
    main()