# Q3. Recursive factorial and Fibonacci series

def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    if n == 0 or n == 1:       # Base condition
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    series = fibonacci(n - 1)
    series.append(series[-1] + series[-2])
    return series

number = int(input("Enter a number for factorial: "))
print("Factorial:", factorial(number))

terms = int(input("Enter number of Fibonacci terms: "))
print("Fibonacci series:", fibonacci(terms))
