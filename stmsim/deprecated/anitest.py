import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


linescan=np.loadtxt("line.txt", comments='#', delimiter=";", converters=None, skiprows=1)

tipi=np.loadtxt("tipi.txt", comments='#', delimiter=";", converters=None, skiprows=1)


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


def animate(i):
    tipmove(linescan[i], tipi)
    line, = ax.plot(tipi[:,0],tipi[:,1])
    ax.plot(linescan[:,0],linescan[:,1]) # update the data.
    return line,


ani = animation.FuncAnimation(
    fig, animate,500, interval=5, blit=True, save_count=500)

# To save the animation, use e.g.
#
# ~ ani.save("simm1.html")
#
# or
#
# ~ writer = animation.FFMpegWriter(fps=15, metadata=dict(artist='Me'), bitrate=1800)
# ~ ani.save("sim1.mp4", writer=writer)

plt.show()
