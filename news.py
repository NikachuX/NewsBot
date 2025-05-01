import aiohttp
import feedparser


# Функция для получения новостей
async def fetch_rss(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


# Функция для обработки новостей по категории
async def get_news(message, categories):
    url = 'https://lenta.ru/rss'
    rss_content = await fetch_rss(url)
    feed = feedparser.parse(rss_content)
    for category in categories:
        filtered_entries = []
        for entry in feed.entries:
            if 'category' in entry:
                if category.lower() in entry.category.lower():
                    filtered_entries.append(entry)
        news_to_display = filtered_entries[0:5]
        if news_to_display:
            for entry in news_to_display:
                await message.answer(f"""Заголовок: {entry.title}\nСсылка: {entry.link}\nКатегория: {entry.category}""")
        else:
            await message.answer(f"Нет новостей категории {category} для отображения.")

async def get_news_keywords(message, keywords):
    url = 'https://lenta.ru/rss'
    categories = ['Мир', 'Наука и техника', 'Культура', 'Экономика', 'Спорт']
    rss_content = await fetch_rss(url)
    feed = feedparser.parse(rss_content)
    for category in categories:
        filtered_entries = []
        for entry in feed.entries:
            if any(word.lower() in entry.title.lower() for word in keywords.split('/')):
                if category.lower() in entry.category.lower():
                    filtered_entries.append(entry)
        news_to_display = filtered_entries[0:5]
        if news_to_display:
            for entry in news_to_display:
                await message.answer(f"""Заголовок: {entry.title}\nСсылка: {entry.link}\nКатегория: {entry.category}""")
        else:
            await message.answer(f"Нет новостей категории {category} для отображения по ключевым словам.")