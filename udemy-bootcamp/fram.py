import pandas as pd
import numpy as np
data = { 'a': 1, 'b': 2}
print(pd.Series([1,2,3,45], ['a','b','c','d']))
print(pd.Series(data))
print(pd.DataFrame(np.random.randn(2,4), columns=['a','b','c','d']))
print(pd.DataFrame(np.random.randn(2,4), columns=['a','b','c','d']).drop(['a', 'b'], axis = 1))

df = pd.DataFrame(np.random.randn(2,4), columns=['a','b','c','d'])
print(df)
print(df.loc[0:,'a'])
# postgres://{username}:password@localhost:port/{db}
from sqlalchemy import create_engine
engine = create_engine('postgres://postgres:quininmotion2@localhost:5432/test')
database = pd.read_sql_query('select * from company', con=engine)

print(database)
print(pd.read_csv('cars.csv'))
with pd.ExcelFile('Excel_Sample.xlsx') as x:
    s1 = x.parse('Sheet1')
print(s1)
print(pd.read_excel('Excel_Sample.xlsx', 'Sheet1').isnull())
