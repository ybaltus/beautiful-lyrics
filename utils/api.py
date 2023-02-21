import requests

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
        return
    except:
        print("Une erreur est survenue")
        return


def extract_lyrics(url_lyrics : str):
    print("OK")