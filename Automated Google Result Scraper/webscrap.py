import requests
from bs4 import BeautifulSoup
import urllib.parse

def google_search(query, num_results=10):
    base_url = "https://www.google.com/search"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
    }

    params = {
        "q": query,
        "num": num_results
    }

    response = requests.get(base_url, headers=headers, params=params)

    if response.status_code != 200:
        print("Failed to retrieve results")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    results = []

    for item in soup.select('.tF2Cxc'):  # Updated class name for results
        title = item.select_one('h3')
        link = item.select_one('a')
        description = item.select_one('.VwiC3b')

        if title and link and description:
            results.append({
                "title": title.get_text(),
                "link": link['href'],
                "description": description.get_text()
            })

    if not results:
        print("No results found")

    return results

# Example usage
print("Enter your query: ")
query = input()
results = google_search(query, num_results=10)

for idx, result in enumerate(results, start=1):
    print(f"{idx}. {result['title']}")
    print(f"Link: {result['link']}")
    print(f"Description: {result['description']}\n")