lista_a = [11,22,33,44,55]
lista_b = ['a','b','c','d','e']

import pandas as pd

serie_1 = pd.Series(lista_a)
print(serie_1)

serie_1 = pd.Series(lista_b, index=lista_a)
print(serie_1)

import numpy as np

arr = np.arange(10)**2

dic={'a':123,'b':456, 'c':789}

serie_3 = pd.Series(arr)
print(serie_3)

serie_4 = pd.Series(dic)
print(serie_4)
print(serie_4['a'])

dic2 = {'coluna': np.arange(10)*5, 'coluna2': np.arange(10)**2, 'coluna3':np.ones(10)}
print(dic2)

df1 = pd.DataFrame(dic2)
print(df1)
df1

arr2 = np.arange(15).reshape(5,3)

df2 = pd.DataFrame(arr2)

df2

lista_a = ['a','b','c','d','e','f','g']
lista_b = list(range(7))

dic = {'string':lista_a,'numeros':lista_b}

df = pd.DataFrame(dic)
df

list(df.columns)

import numpy as np

df2 = pd.DataFrame({'col1':np.arange(100)**2, 'col2':np.ones(100)})
df2

df2.head(10)

df2.tail(10)

df2.mean()

df2.min()

df2.cumsum()

df['string'].value_counts()

df.sort_values(by='string')

df2.columns

df2.loc[1:4,['col1']]

df.iloc[1:4,::]

dfa = pd.DataFrame(np.arange(15).reshape(5,3))
dfb = pd.DataFrame((np.arange(9)**2).reshape(3,3))

pd.concat([dfa,dfb],ignore_index=True)

dfCor = pd.DataFrame({'id':[1,2,3],
                      'cor':['branco','preto','vasco da gama']})
dfTime = pd.DataFrame({'times':['time1','time2','time3','time4','gigante da colina'],
                       'id_cor':[1,1,2,1,3]})

pd.merge(dfCor,dfTime,left_on='id',right_on='id_cor')

par = df2['col1']%2==0
df2[par]

pd.pivot_table(df2,index=par,values='col2',aggfunc='sum')

import numpy as np

numeros = np.random.randint(1,10, size=40)

serie_1 = pd.Series(numeros)

serie_1.plot.bar()

df1.plot(x='c',y=['a','b'])

df1 = pd.DataFrame({'a':np.arange(50)**2,
                    'b':np.arange(50)*3,
                    'c':np.arange(50)*5})
df1.plot()

serie_1 = pd.Series(arr.cumsum())
serie_1.plot()

df1.plot(x='c',y=['a','b'])

import numpy as np

numeros = np.random.randint(1,10, size=40)

serie_1 = pd.Series(numeros)

serie_1.plot.bar()

serie_1.plot.pie(subplots=True)

a_arr = np.arange(20).reshape(4,5)

df_columns = ['a','b','c','d','e']
df = pd.DataFrame(a_arr,columns=df_columns)

df.drop(index=2)

df.drop(columns='c', index=[0,2])

b_arr = np.vstack([a_arr, np.array([np.nan,np.nan,np.nan,np.nan,np.nan]),np.array([np.nan,np.nan,np.nan,np.nan,np.nan])])
dfb = pd.DataFrame(b_arr,columns=df_columns)
dfb.isnull()

dfb['a'].notnull()

dfb.dropna()

dfb.fillna(value=1)

dfb.duplicated(keep='last')

import numpy as np
import pandas as pd

arrA = np.arange(20).reshape(5,4)

dfA = pd.DataFrame(arrA)
list(dfA.index)

dfA

aTupla = [('A',0),('A',1),('A',2),('B',3),('B',4)]
aIndex = pd.MultiIndex.from_tuples(aTupla)
type(aIndex)

dfA2 = pd.DataFrame(arrA, index = aIndex)
dfA2

