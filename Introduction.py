import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

# Function to search The Hacker News
def search_hacker_news(query):
    url = f'https://www.bing.com/search?q=site:https://thehackernews.com/search/label/data%20breach+{query}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        results = soup.find_all('li', class_='b_algo')
        incidents = []
        for result in results:
            title = result.find('h2').get_text()
            link = result.find('a')['href']
            incidents.append({'title': title, 'link': link})
        return incidents
    else:
        print(f'Failed to retrieve search results. Status code: {response.status_code}')
        return []

# Search for cyber incidents
query = 'India'
incidents = search_hacker_news(query)

# Print the results
if incidents:
    for incident in incidents:
        print(f"Title: {incident['title']}")
        print(f"Link: {incident['link']}\n")

    # Visualize the data
    titles = [incident['title'] for incident in incidents]
    plt.figure(figsize=(10, 5))
    plt.barh(titles, range(len(titles)))
    plt.xlabel('Number of Incidents')
    plt.ylabel('Incident Titles')
    plt.title('Cyber Incidents from The Hacker News')
    plt.show()
else:
    print("No incidents found.")
