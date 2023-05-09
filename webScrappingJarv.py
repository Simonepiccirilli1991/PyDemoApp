import requests
from bs4 import BeautifulSoup

url = "https://www.youtube.com/watch?v=oAwKuYcAg-A&list=RDMM&index=4&ab_channel=AlejandroSanzVEVO"
response = requests.get(url)
print(url)
html_content = response.text

#parso l'html se no se spezza come l'altro caso
soup = BeautifulSoup(html_content, "html.parser")

print(soup)
#lista di parole da cercare nel sito
search_words = ["Correcaminos"]

#me ciclo la lista di parole da trovare
for word in search_words:
    if soup.find(string=lambda string: string and word in string):
        print(f"a parola '{word}' ce sta!")
    else:
        print(f"a parola '{word}' nun ce sta.")