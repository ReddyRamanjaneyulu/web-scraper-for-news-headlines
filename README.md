#  Web Scraper for News Headlines

This Python script scrapes the top headlines from a public news website using `requests` and `BeautifulSoup`, and saves them to a `.txt` file.

##  Features

- Fetches live HTML content using `requests`
- Parses `<h2>` and `<title>` tags with `BeautifulSoup`
- Saves headlines to a clean, numbered `.txt` file
- Easy to modify for other sites or tags

##  Requirements

- Python 3.6+
- Install dependencies:

```bash
pip install requests beautifulsoup4

## FILES
scrape headlines.py - Main Python script

headlines.txt - Output file with scraped headlines

## Usage
bash
Copy
Edit
python scrape_headlines.py
The script will:

Scrape headlines from (https://www.thehindu.com/)

Save them to headlines.txt in the same folder

## Legal Note
This scraper is intended for educational purposes. Always check the website’s robots.txt and terms of service before scraping.

## License
MIT License – Free to use and modify
