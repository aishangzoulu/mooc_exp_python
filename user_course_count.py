import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
# 设置matplotlib正常显示中文和负号
matplotlib.rcParams['font.sans-serif']=['SimHei']   # 用黑体显示中文
matplotlib.rcParams['axes.unicode_minus']=False     # 正常显示负号

filename = './input/user_course.csv'
userCourseFile = pd.read_csv(filename)
data = userCourseFile.groupby('uid')['uid'].count()
plt.hist(data, bins=5)
plt.title('选课数分布直方图',size=14)
plt.xlabel('选课频数区间',size=12)
plt.ylabel('人数',size=12)
plt.show()