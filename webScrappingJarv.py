import requests
from bs4 import BeautifulSoup

url = "https://www.youtube.com/watch?v=XzZJN2IlsZg&ab_channel=PabloAlbor%C3%A1n"
response = requests.get(url)

html_content = response.text

#parso l'html se no se spezza come l'altro caso
soup = BeautifulSoup(html_content, "html.parser")

#lista di parole da cercare nel sito
search_words = ["La mudanza"]

#me ciclo la lista di parole da trovare
for word in search_words:
    if soup.find(string=lambda string: string and word in string):
        print(f"a parola '{word}' ce sta!")
    else:
        print(f"a parola '{word}' nun ce sta.")