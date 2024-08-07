import numpy as np
import pandas as pd

ind = ['A','B','C']
col=['이름','나이','성별']
data = np.array([['Al','Bo','hg']
                    ,[26,30,24]
                    ,['남','여','여']
                    ]).transpose()
df = pd.DataFrame(data,index=ind,columns=col)
# print(df,df.shape)
# print(df[['나이','이름']])
print(df.loc['A'])