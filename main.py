import requests
import json
from telegram.ext import Updater, CommandHandler

# Your NewsAPI key
newsapi_key = "YOUR_API_KEY"

def get_news(topic):
    url = f"https://newsapi.org/v2/top-headlines?q={topic}&apiKey={newsapi_key}"
    response = requests.get(url)
    data = json.loads(response.text)
    articles = data["articles"]
    return articles

def news(update, context):
    topic = " ".join(context.args)
    if not topic:
        update.message.reply_text("Please provide a topic for the news.")
        return
    articles = get_news(topic)
    for article in articles:
        update.message.reply_text(article["title"] + "\n" + article["url"])

def main():
    # Your Telegram token
    updater = Updater("YOUR_TOKEN", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("news", news))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
