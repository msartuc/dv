import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]
fig, ax = plt.subplots()
ax.plot(squares, linewidth=3)
ax.set_title("Squares", fontsize = 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square values", fontsize = 14)
ax.tick_params(labelsize = 24)

plt.show()