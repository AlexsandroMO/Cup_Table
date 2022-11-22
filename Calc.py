import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import numpy as np

#-- Ler times
def read_teams():
  df = pd.read_csv('media/TEAMS.csv')
  return df

#-- Ler status de jogos
def read_table_status():
  df = pd.read_csv('media/STATUS.csv')
  return df

#-- Ler status tabela de jogos
def read_table_games():
  df = pd.read_csv('media/TABLE_GAME.csv')
  print(df)
  
  return df

#-- Ler status de jogos
def rotine_status():
  url = 'https://www.api-futebol.com.br/campeonato/copa-do-mundo/Catar%202022'
  header = {'user-agent':'Mozilla/5.0'}
  r = requests.get(url, headers = header)
  r.text
  soup = BeautifulSoup(r.text, 'html.parser')
  read_status = soup.find_all('table',{'class':'table table-bordered table-striped mb-4'})
  recent = soup.find_all('span',{'data-toggle':'tooltip'})
  
  recent_list = []
  for a in recent:
    recent_list.append(a['title'])

  status_list = []
  cont_list = [3,5,7,9]
  cont_recent = 0
  for read_cont in range(0, 8):
    for cont in cont_list:
      read_all = read_status[read_cont].contents[cont].text
      data_read = read_all.split('\n')
      del(data_read[0])
      if cont_recent >= len(recent_list) -1:
        data_read[11] = '-'
        status_list.append(data_read[:-2])
      else:
        data_read[11] = recent_list[cont_recent]
        status_list.append(data_read[:-3])
      cont_recent += 1
  
  df = pd.DataFrame(data=status_list, columns=['POS',
  'Time',
  'PTS',
  'J',
  'V',
  'E',
  'D',
  'GP',
  'GC',
  'SG',
  'percento',
  'Recentes',
  'xx'])

  df.drop(columns=['xx'], inplace=True)

  df.to_csv('media/STATUS.csv')


def list_games():
  url = 'https://www.api-futebol.com.br/campeonato/copa-do-mundo/Catar%202022'
  header = {'user-agent':'Mozilla/5.0'}
  r = requests.get(url, headers = header)
  r.text
  soup = BeautifulSoup(r.text, 'html.parser')
 
  result = soup.find_all('div',{'class':'small text-center'})
  team_right = soup.find_all('div',{'class':'text-right'})
  team_left = soup.find_all('div',{'class':'text-left'})
  time_game = soup.find_all('small',{'class':'smaller'})

  result_list = []
  for a in result:
    result_list.append(a.text)

  right_list = []
  for a in team_right:
    right_list.append(a.text)

  del(right_list[0])
  right_list

  left_list = []
  for a in team_left:
    left_list.append(a.text)

  time_list = []
  for a in time_game:
    time_list.append(a.text)

  array = np.array(np.arange(len(time_list)))
  x = np.where(array%2 == 0)
  y = np.where(array%2 == 1)
  cont_time_x, cont_time_y = [],[]
  for a in x:
    for b in a:
      cont_time_x.append(b)

  for a in y:
    for b in a:
      cont_time_y.append(b)

  time_x = []
  for a in cont_time_x:
    time_x.append(time_list[a])

  time_y = []
  for a in cont_time_y:
    time_y.append(time_list[a])

  games_list = []
  for result, left, right, t_x, t_y in zip(result_list, left_list, right_list, time_x,time_y):
    games_list.append([right, result, left, t_x, t_y])

  df = pd.DataFrame(data=games_list, columns=['TIME_L', 'RESULT', 'TIME_F','DATA','LOCAL'])
  
  df.to_csv('media/TABLE_GAME.csv')

#rotine_status()
#list_games()

