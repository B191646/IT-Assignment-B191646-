
from matplotlib import pyplot as plt
d1={'pranav':8.81,'shashi':8.32,'Niroop':9.8}
student=list(d1.keys())
marks=list(d1.values())
plt.bar(student,marks)
print(plt.show())
