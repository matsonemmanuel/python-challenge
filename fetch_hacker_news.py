import requests
import csv

def fetch_hacker_news_data():
    # Get top stories from Hacker News
    response = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty')
    top_stories_ids = response.json()

    # Retrieve details of the top stories
    top_stories_data = []
    for story_id in top_stories_ids[:10]:  # Get the top 10 stories
        story_details = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{story_id}.json?print=pretty').json()
        title = story_details.get('title', 'No title')
        url = story_details.get('url', 'No URL')
        top_stories_data.append([title, url])

    # Save the data in CSV format
    with open('hacker_news_data.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'URL'])  # Header row
        writer.writerows(top_stories_data)

    print("CSV file created successfully!")

if __name__ == '__main__':
    fetch_hacker_news_data()