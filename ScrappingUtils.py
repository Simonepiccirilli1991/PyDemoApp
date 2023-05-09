import requests
from bs4 import BeautifulSoup


def web_scrapping(sito: str, parola: str) -> str:
    """Get info on some item for website.

      Keyword arguments:
      sito:str - Site to make a search
      parola:str - word to find in site
      Return:dict - JSON data
      """
    print(sito)
    url = sito

    print(url)
    print(parola)
    response = requests.get(url)
    html_content = response.text

    # parso l'html se no se spezza come l'altro caso
    soup = BeautifulSoup(html_content, "html.parser")

    search_words = [parola]

    for word in search_words:
        if soup.find(string=lambda string: string and word in string):
            return(f"a parola '{word}' ce sta!")
        else:
            return(f"a parola '{search_words}' nun ce sta.")