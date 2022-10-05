from matplotlib import pyplot as plt
x=[1,5,7,7,9,4]
y1=[5,3,7,2,8,6]
y2=[3,7,6,9,2,6]
plt.scatter(x,y1)
plt.scatter(x,y2,color='r')
plt.grid('true')
plt.show()