import random
import sys
from sys import stdin

def is_prime(x: int) -> bool:
	if x <= 1:
		return False
	else:
		for y in range(2, x):
			if x % y == 0:
				return False
		else:
			return True


def primes(n: int) -> list[int]:
	res = []
	x = 0
	while len(res) < n:
		if is_prime(x):
			res.append(x)
		x += 1
	return res


def checksum(nums: list[int]) -> int:
	cnt_sum = 0
	for el in nums:
		cnt_sum += el
		cnt_sum *= 113
		cnt_sum = cnt_sum % 10000007
	return cnt_sum

def pipeline(seed_: int) -> int:
	random.seed(seed_)
	prime_list = primes(1000)
	random.shuffle(prime_list)
	return checksum(prime_list)


def main():
	seed_ = int(sys.argv[1])
	print(pipeline(int(seed_)))
main()
