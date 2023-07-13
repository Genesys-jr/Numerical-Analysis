import math

def bisection(f, a, b, tolerance=0.0001, max_iterations=100):
    if f(a) * f(b) >= 0:
        print("Bisection method is not applicable to the given interval.")
        return None

    c = a
    iterations = 0

    while (b - a) >= tolerance and iterations < max_iterations:
        c = (a + b) / 2

        if f(c) == 0.0:
            break

        if f(c) * f(a) < 0:
            b = c
        else:
            a = c

        iterations += 1

    return c

def fixed_point(g, x0, tolerance=0.0001, max_iterations=100):
    x = x0
    iterations = 0

    while True:
        x_next = g(x)

        if abs(x_next - x) < tolerance or iterations >= max_iterations:
            break

        x = x_next
        iterations += 1

    return x

def newton_raphson(f, f_prime, x0, tolerance=0.0001, max_iterations=100):
    x = x0
    iterations = 0

    while True:
        x_next = x - f(x) / f_prime(x)

        if abs(x_next - x) < tolerance or iterations >= max_iterations:
            break

        x = x_next
        iterations += 1

    return x

# Function f(x) example
def f(x):
    return x**3 - x**2 + 2

# Function g(x) example for fixed-point iteration
def g(x):
    return math.sqrt(x**2 - 2)

# Derivative of f(x) example
def f_prime(x):
    return 3 * x**2 - 2 * x

# Main program
print("Choose a method of solution:")
print("(1) Bisection")
print("(2) Fixed-Point")
print("(3) Newton-Raphson")

choice = int(input("Enter your choice: "))

if choice == 1:
    a = float(input("Enter the lower bound: "))
    b = float(input("Enter the upper bound: "))
    root = bisection(f, a, b)
elif choice == 2:
    x0 = float(input("Enter the initial guess: "))
    root = fixed_point(g, x0)
elif choice == 3:
    x0 = float(input("Enter the initial guess: "))
    root = newton_raphson(f, f_prime, x0)
else:
    print("Invalid choice. Please choose a number from 1 to 3.")

if root is not None:
    print("The root is approximately:", root)
else:
    print("Unable to find the root within the given parameters.")