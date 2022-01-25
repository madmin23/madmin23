import numpy as np
from tqdm import tqdm

#tipinit=np.array([90,2.477,0]) #initial tip position
tipinit=np.array([0,4,0])

#current-parameters
voltset=2.0	#set-Voltage
ampset=5	#set-Current
intetset=20 #integrationtime 30

#image parameters
pixies=1024 # number of measurements
lengthi=300.0	# spacing of pixels
tppx=1 #time per pixel 10


#curr=(volts/amps)*scalar 

#print (curr)

surf=np.loadtxt("surface.txt", comments='#', delimiter=";", converters=None, skiprows=1)

tipdd=np.loadtxt("tipi.txt", comments='#', delimiter=";", converters=None, skiprows=1)

#print(surf)


def tipmove(tipnow, tipdd):
	j=0
	tipdds=tipdd.shape
	for j in range(tipdds[0]):
		#print ("now", tipnow)
		tipdd[j]=tipdd[j]+tipnow
		#print tipdd[j]
	#print tipdd

def hmeassure(tip, surf, tipdd, volts, amps, intet, tppx):
	i=0
	q=0
	tipscalar=.17 # limits tip movement 0.001######0.1#############0.15
	tipadjust=1
	count=0

	surfs=surf.shape
	tipdds=tipdd.shape
	
	tipmove(tip, tipdd)
	
	#print (surfs[0])
	#print (surf[i])
	
	#while abs(tipadjust)>0.0001:
	while count <= tppx:
		alltunc=0
		tunc=0
		for q in range(tipdds[0]):
			tip=tipdd[q]
			for i in range(surfs[0]):
				k=surf[i]-tip

				#print("k ",k)

				dis=np.sqrt((k[0]**2)+(k[1]**2))
				#print ("dis ",dis)

				#poni=volts*np.exp(-(dis/surf[i,2]))
				poni=volts*np.exp(-(1*dis/surf[i,2]))
				#print ("poni ",poni)
				for n in range(intet):
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
		# ~ tipadjust=tipscalar*(alltunc-amps)**3
		# ~ print ("TTTTTT",tipadjust)
		if abs(tipadjust)>6.0:
			tipadjust=(tipadjust/abs(tipadjust))*6.0
			print (tipadjust,"ipitopi")
		tipmove([0.0, tipadjust, 0.0],tipdd)
		#tip = tip + [0.0,tipadjust,0.0]
		#print ("tip",tip,count)
		count=count+1
	return tipdd




def measurment(tipinit, surf, tipdd, pixies, lengthi, voltset, ampset, intetset, tppx):
	
	linescan=np.array([tipinit])
	
	#inititial setteling
	tipnowh=np.array(tipdd)
	h=np.array(tipdd)
	
	#tipnowh=tipdd
	#print tipnowh
	#h=hmeassure(tipinit, surf, tipdd, voltset, ampset, intetset, 2)
	h=np.array(hmeassure(tipinit, surf, tipdd, voltset, ampset, intetset, 2)) 
	#print h
	#print ("hmhmhm",h[0,1]-tipnowh[0,1],h[0,1],tipnowh[0,1])
	while abs(h[0,1]-tipnowh[0,1])>0.005:
		#h=hmeassure([0,0,0], surf, tipdd, voltset, ampset, intetset, 2)
		h=np.array(hmeassure([0,0,0], surf, tipdd, voltset, ampset, intetset, 1)) 
		#print ("p",tipdd, tipnowh, h)
		tipnowh=np.array(hmeassure([0,0,0], surf, tipdd, voltset, ampset, intetset, 1)) 
		
		
		#print ("a",tipdd, tipnowh, h)
		
		#h=tipnowh
		hihi=h[1]-tipnowh[1]
		# ~ print ("HHHHH",tipdd[0,1],h[1]-tipnowh[1])
		print ("hihih",tipdd[0,1],hihi[1])
	
	n=1
	#scanning
	tipnow=[0,0,0]
	for n in tqdm(range(pixies)):
		g=hmeassure(tipnow, surf, tipdd, voltset, ampset, intetset, tppx)
		tipnow=g[0]
		linescan=np.append(linescan,[tipnow],axis=0)
		#print tipnow
		#print ("line", linescan)
		tipnow= [(lengthi/pixies),0.0,0.0]
		#print ("loading "+ str(n) + "/" + str( pixies))
	return linescan

liniscani=measurment(tipinit, surf, tipdd, pixies, lengthi, voltset, ampset, intetset, tppx)

#tipmove(tipinit, tipdd)

#tipmove([0,-0.5,0], tipdd)

#h=hmeassure([0,0,0], surf, tipdd, voltset, ampset, intetset, 2)



np.savetxt("line.txt", liniscani,fmt='%s', delimiter=';', newline='\n', header='', footer='', comments='# ', encoding=None)
