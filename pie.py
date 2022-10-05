from matplotlib import pyplot as plt
k={'Shashi':314,'Pranav':400,'Niroop':430,'Mittu':245}
l=list(k.keys())
m=list(k.values())
plt.figure(figsize=(30,30))
plt.pie(m,labels=l,autopct='%0.0f%%',shadow='true')
plt.show()
