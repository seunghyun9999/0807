import pandas as pd
import numpy as np

data = pd.Series([10,20,30,40,50], index=['A','B',"C","D","E"])
data['B']=60
print(data)


