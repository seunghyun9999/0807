import pandas as pd
import matplotlib.pyplot as plt
cnames = ['preg','plas','pres','skin','test','mass','pedi','age','class']
data = pd.read_csv('./pima-indians-diabetes.data.csv',
                   names=cnames)
# ./ = 지금 실행 되고 있는 파이 파일의 위치까지를 불러오는것
#  따라서 그보다 안쪽의 파일을 불러올려면 ./data/pima-indians-diabetes.data.csv 라는식으로 써야함
# ./를 사용하세요 다른 컴퓨터에서 오작동 가능성 높음
# print(data.head(5))
# print(data.describe())

plt.clf()
plt.hist(data['age'])
plt.show()
data.describe().to_csv('./results/describe.csv')
