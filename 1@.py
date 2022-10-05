from matplotlib import pyplot as plt
import numpy as np
x=np.arange(1,10)
y=x*2
print(plt.plot(x,y))
plt.title('graph representation')
plt.xlabel('numbers')
plt.ylabel('product')
print(plt.show())
