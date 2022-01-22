import matplotlib
import matplotlib.pyplot as plt
import numpy as np

linescan=np.loadtxt("line.txt", comments='#', delimiter=";", converters=None, skiprows=1)

linisize=linescan.size
print (linisize)
# Generate data:
N = 500
x = np.linspace(0, 500, N)
y = np.linspace(0, 1, N)
#x, y = np.meshgrid(x, y)
colors = linescan[:,1] # colors for each x,y

#print (linescan.shape)

# Plot
circle_size = 2
cmap = matplotlib.cm.gray # replace with your favourite colormap 
fig, ax = plt.subplots(figsize=(10, 8.4))
for q in range(N):
	# ~ s = ax.scatter(linescan[:,0], linescan[:,2]+q, s=circle_size, c=colors, cmap=cmap)
	s = ax.scatter(x, linescan[:,2]+q, s=circle_size, c=colors, cmap=cmap, marker="s")

# Prettify
ax.axis("tight")
fig.colorbar(s)

plt.xlabel('length x in au')
plt.ylabel("length y in au")
plt.legend()
plt.show()

plt.show()
