# recursion = a function that calls itself from within
# helps to visualize a complex problem into basic steps
# problems can be solved more easily iteratively or recursively
# iterative = faster, complex
# recursive = slower, simpler

def walk(steps):
    if steps == 0:
        return
    walk(steps - 1)
    print(f"You take step {steps}")

# walk(20)

def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(f"factorial of is {factorial(10)}")
