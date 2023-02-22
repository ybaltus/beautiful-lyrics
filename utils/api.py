import requests
from bs4 import BeautifulSoup
import collections
import json
import pathlib


CUR_DIR = pathlib.Path.cwd()
PATH_FILE = CUR_DIR / "words.json"

def get_all_lyrics_urls():
    try:
        page_number = 1
        list_urls = []
        while str(page_number).isnumeric():
            # Get response
            r = requests.get(f"https://genius.com/api/artists/453973/songs?page={str(page_number)}&sort=popularity")
            response = r.json().get("response", {})
            # Get next_page value
            page_number = int(response.get("next_page")) if response.get("next_page") else None
            # Loop on the songs
            songs = response.get("songs")
            for song in songs:
                list_urls.append(song.get("url"))

        return list_urls
    except requests.exceptions.ConnectionError:
        print("L'URL n'est pas valide ou est incorrect.")
        return []
    except:
        print("Une erreur est survenue")
        return []


def extract_lyrics(url_lyrics : str, word_length = 2):
    r = requests.get(url_lyrics)
    print(f"Traitement de l'url suivante: {url_lyrics}")

    if r.status_code != 200:
        print('Page impossible à récupérer.')
        return []
    # Create soup object
    page_html_soup = BeautifulSoup(r.text, 'html.parser')

    # Extract the words
    sentences = page_html_soup.find("div", class_="Lyrics__Container-sc-1ynbvzw-6 YYrds")
    lyrics_words = []
    words_to_remove = (
        "refrain",
        "paroles"
        "couplet"
    )
    if sentences:
        for sentence in sentences.stripped_strings:
            sentence_words = [word.strip("[()]\",.").lower() for word in sentence.split() if len(word) > word_length and word.strip("[()]\",.").lower() not in words_to_remove]
            lyrics_words.extend(sentence_words)
   
    return lyrics_words

def get_top_words(words: list, top_count=10):
    # Count and extract the top 10
    counter = collections.Counter(words)
    return counter.most_common(10)

def get_all_words(word_length = 2):
    all_lyrics_urls = get_all_lyrics_urls()
    print("Nombre d'urls = " + str(len(all_lyrics_urls)))
    if len(all_lyrics_urls) > 0:
        all_words = []
        for lyrics_url in all_lyrics_urls:
            lyrics = extract_lyrics(lyrics_url, word_length)
            all_words.extend(lyrics)
        return all_words
    else:
        return []

def save_in_json_file(words: list):
    with open(PATH_FILE, 'w') as f:
        json.dump(words, f, indent=2)
        
