import time

def factors(n):
    _n = n
    i = 2
    primes = []
    while i <= n/2:
        if _n % i == 0:
            primes.append(i)
            print(_n)
            _n //= i
        else:
            i += 1
    return primes



def evaluate(start, end):
    def sieve_of_eratosthenes(n):
        """Generate a list of prime numbers up to n."""
        sieve = [True] * (n + 1)
        sieve[0], sieve[1] = False, False
        for i in range(2, int(n**0.5) + 1):
            if sieve[i]:
                for j in range(i*i, n + 1, i):
                    sieve[j] = False
        return [i for i, v in enumerate(sieve) if v]

    def primes_in_range(start, end):
        """Generate a list of prime numbers in the given range [start, end]."""
        primes = sieve_of_eratosthenes(end)
        return [p for p in primes if p >= start]
    prime_nums = primes_in_range(start, end)
    prev_num = prime_nums[0]
    filtered_primes = []
    for num in prime_nums:
        if num / prev_num < 2:
            continue
        filtered_primes.append(num)
        prev_num = num
    print("[INFO] Testing on numbers:", filtered_primes)
    print("\n   n\t|  T(n) (seconds)")
    print("-------------------------")
    for num in filtered_primes:
        start_time = time.time()
        factors(num)
        end_time = time.time()
        print(f'{num}\t|\t{round((end_time - start_time) * 1000, 4)}\t|')

if __name__ == "__main__":
    # evaluate(30, 1000000)
    


    # start = time.time()
    print(factors(21))
    # end = time.time()
    # print(end - start)