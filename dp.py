import pandas as pd
data = {
    '이름':['승현','지우','수경','아진'],
    '나이':[26,26,25,24]
    ,'성별':['남','여','여','여']
}

df=pd.DataFrame(data,index=['A','B','C','D'])

print(df)
# df.to_csv('./2조.csv')
