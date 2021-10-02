import requests
from bs4 import BeautifulSoup
import psycopg2
import os
from dotenv import load_dotenv
from decimal import Decimal
import datetime
from pytz import timezone


load_dotenv()

conn = psycopg2.connect(
        host=os.getenv('host'),
        database=os.getenv('database'),
        user=os.getenv('user')
        )   
cur = conn.cursor()



# headers = {
#     'Access-Control-Allow-Origin': '*',
#     'Access-Control-Allow-Methods': 'GET',
#     'Access-Control-Allow-Headers': 'Content-Type',
#     'Access-Control-Max-Age': '3600',
#     'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
#     }


url = "https://www.actionnetwork.com/nfl/public-betting"
req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')
for tr in soup.find('tbody').find_all("tr"):
    # is part of formatting
    if tr.has_attr('class'):
        continue
    else:
    # find the teams
        # each rows columns
        tds = tr.find_all('td')
        teams = tds[0]
        status = teams.find('div','public-betting__game-status').get_text().strip()
        if status!='Final':
            date_object = datetime.datetime.strptime(status, "%a %m/%d, %I:%M %p")
            if datetime.datetime.now().month > date_object.month:
                new_year=date_object.replace(year=(datetime.datetime.now().year + 1)) + datetime.timedelta(hours=-5)
            else:
                new_year=date_object.replace(year=datetime.datetime.now().year) + datetime.timedelta(hours=-5)
            string_object_status = datetime.datetime.strftime(new_year,"%a %m/%d, %I:%M %p")
        else:
            string_object_status='Final'
        team_names = teams.find_all('div','game-info__team--desktop')
        team_1_name = team_names[0].get_text()
        team_2_name = team_names[1].get_text()
        game_id = team_1_name + '-' + team_2_name + '-' + status
        # team 2 is home
        team_1_away='Away'
        team_2_home='Home'
        opens = tds[1].find_all('div','public-betting__open-cell')
        team_1_open = Decimal(opens[0].get_text())
        team_2_open = Decimal(opens[1].get_text())
        best_odds = tds[2].find_all('div','custom-5d751z ena22470')
        team_1_best_odds = Decimal(best_odds[0].find_all('span','highlight-text__children')[0].get_text())
        team_1_juice = Decimal(best_odds[0].find_all('span','highlight-text__children')[1].get_text())
        team_2_best_odds = Decimal(best_odds[1].find_all('span','highlight-text__children')[0].get_text())
        team_2_juice = Decimal(best_odds[1].find_all('span','highlight-text__children')[1].get_text())
        percent_of_bets = tds[3].find_all('span','highlight-text__children')
        team_1_percent_of_bet = Decimal(percent_of_bets[0].get_text().rstrip('%'))
        team_2_percent_of_bet = Decimal(percent_of_bets[1].get_text().rstrip('%'))
        percent_of_money = tds[4].find_all('span','highlight-text__children')
        if len(percent_of_money)>0:
            team_1_percent_of_money = Decimal(percent_of_money[0].get_text().rstrip('%'))
            team_2_percent_of_money = Decimal(percent_of_money[1].get_text().rstrip('%'))
        else:
            team_1_percent_of_money = None
            team_2_percent_of_money = None 
        num_bets_pull = tds[6].find('div','public-betting__number-of-bets').get_text().replace(',','')
        try:
            float(num_bets)
            num_bets = int(float(num_bets_pull))
        except:
            num_bets=-1
        tz = timezone('EST')
        now = datetime.datetime.now(tz)
        sql = 'INSERT INTO nfl VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);' 
        try:
        
            cur.execute(sql, (
            string_object_status
            ,team_1_name
            ,team_1_open 
            ,team_1_best_odds
            ,team_1_juice 
            ,team_1_percent_of_bet
            ,team_1_percent_of_money
            ,num_bets
            ,now
            ,'Away'
            ,game_id))
            conn.commit()

            cur.execute(sql, (
            string_object_status
            ,team_2_name
            ,team_2_open 
            ,team_2_best_odds
            ,team_2_juice 
            ,team_2_percent_of_bet
            ,team_2_percent_of_money
            ,num_bets
            ,now
            ,'Home'
            ,game_id))
            conn.commit()


        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        
        
cur.close()
conn.close()

        

# rows = cur.fetchall()
# print(rows)


# conn.close()
        
        
        
        
        
        


