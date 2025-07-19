import requests
from bs4 import BeautifulSoup

def fetch_titles(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    titles = set()

    for tag in soup.find_all('h2'):
        text = tag.get_text(strip=True)
        if text:
            titles.add(text)

    for tag in soup.find_all('title'):
        text = tag.get_text(strip=True)
        if text:
            titles.add(text)

    return list(titles)

def save_titles(titles, filename="headlines.txt"):
    with open(filename, 'w', encoding='utf-8') as file:
        for i, title in enumerate(titles, start=1):
            file.write(f"{i}. {title}\n")
    print(f"[+] Saved {len(titles)} titles to '{filename}'")

if __name__ == "__main__":
    url = "https://www.thehindu.com/"
    print("[*] Fetching titles...")
    titles = fetch_titles(url)
    save_titles(titles)
