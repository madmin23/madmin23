import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from tqdm import tqdm


linescan=np.loadtxt("line.txt", comments='#', delimiter=";", converters=None, skiprows=1)

tipi=np.loadtxt("tipi.txt", comments='#', delimiter=";", converters=None, skiprows=1)

surf=np.loadtxt("surface.txt", comments='#', delimiter=";", converters=None, skiprows=1)

hexyplo=np.loadtxt("hexagony.txt", comments='#', delimiter=";", converters=None, skiprows=1)

loopi=500

moveee=[tipi]

def tipmove(tipnow, tipdd):
	j=0
	truemove=[0,0,0]
	tipdds=tipdd.shape
	truemove=tipnow-tipdd[0]
	for j in range(tipdds[0]):
		#print ("now", tipnow)
		tipdd[j]=tipdd[j]+truemove




fig, ax = plt.subplots()

ax.set_xlim([200, 600])
ax.set_ylim([0, 200])


#line, = ax.plot(tipi[:,0],tipi[:,1])

ax.plot(linescan[:,0],linescan[:,1],color='red')
ax.plot(surf[:,0],surf[:,1],color='green')
ax.plot(hexyplo[:,0],hexyplo[:,1],color='pink')

def animate(i):
	# ~ ax.cla()
	# ~ ax.set_xlim([200, 600])
	# ~ ax.set_ylim([0, 200])
	# ~ tipmove(linescan[i], tipi)
	# ~ line, = ax.plot(tipi[:,0],tipi[:,1],color='blue')
	# ~ ax.plot(moveee[i-1,:,0],moveee[i-1,:,1],color='white')
	line = ax.plot(moveee[i,:,0],moveee[i,:,1],color='blue')
	ax.plot(linescan[:,0],linescan[:,1],color='red')
	# ~ ax.plot(surf[:,0],surf[:,1],color='green')
	# ~ ax.plot(hexyplo[:,0],hexyplo[:,1],color='pink') # update the data.
	return line


for g in range(loopi):
	tipmove(linescan[g], tipi)
	moveee=np.append(moveee,[tipi],axis=0)
	print (g)

	

ani = animation.FuncAnimation(
    fig, animate,loopi, interval=5, blit=True, save_count=500, repeat=False)

# To save the animation, use e.g.
#
# ~ ani.save("simm1.html")
#
# or
#
# ~ writer = animation.FFMpegWriter(fps=15, metadata=dict(artist='Me'), bitrate=1800)
# ~ ani.save("sim1.mp4", writer=writer)

plt.show()
ani.save('myAnimation4.gif', writer='imagemagick')
# ~ ani.save('myAnimation4.mp4', writer=writer)
