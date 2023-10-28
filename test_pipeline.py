import random
import primes

def test_is_prime():
	is_prime_0 = primes.is_prime(0)
	is_prime_1 = primes.is_prime(1)
	is_prime_2 = primes.is_prime(10)
	is_prime_3 = primes.is_prime(97)

	assert not is_prime_0
	assert not is_prime_1
	assert not is_prime_2
	assert is_prime_3

def test_primes():
	primes_0 = primes.primes(0)
	primes_1 = primes.primes(1)
	primes_2 = primes.primes(1000)

	assert len(primes_0) == 0
	assert len(primes_1) == 1
	assert len(primes_2) == 1000

def test_checksum():
	random.seed(100)
	checksum_0 = primes.checksum(primes.primes(10))

	assert checksum_0 == 4405291

def test_pipeline():
	pipeline_0 = primes.pipeline()

	assert pipeline_0 == 7785816

test_pipeline()