from bs4 import BeautifulSoup

def extract_text_from_html(html):
    soup = BeautifulSoup(html, features="html.parser")
    return soup.text
