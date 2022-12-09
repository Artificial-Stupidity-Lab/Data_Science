import numpy as np
import matplotlib.pyplot as plt
# Python code
""" result = 0
for i in range(10):
 print(i) """

""" L = list(range(10))
print(L)
L2 = [str(c) for c in L]
print(L2)
L3 = [True, "a", 3.55, 2]
L3 = [type(c) for c in L3]
print(L3) """

''''#creating numpy array
arr = np.array([1,2,3])
print(arr)'''

# Create a 3x5 floating-point array filled with 1s
#np.ones((3, 5), dtype=float)
""" x1 = np.random.randint(200, size=6)
print(x1) """
""" arr1 = np.array([5,2,3,9])
arr1[1]=1
print(arr1) #[5 1 3 9]
arr[-1]=7
print(arr1) #[5 1 3 7] """
""" arr1 = np.array([[8, 6, 9],
                [3, 0, 8],
                [11, 87, 100]])
arr1[1,1] = 11
print(arr1) # second row = [3,11,8] """

""" name = ['Alice', 'Bob', 'Cathy', 'Doug']
age = [25, 45, 37, 19]
weight = [55.0, 85.5, 68.0, 61.5]
data['name'] = name
data['age'] = age
data['weight'] = weight
print(data) """

fig, ax = plt.subplots()
x = np.linspace(0, 20, 1000)
ax.plot(x, np.cos(x))
ax.axis('equal')
ax.annotate('local maximum', xy=(6.28, 1), xytext=(10, 4), arrowprops=dict(facecolor='black', shrink=0.05))
ax.annotate('local minimum', xy=(5 * np.pi, -1), xytext=(2, -6),
arrowprops=dict(arrowstyle="->",
connectionstyle="angle3,angleA=0,angleB=-90"))
plt.show()