import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from tqdm import tqdm


linescan=np.loadtxt("line.txt", comments='#', delimiter=";", converters=None, skiprows=1)

tipi=np.loadtxt("tipi.txt", comments='#', delimiter=";", converters=None, skiprows=1)

surf=np.loadtxt("surface.txt", comments='#', delimiter=";", converters=None, skiprows=1)

hexyplo=np.loadtxt("hexagony.txt", comments='#', delimiter=";", converters=None, skiprows=1)




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
ax.set_ylim([0, 100])


#line, = ax.plot(tipi[:,0],tipi[:,1])


def animate(i):
    tipmove(linescan[i], tipi)
    line, = ax.plot(tipi[:,0],tipi[:,1],color='blue',marker='o')
    ax.plot(linescan[:,0],linescan[:,1],color='red')
    ax.plot(surf[:,0],surf[:,1],'g.')
    # ~ ax.plot(hexyplo[:,0],hexyplo[:,1],color='teal') # update the data.
    return line,


ani = animation.FuncAnimation(
    fig, animate,linescan.shape[0], interval=50, blit=True, save_count=0, repeat=True)
    # ~ fig, animate,linescan.shape[0], interval=50, blit=True, save_count=0, repeat=False)

# To save the animation, use e.g.
#
# ~ ani.save("simm1.html")
#
# or
#
# ~ writer = animation.FFMpegWriter(fps=15, metadata=dict(artist='Me'), bitrate=1800)
# ~ ani.save("sim1.mp4", writer=writer)

plt.show()
# ~ ani.save('myAnimation4.html', writer='imagemagick')
