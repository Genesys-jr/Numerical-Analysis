import math
import matplotlib.pyplot as plt

def bisection(f, a, b, error_criteria, function_criteria, max_iterations):
    # Bisection method
    iterations = 0
    flag = 0  # Flag to indicate stopping criteria
    x = a
    prev_x = None
    error = 100.0  # Initialize error to a high value

    # Lists to store values for plotting
    iteration_numbers = []
    errors = []

    while iterations < max_iterations:
        if abs(error) < error_criteria:
            flag = 1  # Stopping criteria (i) met
            break

        if abs(f(x)) < function_criteria:
            flag = 2  # Stopping criteria (ii) met
            break

        if iterations > 0:
            error = abs((x - prev_x) / x) * 100.0  # Calculate relative approximate error
            if error < error_criteria:
                flag = 3  # Stopping criteria (iii) met
                break

        prev_x = x

        # Bisection step
        c = (a + b) / 2.0
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c

        iterations += 1
        x = c

        # Append values for plotting
        iteration_numbers.append(iterations)
        errors.append(error)

    root = x
    return root, flag, iteration_numbers, errors

def fixed_point(g, x0, error_criteria, function_criteria, max_iterations):
    # Fixed-Point method
    iterations = 0
    flag = 0  # Flag to indicate stopping criteria
    x = x0
    prev_x = None
    error = 100.0  # Initialize error to a high value

    # Lists to store values for plotting
    iteration_numbers = []
    errors = []

    while iterations < max_iterations:
        if abs(error) < error_criteria:
            flag = 1  # Stopping criteria (i) met
            break

        if abs(g(x) - x) < function_criteria:
            flag = 2  # Stopping criteria (ii) met
            break

        if iterations > 0:
            error = abs((x - prev_x) / x) * 100.0  # Calculate relative approximate error
            if error < error_criteria:
                flag = 3  # Stopping criteria (iii) met
                break

        prev_x = x

        # Fixed-Point iteration step
        x = g(x)

        iterations += 1

        # Append values for plotting
        iteration_numbers.append(iterations)
        errors.append(error)

    root = x
    return root, flag, iteration_numbers, errors

def newton_raphson(f, f_prime, x0, error_criteria, function_criteria, max_iterations):
    # Newton-Raphson method
    iterations = 0
    flag = 0  # Flag to indicate stopping criteria
    x = x0
    prev_x = None
    error = 100.0  # Initialize error to a high value

    # Lists to store values for plotting
    iteration_numbers = []
    errors = []

    while iterations < max_iterations:
        if abs(error) < error_criteria:
            flag = 1  # Stopping criteria (i) met
            break

        if abs(f(x)) < function_criteria:
            flag = 2  # Stopping criteria (ii) met
            break

        if iterations > 0:
            error = abs((x - prev_x) / x) * 100.0  # Calculate relative approximate error
            if error < error_criteria:
                flag = 3  # Stopping criteria (iii) met
                break

        prev_x = x

        # Newton-Raphson iteration step
        x = x - f(x) / f_prime(x)

        iterations += 1

        # Append values for plotting
        iteration_numbers.append(iterations)
        errors.append(error)

    root = x
    return root, flag, iteration_numbers, errors

def plot_function(f, x_values, title):
    y_values = [f(x) for x in x_values]
    plt.plot(x_values, y_values)
    plt.axhline(y=0, color='black', linewidth=0.5)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title(title)
    plt.grid(True)
    plt.show()

def plot_errors(iteration_numbers, errors, title):
    plt.plot(iteration_numbers, errors)
    plt.xlabel('Iteration')
    plt.ylabel('Relative Approximate Error (%)')
    plt.title(title)
    plt.grid(True)
    plt.show()

def main():
    # Test functions
    equation_1 = lambda x: x - math.cos(x)
    equation_1_derivative = lambda x: 1 + math.sin(x)
    equation_2 = lambda x: math.exp(-x) - x
    equation_2_derivative = lambda x: -math.exp(-x) - 1
    equation_3 = lambda x: x**4 - 7.4*x**3 + 20.44*x**2 - 24.184*x + 9.6448

    # User input
    print("Choose the method of solution:")
    print("(1) Bisection")
    print("(2) Fixed-Point")
    print("(3) Newton-Raphson")
    method = int(input("Enter your choice: "))

    if method == 1:
        # Bisection method
        print("Bisection Method")
        a = float(input("Enter the left interval point (a): "))
        b = float(input("Enter the right interval point (b): "))
        f = equation_1  # Change this to test different equations
        error_criteria = float(input("Enter the convergence criterion for relative approximate errors (%): "))
        function_criteria = float(input("Enter the convergence criterion for function value: "))
        max_iterations = int(input("Enter the maximum number of iterations: "))

        # Compute root using Bisection method
        root, flag, iteration_numbers, errors = bisection(f, a, b, error_criteria, function_criteria, max_iterations)

        # Print results
        print("Root:", root)
        print("Stopping Criteria Flag:", flag)

        # Plot f(x) vs. x
        x_values = [a + i * (b - a) / 1000 for i in range(1001)]
        plot_function(f, x_values, "Bisection Method: f(x) vs. x")

        # Plot the approximate relative error vs. iteration number
        plot_errors(iteration_numbers, errors, "Bisection Method: Approximate Relative Error vs. Iteration Number")

    elif method == 2:
        # Fixed-Point method
        print("Fixed-Point Method")
        x0 = float(input("Enter the initial guess (x0): "))
        g = equation_1_derivative  # Change this to test different equations
        error_criteria = float(input("Enter the convergence criterion for relative approximate errors (%): "))
        function_criteria = float(input("Enter the convergence criterion for function value: "))
        max_iterations = int(input("Enter the maximum number of iterations: "))

        # Compute root using Fixed-Point method
        root, flag, iteration_numbers, errors = fixed_point(g, x0, error_criteria, function_criteria, max_iterations)

        # Print results
        print("Root:", root)
        print("Stopping Criteria Flag:", flag)

        # Plot f(x) vs. x
        x_values = [x0 + i * (root - x0) / 1000 for i in range(1001)]
        plot_function(f, x_values, "Fixed-Point Method: f(x) vs. x")

        # Plot the approximate relative error vs. iteration number
        plot_errors(iteration_numbers, errors, "Fixed-Point Method: Approximate Relative Error vs. Iteration Number")

    elif method == 3:
        # Newton-Raphson method
        print("Newton-Raphson Method")
        x0 = float(input("Enter the initial guess (x0): "))
        f = equation_1  # Change this to test different equations
        f_prime = equation_1_derivative  # Change this to the derivative of the chosen equation
        error_criteria = float(input("Enter the convergence criterion for relative approximate errors (%): "))
        function_criteria = float(input("Enter the convergence criterion for function value: "))
        max_iterations = int(input("Enter the maximum number of iterations: "))

        # Compute root using Newton-Raphson method
        root, flag, iteration_numbers, errors = newton_raphson(f, f_prime, x0, error_criteria, function_criteria, max_iterations)

        # Print results
        print("Root:", root)
        print("Stopping Criteria Flag:", flag)

        # Plot f(x) vs. x
        x_values = [x0 + i * (root - x0) / 1000 for i in range(1001)]
        plot_function(f, x_values, "Newton-Raphson Method: f(x) vs. x")

        # Plot the approximate relative error vs. iteration number
        plot_errors(iteration_numbers, errors, "Newton-Raphson Method: Approximate Relative Error vs. Iteration Number")

    else:
        print("Invalid choice. Please try again.")

# Run the program
main()