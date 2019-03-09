from matplotlib import pyplot as plt

x_value = list(range(5001))
cubes = [x**3 for x in x_value]

#plt.plot(x_value, y_value, edgecolor='none', c=y_value, cmap=plt.cm.summer)
plt.scatter(x_value, cubes, edgecolor='none', c=cubes, cmap=plt.cm.ocean, s=40)

plt.title("Cubes", fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Cube of Value', fontsize=14)
plt.tick_params(axis='both', labelsize=14)
plt.axis([0, 5100, 0, 5100**3])

plt.show()
