import aiohttp
import feedparser

# Асинхронная функция для получения новостей
async def fetch_rss(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


# Асинхронная функция для обработки новостей по категории
async def get_news(message, *categories):

    current_position = 0

    # URL RSS-ленты
    url = 'https://lenta.ru/rss'

    rss_content = await fetch_rss(url)

    feed = feedparser.parse(rss_content)

    # Фильтруем новости по категории
    for category in categories:
        filtered_entries = []
        for entry in feed.entries:
            if 'category' in entry:
                if category.lower() in entry.category.lower():
                    filtered_entries.append(entry)

        # Вычисляем, какие новости выводить
        start = current_position
        end = current_position + 5
        news_to_display = filtered_entries[start:end]

        if news_to_display:
            for entry in news_to_display:
                await message.answer(f"""Заголовок: {entry.title}\nСсылка: {entry.link}\nКатегория: {entry.category}""")

        else:
            print(f"Нет новостей категории {category} для отображения или достигнут конец ленты.")

