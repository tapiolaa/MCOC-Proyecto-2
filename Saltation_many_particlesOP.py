from matplotlib.pylab import *
from time import time
tiempo_inicial = time()
# Unidades base SI (m, kg, s)
_m = 1.
_kg = 1.
_s = 1.
_mm = 1e-3*_m
_cm = 1e-2*_m
_gr = 1e-3*_kg 
_in= 2.54*_cm


g= 9.81*_m/_s**2
d= 15*_mm

rho_agua=1000.*_kg/(_m**3)
rho_particula= 2650.*_kg/(_m**3)

dt= 0.001*_s 
tmax= 1*_s
ti= 0.*_s



Nparticulas = 5

if Nparticulas <= 5:
	x0=10*d*rand(Nparticulas)
	y0=20*d*rand(Nparticulas)+d
elif Nparticulas > 5 and Nparticulas <=12:
	x0=30*d*rand(Nparticulas)
	y0=60*d*rand(Nparticulas)+d
else:
	x0=60*d*rand(Nparticulas)
	y0=90*d*rand(Nparticulas)+10*d

vx0= rand(Nparticulas)/2
vy0= rand(Nparticulas)/2

A=pi*(d/2)**2
V=(4./3.)*pi*(d/2)**3
m= rho_particula*V

W=array([0,-m*g])

t=arange(0,tmax,dt)
Nt=len(t)

norm= lambda v: sqrt(dot(v,v))

Cd=0.47
Cm= 2/3*pi*(d/2)**3*rho_agua # 0.5 ; para una esfera la masa aderida es 2/3*pi*(d/2)**3*rho_agua (sacado de wiki)
CL=0.2
Rp=73.
R= ((rho_particula/rho_agua) -1)
alpha= 1/(1+R+Cm)


ihat= array([1,0])
jhat= array([0,1])

ustar= 0.18*_m/_s # sqrt(tauw/rho_agua)

def velocity_field(x):
	z=x[1]/d
	if z>1./30:
		uf= ustar*log(30.*z)/0.41
	else:
		uf=0

	return array([uf,0])
vfx= velocity_field([0, 4*d])[0]
k_penal= 1000*0.5*Cd*rho_agua*A*norm(vfx)**2/(1*_mm)


def particula(z,t):
		zp = zeros(4*Nparticulas)

		for i in range(Nparticulas):
			di = d 
			xi = z[4*i:(4*i+2)]
			vi = z[4*i+2:(4*i+4)]

			xtop = xi + (d/2)*jhat
			xbot = xi - (d/2)*jhat
			vf = velocity_field(xi + 0*jhat)
			vf_top = abs(velocity_field(xtop)[0]) 
			vf_bot = norm(velocity_field(xbot)[0]) 
			vrel = vf - vi
			fD = (0.5*Cd*alpha*rho_agua*norm(vrel)*A)*vrel  #formula wiki
			#fD = alpha*(R*(d*g/(ustar**2))-(3./4.)*Cd*(vrel)*norm(vrel)) # formula PM
			fL = (0.5*CL*alpha*rho_agua*norm(vf_top**2 - vf_bot**2)*A)*jhat #formula wiki
			#fL = alpha*(3/4*CL*(norm(vf_top)**2 - norm(vf_bot)**2)) # formula PM
			fB =  alpha*(-rho_agua*g*V*jhat) # fromula de empuje


			Fi = W + fD + fL + fB

			xs = (xi[0]//d)*d + d/2
			cxs = array([xs,0])
			dxs = xi - cxs
			if norm(dxs) < d:
				delta = d - norm(dxs)
				nxs = dxs/norm(dxs)
				Fi += k_penal*delta*nxs

			zp[4*i:(4*i+2)] = vi
			zp[4*i+2:(4*i+4)] = Fi/m

			for i in range(Nparticulas):
				xi = z[4*i:(4*i+2)]
				for j in range(Nparticulas):
					if i > j:
						xj = z[4*j:(4*j+2)]
						rij = xj -xi
						if norm(rij) < d:
							delta = d - norm(rij)
							nij = rij/norm(rij)
							Fj = k_penal*delta*nij
							Fi = -k_penal*delta*nij
							zp[4*i+2:(4*i+4)] += Fi/m
							zp[4*j+2:(4*j+4)] += Fj/m

		return zp

#Choque entre particulas:
# j = -f*(1+e)*n*(vxi-vxj)*(m/2)

#choque con el suelo
# r/d = 0.5*(cos(tethab)-tan(tethain)*sin(tethab))
#promedio de los saltos de las particulas, H/d para un Tstar/tcritico definido.
# caracteristicas de pc, raficar tiempo de particulas respecto a cuantose demora.

from scipy.integrate import odeint
z0= zeros(4*Nparticulas)
z0[0::4]=x0
z0[1::4]=y0
z0[2::4]=vx0
z0[3::4]=vy0

print "Integrando"
z=odeint(particula,z0,t)
print "Fin"

fig=figure()

ax=gca()
for i in range(Nparticulas):
	xi=z[:,4*i]/d
	yi=z[:,4*i+1]/d
	col= rand(3)
	plot(xi[0],yi[0],"o",color="r")

	plot(xi,yi,color=col)

xmax = 0
for a in range(Nparticulas):
	xi=z[:,4*i:]
	xmax1 = max(xi[:,0])
	xmax = max([xmax,xmax1])

l = (xmax/d)*100
x = linspace(0, xmax, l)
x_mod_d = (x % d) - d/2
y = sqrt((d/2)**2 - x_mod_d**2)	
plot(x/d, y/d)

ax.axhline(d/2,color="k", linestyle="--")
ax.axhline(0,color="k", linestyle="--")
xlabel("Avance direccion X (mm)")
ylabel("Altura direccion Y (mm)")
title("Movimiento de particulas (plano XY)")
legend()
savefig("Np5_11.jpg")
tiempo_final= time() 

tiempo_de_compilacion= tiempo_final-tiempo_inicial	
print 'El tiempo de ejecucion fue:',tiempo_de_compilacion, "segundos" #En segundos

#axis("equal")

show()