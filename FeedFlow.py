import feedparser  # RSS feed ko parse karne ke liye
import requests    # RSS feed ko internet se fetch karne ke liye

# RSS Feed URLs ki ek list banani hai (user input nahi chahiye)
rss_urls = [
    "https://rss.nytimes.com/services/xml/rss/nyt/World.xml",  # New York Times - World News
    "https://feeds.bbci.co.uk/news/rss.xml"  # BBC News RSS Feed
]

# Step 2: Counter variable banani hai (jo track karega hum kis feed pe hain)
index = 0  
total_feeds = len(rss_urls)  # Kitni feeds hain total

# Jab tak sari feeds process nahi hoti, tab tak loop chalega
while index < total_feeds:
    url = rss_urls[index]  # Current RSS feed URL
    print("\nFetching RSS Feed:", url)  # Bata rahe hain konsa feed fetch ho raha hai
    
    try:
        # Feed ko parse karna
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        newsfeed = feedparser.parse(response.content)

        # Agar feed me koi content hai to show karein
        if newsfeed.entries:
            print("\n🔗 Title: ", newsfeed.feed.title)
            print("📌 Description: ", newsfeed.feed.get("description", "No description available"))
            print("--------------------------------------------------")

            # Counter variable for articles
            article_index = 0  
            total_articles = len(newsfeed.entries)  # Kitne articles hain

            # Jab tak 5 articles display nahi ho jate, loop chalayenge
            while article_index < min(5, total_articles):  # Sirf pehle 5 show karega
                entry = newsfeed.entries[article_index]
                print(f"📰 {entry.title}")
                print(f"📇 {entry.description}")
                print(f"🔗 {entry.link}\n")
                article_index += 1  # Next article pe move karne ke liye

        else:
            print("⚠️ No news found in this feed!")

    except Exception as e:
        print(f"❌ Error fetching feed: {e}")

    index += 1  # Next RSS feed pe move karne ke liye
