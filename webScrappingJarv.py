import requests
from bs4 import BeautifulSoup

url = "https://it.wikipedia.org/wiki/Guerra_di_Crimea"
response = requests.get(url)
html_content = response.text

#parso l'html se no se spezza come l'altro caso
soup = BeautifulSoup(html_content, "html.parser")

#lista di parole da cercare nel sito
search_words = ["Omar Pascià"]

#me ciclo la lista di parole da trovare
for word in search_words:
    if soup.find(string=lambda string: string and word in string):
        print(f"The word '{word}' was found on the web page!")
    else:
        print(f"The word '{word}' was not found on the web page.")