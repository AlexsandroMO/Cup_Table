from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import Calc as CL


def Index(request):

    return render(request,'tableCup/index.html')


def TableTeam(request):

    read_table = CL.read_table_status()

    tabela = []
    for a in range(0, len(read_table['POS'])):
        tabela.append([read_table['POS'].loc[a],read_table['Time'].loc[a],read_table['PTS'].loc[a],read_table['J'].loc[a],read_table['V'].loc[a],read_table['E'].loc[a], read_table['D'].loc[a],read_table['GP'].loc[a],read_table['GC'].loc[a],read_table['SG'].loc[a],read_table['percento'].loc[a],read_table['Recentes'].loc[a]])

    print(tabela)

    return render(request,'tableCup/table-teams.html', {'tabela':tabela})


def Result(request):
    read_table = CL.read_teams()
    read_game = CL.read_table_games()
    
    tabela = []
    for a in range(0, len(read_table['BANDEIRA'])):
        tabela.append([read_table['BANDEIRA'].loc[a],read_table['PAIS'].loc[a]])
        print([read_table['BANDEIRA'].loc[a],read_table['PAIS'].loc[a]])

    tabela_game = []
    for a in range(0, len(read_game['TIME_L'])):
        tabela.append([read_game['TIME_L'].loc[a],read_game['RESULT'].loc[a],read_game['TIME_F'].loc[a],read_game['DATA'].loc[a],read_game['LOCAL'].loc[a]])
        print([read_game['TIME_L'].loc[a],read_game['RESULT'].loc[a],read_game['TIME_F'].loc[a],read_game['DATA'].loc[a],read_game['LOCAL'].loc[a]])

    return render(request,'tableCup/result.html', {'tabela':tabela, 'tabela_game':tabela_game})