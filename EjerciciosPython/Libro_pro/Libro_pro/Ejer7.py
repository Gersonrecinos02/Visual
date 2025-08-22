import matplotlib.pyplot as plt
import numpy as np

# Definir rango de x
x = np.linspace(-10, 10, 400)

# Definir las funciones despejadas de y
y1 = (1/3) * x - (4/3)   # De x - 3y = 4  ->  y = (1/3)x - 4/3
y2 = 2 * x + 3           # De -4x + 2y = 6  ->  y = 2x + 3

# Crear la gráfica
plt.figure(figsize=(8, 6))
plt.plot(x, y1, label=r'$y = \frac{1}{3}x - \frac{4}{3}$', color='blue')
plt.plot(x, y2, label=r'$y = 2x + 3$', color='green')

# Punto de intersección calculado
x_int = -13/5
y_int = -11/5
plt.plot(x_int, y_int, 'ro')  # Punto rojo para la solución
plt.text(x_int + 0.5, y_int, f'({x_int:.2f}, {y_int:.2f})', color='red')

# Configuración del gráfico
plt.axhline(0, color='black', linewidth=0.5)  # Eje x
plt.axvline(0, color='black', linewidth=0.5)  # Eje y
plt.grid(True, linestyle='--', alpha=0.6)
plt.title('Solución por Método Gráfico')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.gca().set_aspect('equal', adjustable='box')

# Mostrar gráfica
plt.show()
