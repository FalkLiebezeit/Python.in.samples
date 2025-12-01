import time

def sieve_of_eratosthenes(n):
    prime = [True for _ in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1

    for p in range(2, n+1):
        if prime[p]:
            print(p, end=' ')

def main():
    n = 100000

    start_time = time.time()

    sieve_of_eratosthenes(n)

    end_time = time.time()
    print("\nBerechnungszeit: {:.2f} ms".format((end_time - start_time) * 1000))

if __name__ == "__main__":
    main()
