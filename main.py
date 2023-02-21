"""
    Description: Scraper les parôles des chansons d'un artiste
    Site: Genius.com
    Artiste: Slaï
    Stack: Request + Beautifulsoup4
"""
import utils.api as api
import pprint

all_lyrics_links = api.get_all_lyrics_urls()
pprint.pprint(all_lyrics_links)