import numpy as np

tipinit=np.array([90,2.477,0]) #initial tip position

#current-parameters
voltset=4.0	#set-Voltage
ampset=.5	#set-Current
intetset=30  #integrationtime

#image parameters
pixies=80 # number of measurements
lengthi=40.0	# spacing of pixels
tppx=5 #time per pixel


#curr=(volts/amps)*scalar 

#print (curr)

surf=np.loadtxt("surface.txt", comments='#', delimiter=";", converters=None, skiprows=1)

tipdd=np.loadtxt("tipi.txt", comments='#', delimiter=";", converters=None, skiprows=1)

#print(surf)


def tipmove(tipnow, tipdd):
	j=0
	tipdds=tipdd.shape
	for j in range(tipdds[0]):
		tipdd[j]=tipdd[j]+tipnow
	print tipdd

def hmeassure(tip, surf, tipdd, volts, amps, intet, tppx):
	i=0
	tipscalar=.1 # limits tip movement 0.001
	tipadjust=1
	count=0

	surfs=surf.shape

	#print (surfs[0])
	#print (surf[i])
	
	#while abs(tipadjust)>0.0001:
	while count <= tppx:
		alltunc=0
		for tt in range(intet):
			tunc=0
			for i in range(surfs[0]):
				k=surf[i]-tip

				#print("k ",k)

				dis=np.sqrt((k[0]**2)+(k[1]**2))
				#print ("dis ",dis)

				#poni=volts*np.exp(-(dis/surf[i,2]))
				poni=volts*np.exp(-(1*dis/surf[i,2]))
				#print ("poni ",poni)

				rando=np.random.random_sample()

				#print ("rando ",rando)
				if poni>=rando:
					tunc = tunc + poni

			#print ("tunc ",tunc)
			alltunc= alltunc + tunc

		#print ("alltunc",alltunc)
		alltunc=alltunc/intet
		#print alltunc
		tipadjust=tipscalar*(alltunc-amps)
		tip = tip + [0.0,tipadjust,0.0]
		#print ("tip",tip,count)
		count=count+1
	return tip




def measurment(tipinit, surf, tipdd, pixies, lengthi, voltset, ampset, intetset, tppx):
	
	linescan=np.array([tipinit])
	
	#inititial setteling
	h=hmeassure(tipinit, surf, tipdd, voltset, ampset, intetset, 1)
	tipnow=tipinit
	while abs(h[1]-tipnow[1])>0.005:
		h=tipnow
		tipnow=hmeassure(h, surf, tipdd, voltset, ampset, intetset, 1)
		print h[1]-tipnow[1]

	n=1
	#scanning
	for n in range(pixies):
		g=hmeassure(tipnow, surf, tipdd, voltset, ampset, intetset, tppx)
		tipnow=g
		linescan=np.append(linescan,[tipnow],axis=0)
		print tipnow
		#print linescan
		tipnow= tipnow + [(lengthi/pixies),0,0]
	return linescan

liniscani=measurment(tipinit, surf, tipdd, pixies, lengthi, voltset, ampset, intetset, tppx)

#tipmove(tipinit, tipdd)

np.savetxt("line.txt", liniscani,fmt='%s', delimiter=';', newline='\n', header='', footer='', comments='# ', encoding=None)
