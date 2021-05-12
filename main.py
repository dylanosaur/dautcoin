import requests
import json
from Models import Game


def main():
    url = 'https://aoe2.net/api/matches'
    data = requests.get(url, params={'game':'aoe2de', 'count':10, 'since':1620693540})
    myArray = json.loads(data.text)
    games = []
    for game in myArray:
        print(game)
        myGame = Game(game)
        print(myGame)
        games.append(myGame)
    return games

if __name__ == '__main__':
    main()