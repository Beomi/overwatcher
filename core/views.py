# pip modules
import requests
from bs4 import BeautifulSoup


def _get_overwatch_tech(): # Returns List
    with requests.Session() as s:
        http = s.get('http://kr.battle.net/forums/ko/overwatch/4989053/')
        html = BeautifulSoup(http.text, 'html.parser')
        titles = html.select(
            "span.ForumTopic-title"
        )
        board = []
        for title in titles:
            board.append(title.text.strip())

        return board
