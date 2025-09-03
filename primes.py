from sympy import primerange

def build_prime_triangle(limit=100):
    # Step 1: Get all primes ≤ 100
    primes = list(primerange(0, limit + 1))
    triangle = [primes]

    # Step 2: Compute first derived column: (next - current) / 2
    derived = [(primes[i+1] - primes[i]) / 2 for i in range(len(primes) - 1)]
    triangle.append(derived)

    # Step 3: Continue computing successive differences
    while len(triangle[-1]) > 1:
        prev = triangle[-1]
        next_layer = [prev[i+1] - prev[i] for i in range(len(prev)-1)]
        triangle.append(next_layer)

    return triangle

def print_triangle(triangle):
    height = len(triangle[0])
    width = len(triangle)

    for i in range(height):
        row = ''
        for j in range(width):
            if i < len(triangle[j]):
                val = triangle[j][i]
                row += '\t' * j + f'{val}' + '\t'
        print(row)

# Run and print
triangle = build_prime_triangle(100)
print_triangle(triangle)
