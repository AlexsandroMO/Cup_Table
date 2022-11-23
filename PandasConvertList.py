import numpy as np

def change_in_list(df):
  #Status Test
  status = False
  for a in df.columns:
    print(a)
    if a == 'Unnamed: 0':
      status = True

  if status == True:
    df = df.drop(columns=['Unnamed: 0'])

  x = np.array(range(len(df.columns)))

  list_all = []
  for a in range(0, len(df[df.columns[0]])):
    list_read = []
    for b in x:
      list_read.append(df[df.columns[b]].loc[a])
    list_all.append(list_read)
  return list_all