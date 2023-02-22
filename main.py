"""
    Description: Scraper les parôles des chansons d'un artiste
    Site: Genius.com
    Artiste: Slaï
    Stack: Request + Beautifulsoup4
"""
import utils.api as api
import pprint

# Get the words for all songs
all_words = api.get_all_words(5)
# Save in json file
api.save_in_json_file(all_words)
# Extract the top 10
top_10_words = api.get_top_words(all_words, 10)
pprint.pprint(top_10_words)
