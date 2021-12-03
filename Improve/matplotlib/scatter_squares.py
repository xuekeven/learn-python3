import matplotlib.pyplot as plt

x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,edgecolors=None,s = 40)   #绘制散点图，设置点

plt.axis([0,1100,0,1100000])   #设置坐标轴取值范围

plt.title("Square Numbers",fontsize = 24)
plt.xlabel("Value",fontsize = 14)
plt.ylabel("Square of Value",fontsize = 14)
plt.tick_params(axis='both',which = 'major',labelsize = 14)

plt.savefig('squares_plot.png',bbox_inches = 'tight')   #保存图表默认到本文件下，并裁剪空白区
plt.show()