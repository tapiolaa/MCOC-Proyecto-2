# Proyecto 2 
from matplotlib.pylab import *


#Unidades base SI
_m = 1.
_kg = 1.
_s = 1.
_mm = 1e-3*_m

_gr = 1e-3*_kg


#velocidades iniciales
vfx = 5.0*_m/_s #m/s 
vfy = 0.0*_m/_s #m/s 

x0 = array([0.,1.], dtype =double)
v0 = array([1.,1.], dtype =double)

#velocidad y posicion actual
xi =x0
vi =v0

#velocidad y posicion en el instante mas 1
xim1 =zeros(2, dtype=double)
vim1 =zeros(2, dtype=double)



g = 9.81 *_m/_s**2
d= 1*_mm
rho = 2700.*_kg/(_m**3)
Cd = 0.47 # particula esferica


m = rho *(4./3./8.)*pi*(d**3)   # masa de la particula

#Inicializar Euler en x0

dt= 2e-6*_s   #paso de tiempo
tmax = 0.1*_s   # tiempo maximo de simulacion


ti = 0.0*_s   #tiempo actual

W=array([0, -m*g])
vf=array([vfx,vfy])


Nt = int32(2*tmax /dt) 
x_store = zeros((2,Nt))
v_store = zeros((2,Nt))
t_store = zeros((Nt))
# Empieza metodo de euler

i = 0
while ti < tmax:


	if i % 100 == 0:
		print "ti =", ti," |xi| =", sqrt(dot(xi,xi))
    	#print "x_i =", x_i
    	#print "v_i =", v_i

	# evaluar velocidad relativa
	vrel = vf - vi                      # velocidad relativa,  velocidad relativa de la particula en comparacion con la velocidad del flujo
	norm_vrel = sqrt(dot(vrel, vrel))   # norma velocidad relativa
	# evaluar fuerzas sobre la particula
	fD = 0.5*Cd*norm_vrel*vrel          # Fuerza de Drag
	Fi = W + fD                               # Sumatoria de todas las fuerzas que se ejercen sobre la particula

	#print "F_i =", F_i
	# evaluar aceleracion
	ai = Fi / m  # Fuerza = masas * aceleracion

	#print "a_i =", a_i
	# integrar, donde xi es un arreglo

	xim1 = xi + vi*dt + ai*(dt**2/2) # base del algoritmo, se calcula la posicion con esta formula
	vim1 = vi + ai*dt

	# avanzar al siguiente paso
	x_store[:, i] = xi
	v_store[:, i] = vi
	t_store[:] = ti

	ti += dt # adelanto el tiempo
	i += 1
	xi = xim1	# adelanto la posicion
	vi = vim1
	

# guardar ultimo paso
x_store[:, i] = xi
v_store[:, i] = vi
t_store[:] = ti


print x_store
figure()
plot(x_store[0, :i], x_store[1, :i])
show()
