import math

def get_largest_prime_factor(n):
	upto = int(math.sqrt(n))+1
	ans = 0
	for i in range(2,upto):
		while n % i == 0:
			n = n / i
			ans = i

	if n > 1:
		ans = n

	return ans

n = 600851475143
largest_prime_factor = get_largest_prime_factor(n)
print (largest_prime_factor)	