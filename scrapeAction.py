import requests
from bs4 import BeautifulSoup


headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }


url = "https://www.actionnetwork.com/nfl/public-betting"
req = requests.get(url, headers)
soup = BeautifulSoup(req.content, 'html.parser')
num = 0
for tr in soup.find('tbody').find_all("tr"):
    # is part of formatting
    if tr.has_attr('class'):
        continue
    else:
    # find the teams
        # each rows columns
        tds = tr.find_all('td')
        teams = tds[0]
        open = tds[1]
        best_odds = tds[2]
        percent_of_bets = tds[3]
        percent_of_money = tds[4]
        diff = tds[5]
        num_bets = tds[6]
        print(teams.get_text(),open.get_text(),best_odds.get_text(),percent_of_bets.get_text(),percent_of_money.get_text())
        # teams = tr.find_all('div',class_="game-info__team--desktop")
        # betting_percent = tr.find_all('div',class_="public-betting__percent-and-bar")
        # money_percent= tr.find_all('span',class_=["public-betting__percent custom-q2y3yl e1h8ku180"])
        # print(money_percent[3].get_text())
        # # print(len(money_percent))
        # for idx, team in enumerate(teams):
        #     team_name = team.get_text()
        #     bet_percent = betting_percent[idx].get_text()[len("Right Arrow"):]
            
            # try:
            #     in_money = money_percent[idx].get.text()
            # except:
            #     in_money= 0
            # print(team_name,bet_percent,in_money)
        num= num+1

print(num)
# public = 'public-betting__percents-container'
# bets = soup.find_all('div',public)
# team_ref = 'game-info__team--desktop'
# teams = soup.find_all('div',team_ref)
# # for team in teams:
# #     print(team.get_text())
# for idx, val in enumerate(bets):
#     print(val.get_text())
#     print(teams[idx].get_text())
# print((bets.get_text()))

