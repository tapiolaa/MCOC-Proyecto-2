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

Simulación E4
=============

Simulación del movimiento de n partículas durante un periodo de timepo de 1 segundo con un dt = 0.001. Se incluyen fuerzas que afectan el comportamiento y choque entre ellas como fuerza de lift, drag, fuerza boyante y fuerza de gravedad.

Se compara la velocidad de los computadores del equipo de trabajo con diferentes especificaciones para correr el código. También se presentan los tiempos que demora el equipo en correr la simulación con diferentes cantidades de partículas que irán entre 1 a 20.

- Tiempos de compilación: 

A continuación se encuentra un gráfico que muestra los tiempos de compilación obtuvidos al momento de ejecutar el código con diferentes cantidades de partículas.

![Gráfico tiempo de compilación](https://user-images.githubusercontent.com/53720008/66688633-d7e91080-ec5d-11e9-9211-fc304c31b13b.jpg)
