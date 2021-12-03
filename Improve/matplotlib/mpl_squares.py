import matplotlib.pyplot as plt

input_values = [1,2,3,4,5]
squ1 = [1,4,9,16,25]
squ2 = [1,8,27,64,125]

plt.plot(input_values,squ1,color = 'green',input_values,squ2,color = 'black')   #绘制折线图，设置线条粗细
plt.title("Square Number",fontsize = 24)   #图表标题
plt.xlabel("Value",fontsize = 14)   #图标x轴
plt.ylabel("Square of Value",fontsize = 14)   #图表y轴
plt.tick_params(axis='both',labelsize = 14)   #设置坐标轴刻度标记

plt.show()   #打开查看器并显示绘制的图形
