import math

def f(t, y):
    return 0.5 * y

def solucion_exacta(t):
    return 100 * math.exp(0.5 * t)

# Parámetros
t, y_euler = 0, 100
t_final = 1
h = 0.2

print(f"{'t':>4} | {'Euler':>10} | {'Exacta':>10} | {'Error':>10}")
print("-" * 45)

while t <= t_final:
    exacta = solucion_exacta(t)
    error = abs(exacta - y_euler)
    
    print(f"{t:4.1f} | {y_euler:10.4f} | {exacta:10.4f} | {error:10.4f}")
    
    # Paso de Euler
    y_euler = y_euler + h * f(t, y_euler)
    t = round(t + h, 2)