import matplotlib.pyplot as plt

input_values = [i for i in range(1,6)]
squares = [i**2 for i in range (1,6)]
plt.style.use("seaborn")
fig, ax = plt.subplots()
#ax.plot(input_values, squares, linewidth=3)
ax.scatter(input_values, squares)
ax.set_title("Squares", fontsize = 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square values", fontsize = 14)
ax.tick_params(labelsize = 12)

plt.show()