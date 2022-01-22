
import numpy as np

sizex=5
modus=6
raradi=50

# ~ centri = np.array([[0,2,1]])
# ~ centri = np.array([[280,2,1]])
centri = np.array([[280,2,1]])
pointi = np.array([0,0,0])


tipdd=np.array([['x','y','m']])
tipdd=np.append(tipdd,centri,axis=0)


if modus==1:
	for i in range(-sizex,sizex+1,1):
	#pointi = centri + ([i*1.0,np.cosh(i*1.0)-1,0])


		tipdd=np.append(tipdd,pointi,axis=0)

if modus==2:
	for i in range(1,99,9):
		pointi = centri + ([np.arccosh(i*1.0),i*1.0,0])
		tipdd=np.append(tipdd,pointi,axis=0)
		pointi = centri + ([-np.arccosh(i*1.0),i*1.0,0])
		tipdd=np.append(tipdd,pointi,axis=0)
		
if modus==3:
	for i in range(1,99,9):
		pointi = centri + ([np.sqrt(i*55.0),i*1.0,0])
		tipdd=np.append(tipdd,pointi,axis=0)
		pointi = centri + ([-np.sqrt(i*55.0),i*1.0,0])
		tipdd=np.append(tipdd,pointi,axis=0)
	
if modus==4:
	for i in range(1,99,9):
		pointi = centri + ([np.sqrt(i*35.0),i*1.0,0])
		tipdd=np.append(tipdd,pointi,axis=0)
		pointi = centri + ([-np.sqrt(i*35.0),i*1.0,0])
		tipdd=np.append(tipdd,pointi,axis=0)

if modus==5:
	centri = np.array([[280,52,1]])
	for i in range(1,99,5):
		pointi = centri + ([raradi*np.cos(i*0.03),-raradi*np.sin(i*0.03)*1.0,0])
		tipdd=np.append(tipdd,pointi,axis=0)
		pointi = centri + ([-raradi*np.cos(i*0.03),-raradi*np.sin(i*0.03),0])
		tipdd=np.append(tipdd,pointi,axis=0)
	for k in range(raradi*10,raradi*10+20,5):
		pointi = centri + ([k*0.1,(.1*(k*0.1)**2)-.1*raradi*raradi,0])
		tipdd=np.append(tipdd,pointi,axis=0)
		pointi = centri + ([-k*0.1,(.1*(-k*0.1)**2)-.1*raradi*raradi,0])
		tipdd=np.append(tipdd,pointi,axis=0)

if modus==6:
	centri = np.array([[280,52,1]])
	for i in range(1,99,5):
		pointi = centri + ([raradi*np.cos(i*0.03),-raradi*np.sin(i*0.03)*1.0,0])
		tipdd=np.append(tipdd,pointi,axis=0)
		pointi = centri + ([-raradi*np.cos(i*0.03),-raradi*np.sin(i*0.03),0])
		tipdd=np.append(tipdd,pointi,axis=0)
	for k in range(raradi*10,raradi*10+20,5):
		pointi = centri + ([k*0.1,(.1*(k*0.1)**2)-.1*raradi*raradi,0])
		tipdd=np.append(tipdd,pointi,axis=0)
		pointi = centri + ([-k*0.1,(.1*(-k*0.1)**2)-.1*raradi*raradi,0])
		tipdd=np.append(tipdd,pointi,axis=0)
	for j in range(1,tipdd.shape[0],1):
		if float(tipdd[j][0])>=280.0:
			print(tipdd[j][1])
			tipdd[j][1]=float(tipdd[j][1])+3
			print(tipdd[j][1])


# ~ for i in range(sizex):
	
	# ~ tipdd=np.append(tipdd,[[i,3,1]],axis=0)


print (tipdd)

np.savetxt("tipi.txt", tipdd,fmt='%s', delimiter=';', newline='\n', header='', footer='', comments='# ', encoding=None)
