import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
# 设置matplotlib正常显示中文和负号
matplotlib.rcParams['font.sans-serif']=['SimHei']   # 用黑体显示中文
matplotlib.rcParams['axes.unicode_minus']=False     # 正常显示负号

#数据读取
filename = './input/user_course.csv'
userCourseFile = pd.read_csv(filename)

#分析2015年哪个月份选课人数最多，画出每月的折线图：
userCourseFile['select_year']=[v[0:4] for v in userCourseFile['select_date']]
userCourseFile['month']=[v[0:7] for v in userCourseFile['select_date']]
hot_month_data=userCourseFile.query("select_year=='2015'")
hot_month=hot_month_data.groupby('month').count().sort_values(by='uid',ascending=False)
hot_month.set_index(pd.to_datetime(hot_month.index))['uid'].plot(label='2015年选课人数')
print(hot_month.set_index(pd.to_datetime(hot_month.index))['uid'])
plt.legend()
plt.show()