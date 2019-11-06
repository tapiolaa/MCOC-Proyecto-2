# MCOC-Proyecto-2

Integrantes:

- Fernanda Arcos Hernández
- Fabian Cortes Figueroa (https://github.com/fabianszne)
- Roberto Cruz Fernández (https://github.com/RobertoCruzF)
- Anibal Tapia Triviño   (https://github.com/tapiolaa)

# Introducción
En este proyecto se implementará y validará un modelo de simulación de transporte de sedimentos en base a un método lagrangiano, en específico el método de Euler. 
La validación se hará a nivel del comportamiento de una partícula individual y luego con el comportamiento estadístico de cantidades
crecientes de partículas.

# Objetivos
Implementar un modelo de simulacion numerico para transporte de sedimentos de fondo. Comprender aspectos de desempeño de aplicaciones de computación científica tales como IO y complejidad algorítmica.

- [Meta 3] : Implementación y validación del código para una partícula considerando un perfil de velocidades sencillo.
- [Entrega 3] : (script saltation_one_particle.py) Como resultado del código se obtienen dos gráficos en los cuales se observa el movimiento de la partícula, tanto en las direcciones x e y.

- [Meta 4] : Implementacion del código para múltiples partículas considerando un perfil de velocidad sencillo; además de uno complejo.
- [Entrega 4] : (script saltation_many_particles_validation.py) Para el código se comienza por abordar el movimiento de más de una partícula, específicamente 2 con un perfil de velocidad sencillo; luego se pretende poder entregar los resultados para un número de partículas deseadas por el usuario, creando un input y con esto un ciclo que permita guardar las posiciones de cada una de estas partículas.


Especifiaciones del computador
=============================

- SO : Windows 10 - 64 bits
- Procesador: AMD A10-9620P, 10 COMPUTE CORES 4C+6G (4CPUs), 2.5GHz
- Versión DirectX: DirectX 12
- Gráficos : AMD Radeon R5 6GB, VRAM 500MB
- RAM: 12GB
- HDD: 1TB
- SSD: 240GB

Simulación Entrega 4
====================

Simulación del movimiento de n partículas durante un periodo de timepo de 1 segundo con un dt = 0.001. Se incluyen fuerzas que afectan el comportamiento y choque entre ellas como fuerza de lift, drag, fuerza boyante y fuerza de gravedad.

Se compara la velocidad de los computadores del equipo de trabajo con diferentes especificaciones para correr el código. También se presentan los tiempos que demora el equipo en correr la simulación con diferentes cantidades de partículas que irán entre 1 a 20.

- Tiempos de compilación: 

A continuación se encuentra un gráfico que muestra los tiempos de compilación obtuvidos al momento de ejecutar el código con diferentes cantidades de partículas.

![GraficoOP](https://user-images.githubusercontent.com/53720008/66693038-dda11f00-ec7a-11e9-8d62-31a0e28239e0.jpg)
![tablaOP](https://user-images.githubusercontent.com/53720008/66693052-f14c8580-ec7a-11e9-8c63-1e098f1d3d3e.jpg)


Análisis de resultados
======================

-Comportamiento de las partículas:

El comportamiento de las partículas ha sido ilustrado en gráficos de movimiento en dirección x y en direccion y. Aquí se puede apreciar los desplazamientos que siguen las partículas junto con los choques, representados por los peaks de las curvas y los rebotes propios de los elementos y la física, representados cuando la curva toca el eje x. Los siguientes gráficos muestran los comportamiendos de 2, 5, 10, 15 y 20 partículas.

  - Desplazamiento 2 partículas
  ![Np2_11](https://user-images.githubusercontent.com/53720008/66692689-28b93300-ec77-11e9-8f50-e832e67a6be2.jpg)

  -Desplazamiento 5 partículas
  ![Np5_11](https://user-images.githubusercontent.com/53720008/66693066-222cba80-ec7b-11e9-919c-68fb1beecdbd.jpg)

  -Desplazamientos 10 partículas
  ![Np10_12](https://user-images.githubusercontent.com/53720008/66692878-150ecc00-ec79-11e9-8c12-66d917ba4c89.jpg)

  -Desplazamiento 15 partículas
  ![Np15_12](https://user-images.githubusercontent.com/53720008/66692708-6453fd00-ec77-11e9-9d44-50d74b7696b9.jpg)

  -Desplazamiento 20 partículas
  ![Np20_1](https://user-images.githubusercontent.com/53720008/66692882-248e1500-ec79-11e9-8348-3cf43b1e6e9b.jpg)
  
  
- Diferencias con la primera iteración del código:

En una primera iteración con el código "saltation_many_particles_validation.py", los tiempos de compilación del código eran muy extensos tal como se muestra en el gráfico y tabla adjuntos. Esto se debia a que las párticulas partían desde el origen a muy poca distancia de separación unas de las otras aumentando las posibilidades de choques entre ellas. Posteriormente, el código fue optimizado aumentando esta distancia entre partículas y los resultados fueron sorprendentemente menores, llegando a reducirse en un 90% para el caso de 20 partículas. Este nuevo código es en llamado "saltation_many_particles_validationOP.py".

A continuación se encuentran los resultados de la primera iteración.

![Gráfico tiempo de compilación](https://user-images.githubusercontent.com/53720008/66688633-d7e91080-ec5d-11e9-9211-fc304c31b13b.jpg)
![Tabla de datos de compilación](https://user-images.githubusercontent.com/53720008/66688860-e08e1680-ec5e-11e9-8374-0258613dcad9.jpg)

Simulación Entrega 6
====================

Para esta entrega se ha modificado el código de la entrega 4, con la finalidad de disminuir los tiempos de compilación. El objetivo se ha logrado, como se puede ver en el gráfico adjunto donde ahora la curva tiene un comportamiento lineal, gracias a que la separación de los integradores para las partículas que colisionan permite acortar los tiempos, situación que antes no se diferenciaba entre las que chocan o no.

Por otra parte, se ha reducido la cantidad de RAM que ocupa la máquina con la ayuda de archivos .npz y .h5py los cuales permiten guardar datos de manera binaria sin la necesidad de trabajarlos para luego utilizarlos, sino que se mantienen en este formato y luego el programa los reconoce como tal ahorrándo el tiempo de las conversiones.

A continuación se presenta la curva de tiempos de compilación que se obtuvo.

![tiemposOP](https://user-images.githubusercontent.com/53720008/68264387-71220180-0027-11ea-8f09-b568aa9de7fb.png)

cant_particulas = [2, 6, 10, 20, 30, 40, 50, 80, 100]

tiempos = [7.33, 19.03, 28.46, 59.76, 91.28, 126.53, 181.92, 302.56, 408.15]
