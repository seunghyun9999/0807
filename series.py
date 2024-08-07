import pandas as pd
import  numpy as np

index = np.array([1,2,3])
data =['길동','관훈','우진']

series = pd.Series(data,index=index)

data2 =[10,20,30,40,50]
series2=pd.Series(data2)
print(series2)