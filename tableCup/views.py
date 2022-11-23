from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import pandas as pd
import Calc as CL
import PandasConvertList as PCL

def Index(request):

    return render(request,'tableCup/index.html')


def TableTeam(request):

    read_table = CL.read_table_status()

    # df = pd.read_csv('media/TABLE_GAME.csv')
    # tabela = PCL.change_in_list(df)
    # print(tabela)

    return render(request,'tableCup/table-teams.html', {'read_table':read_table})


def Result(request):
    read_table = CL.list_games()

    return render(request,'tableCup/result.html', {'read_table':read_table})