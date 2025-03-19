# 📰 FeedFlow - RSS News Fetcher

FeedFlow is a lightweight and fast **command-line RSS feed reader** that fetches and displays the latest news from multiple RSS sources. Stay updated with breaking news, technology updates, and global events—all from your terminal! 🚀

---

## 🌟 Features
- Fetches news from **multiple RSS feeds**
- Displays **latest 5 news articles** per feed
- Uses `feedparser` for easy RSS parsing
- **No user input needed** (Predefined RSS sources)
- **Error handling** for broken or missing feeds

---

## 🔧 Installation
### **Step 1: Clone the Repository**
```sh
git clone https://github.com/yourusername/FeedFlow.git
cd FeedFlow
```

### **Step 2: Install Dependencies**
```sh
pip install feedparser requests
```

---

## 🚀 How to Use
Run the script in your terminal:
```sh
python feedflow.py
```

The script will automatically fetch and display news from multiple RSS sources.

---

## 📌 Example Output
```
Fetching RSS Feed: https://rss.nytimes.com/services/xml/rss/nyt/World.xml

🔗 **Feed Title:** The New York Times - World News
📌 **Feed Description:** Latest world news from The New York Times.
--------------------------------------------------
📰 Headline 1: "Russia-Ukraine Conflict Updates"
🔗 https://nytimes.com/article1

📰 Headline 2: "China Economy Growth News"
🔗 https://nytimes.com/article2

...
```

---

## 📜 License
This project is licensed under the **MIT License**.

---

## ⭐ Contribute
Feel free to submit a **pull request** or suggest **new RSS sources**!

---

🔗 **GitHub Repository:** [FeedFlow](https://github.com/umairfarooqi/FeedFlow)
