import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

# 设置matplotlib正常显示中文和负号
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 用黑体显示中文
matplotlib.rcParams['axes.unicode_minus'] = False  # 正常显示负号

filename = './input/user_course.csv'
userCourseFile = pd.read_csv(filename)
course_hot10 = userCourseFile.groupby('course_id')['course_id'].count().sort_values()
plt.bar(x=range(course_hot10.shape[0]), height=list(course_hot10),
        width=0.4, alpha=0.8, label="选课人数")
plt.xticks([index + 0.01 for index in range(course_hot10.shape[0])], course_hot10.index)
plt.xlabel('课程id',size=12)
plt.ylabel('人数',size=12)
plt.legend()
plt.show()
