
import numpy as np

matconstx=.316
matconsty=.316

sizex=5
modus=7
raradi=int(50/matconstx)

# ~ centri = np.array([[0,2,1]])
# ~ centri = np.array([[280,2,1]])
centri = np.array([[280.0,2.0,1.0]])
pointi = np.array([0,0,0])


tipdd=np.array([['x','y','m']])
# ~ tipdd=np.append(tipdd,centri,axis=0)


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
	centri = np.array([[280.0,52.0,1.0]])
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
	centri = np.array([[280.0/matconstx,52.0/matconsty,1.0]])
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
		if float(tipdd[j][0])>=centri[0][0]:
			# ~ print(tipdd[j][1])
			tipdd[j][1]=float(tipdd[j][1])+50
			# ~ print(tipdd[j][1])

if modus==7:
	centri = np.array([[280.0/matconstx,52.0/matconsty,1.0]])
	print(centri,raradi)
	m1=4
	m2=1
	m3=3
	bre1=22
	bre2=80
	for i in range(1,90,5):
		pointi = centri + ([-raradi*np.cos(i*np.pi/180),-raradi*np.sin(i*np.pi/180),0])
		tipdd=np.append(tipdd,pointi,axis=0)
		if i <=bre1:
			ypsy=m1*i
			ypsym=(m3*(90-bre2))+(m2*bre2)+(m1*bre1)
			pointi = centri+([i*raradi/90,raradi*(ypsy/ypsym)-raradi,0])
			# ~ pointi = centri+([i*raradi/90,m1*i-raradi,0])
			tipdd=np.append(tipdd,pointi,axis=0)
			print(i,'1',pointi)
		elif i <=bre2:
			ypsy=(m2*(i-bre1))+(m1*bre1)
			ypsym=(m3*(90-bre2))+(m2*bre2)+(m1*bre1)
			pointi = centri+([i*raradi/90,raradi*(ypsy/ypsym)-raradi,0])
			# ~ pointi = centri+([i*raradi/90,(m2*(i-bre1)-raradi)+(m1*bre1),0])
			tipdd=np.append(tipdd,pointi,axis=0)
			print(i,'2',pointi)
		elif i >bre2:
			ypsy=(m3*(i-bre2))+(m2*bre2)+(m1*bre1)
			ypsym=(m3*(90-bre2)+(m2*bre2)+(m1*bre1))
			pointi = centri+([i*raradi/90,raradi*(ypsy/ypsym)-raradi,0])
			# ~ pointi = centri+([i*raradi/90,(m3*(i-bre2)-raradi)+(m2*bre2)+(m1*bre1),0])
			tipdd=np.append(tipdd,pointi,axis=0)
			print(i,'3',pointi)
	for k in range(raradi*10,raradi*10+20,5):
		pointi = centri + ([k*0.1,(.1*(k*0.1)**2)-.1*raradi*raradi,0])
		tipdd=np.append(tipdd,pointi,axis=0)
		pointi = centri + ([-k*0.1,(.1*(-k*0.1)**2)-.1*raradi*raradi,0])
		tipdd=np.append(tipdd,pointi,axis=0)


tipilis=np.empty([0,3])
print(tipdd.shape)
for g in range(1,tipdd.shape[0]):
	tipddff=(np.floor(float(tipdd[g][0])),np.floor(float(tipdd[g][1])),float(tipdd[g][2]))
	tipilis=np.append(tipilis,[tipddff],axis=0)
	tipddcc=(np.ceil(float(tipdd[g][0])),np.ceil(float(tipdd[g][1])),float(tipdd[g][2]))
	tipilis=np.append(tipilis,[tipddcc],axis=0)
	tipddfc=(np.floor(float(tipdd[g][0])),np.ceil(float(tipdd[g][1])),float(tipdd[g][2]))
	tipilis=np.append(tipilis,[tipddfc],axis=0)
	tipddcf=(np.ceil(float(tipdd[g][0])),np.floor(float(tipdd[g][1])),float(tipdd[g][2]))
	tipilis=np.append(tipilis,[tipddcf],axis=0)

# ~ print(tipilis)

tipdd2=np.unique(tipilis,axis=0)
# ~ print (tipdd2)

# ~ tipdd2=np.sort(tipdd2,axis=1)
tipdd2=tipdd2[tipdd2[:, 1].argsort()]
tipdd2=np.append(tipdd2,[['x','y','m']],axis=0)
tipdd2=np.roll(tipdd2,1,axis=0)


for jj in range(1,tipdd2.shape[0]):
	tipdd2[jj]=[float(tipdd2[jj,0])*matconstx,float(tipdd2[jj,1])*matconsty,float(tipdd2[jj,2])]

# ~ print(tipdd2)
# ~ print (centrus)
# ~ print (centri[0])
# ~ print (tipdd2[1])

# ~ for i in range(sizex):
	
	# ~ tipdd=np.append(tipdd,[[i,3,1]],axis=0)


# ~ print (tipdd2)

np.savetxt("tipi.txt", tipdd2,fmt='%s', delimiter=';', newline='\n', header='', footer='', comments='# ', encoding=None)
