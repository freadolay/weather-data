import time
import requests
from .helpers import weeks_lkp

class Scraper():
    def __init__(self):
        pass

    def get_with_requests(self, url):
        html_source = requests.get(url).text
        time.sleep(2)  # Add 2 second delay to not overload server
        return html_source

class NflwScraper(Scraper):
    def __init__(self):
        super().__init__()
        self.base_url = 'http//www.nflweather.com'

    def get_games(self, seasons, weeks, game_limit=None):
        if type(seasons) == int:
            seasons = [seasons]
        for season in seasons:
            week_nums, week_labels, week_hrefs = weeks_lkp(season)
            for i in range(min(len(week_nums))):
                continue