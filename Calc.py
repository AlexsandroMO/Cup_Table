import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import numpy as np
import openpyxl

#-- Ler status de jogos
def read_table_status():
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

  return status_list

#-- Ler partidas de jogos
def list_games():
  url = 'https://www.terra.com.br/esportes/futebol/copa-2022/tabela/'
  header = {'user-agent':'Mozilla/5.0'}
  r = requests.get(url, headers = header)
  r.text
  soup = BeautifulSoup(r.text, 'html.parser')

  result = soup.find_all('div',{'class':'match-info'})
  team_all = soup.find_all('span',{'class':'acronym'})
  flags = soup.find_all('img',{'class':'sports-shield'})

  flag_a = []
  for i in range(0, len(flags)):
    if i >= 0 and i < 4:
      flag_a.append([flags[i]['alt'],flags[i]['src']])
    elif i >= 16 and i < 20:
      flag_a.append([flags[i]['alt'],flags[i]['src']])
    elif i >= 32 and i < 36:
      flag_a.append([flags[i]['alt'],flags[i]['src']])
    elif i >= 48 and i < 52:
      flag_a.append([flags[i]['alt'],flags[i]['src']])
    elif i >= 64 and i < 68:
      flag_a.append([flags[i]['alt'],flags[i]['src']])
    elif i >= 80 and i < 84:
      flag_a.append([flags[i]['alt'],flags[i]['src']])
    elif i >= 96 and i < 100:
      flag_a.append([flags[i]['alt'],flags[i]['src']])
    elif i >= 112 and i < 116:
      flag_a.append([flags[i]['alt'],flags[i]['src']])

  flag_b = [
                    ['ALE','Alemanha'],
                    ['ARG','Argentina'],
                    ['AUT','Austrália'],
                    ['BEL','Bélgica'],
                    ['BRA','Brasil'],
                    ['CAN','Canada'],
                    ['CMR','Camarões'],
                    ['CRI','Costa Rica'],
                    ['CRO','Croácia'],
                    ['DEN','Dinamarca'],
                    ['EQU','Equador'],
                    ['ESP','Espanha'],
                    ['EUA','USA'],
                    ['FRA','França'],
                    ['GHA','Gana'],
                    ['ING','Inglaterra'],
                    ['IRA','Irã'],
                    ['JAP','Japão'],
                    ['KOR','Coreia do Sul'],
                    ['MAR','Marrocos'],
                    ['MEX','México'],
                    ['NED','Holanda'],
                    ['PGL','País de Gales'],
                    ['POL','Polônia'],
                    ['POR','Portugal'],
                    ['QAT','Catar'],
                    ['SAU','Arábia Saudita'],
                    ['SER','Sérvia'],
                    ['SNG','Senegal'],
                    ['SWT','Suiça'],
                    ['TUN','Tunísia'],
                    ['URU','Uruguai']
                  ]

  flag_country = []
  for a in range(0, len(flag_a)):
    for b in range(0, len(flag_b)):
      if flag_a[a][0] == flag_b[b][1]:
        flag_country.append([flag_a[a][0],flag_b[b][0],flag_a[a][1]])

  #---------------------
  array = np.array(np.arange(len(team_all)))
  x = np.where(array%2 == 0)
  y = np.where(array%2 == 1)
  team_x, team_y = [],[]
  for a in x:
    for b in a:
      team_x.append(b)

  for a in y:
    for b in a:
      team_y.append(b)

  team_a = []
  for read in team_x:
    team_a.append(team_all[read].text)

  team_b = []
  for read in team_y:
    team_b.append(team_all[read].text)

  #------------
  result_list = []
  increment = 1
  cont_team = 0
  for cont in range(0, len(result)):
    if cont < len(result)/3:
      if result[cont + increment].contents[0].text != '':
        result_list.append([team_a[cont_team],
                          '',
                          result[cont + increment].contents[0].text,
                          result[cont + increment].contents[2].text,
                          '',
                          team_b[cont_team],
                          result[cont + increment].find('div',{'class':'details'}).text[:-14]])
      else:
        result_list.append([team_a[cont_team],
                          '',
                          result[cont + increment].contents[0].text,
                          result[cont + increment].contents[2].text,
                          '',
                          team_b[cont_team],
                          result[cont + increment].find('div',{'class':'details'}).text])
      
      increment += 2
      cont_team += 1

  for a in result_list:
    a[4] = a[4].replace('h00','h00 ')

  for a in range(0, len(result_list)):
    for b in range(0, len(flag_country)):
      if result_list[a][0] == flag_country[b][1]:
        result_list[a][1] = flag_country[b][2]
      if result_list[a][5] == flag_country[b][1]:
        result_list[a][4] = flag_country[b][2]
        
  result_list

  return result_list
