
from Math.gcd import greatest_common_divisor
from Math.fib import fibonacci_number_dp
from Math.fib import fibonacci_number_recursive
from Math.prime import is_prime


# gcd
print(greatest_common_divisor(12, 80))

# fib
# print(fibonacci_number_dp(-1))
for n in range(0, 50):
    print(fibonacci_number_dp(n), end=' ')
print()

for n in range(0, 10):
    print(fibonacci_number_recursive(n), end=' ')
print()

# prime
for n in range(-10, 10):
    print("{}\t{}".format(n, is_prime(n)))