def isPrime(n):
    k = int(math.sqrt(n))
    for i in range(2, k + 1):
        if (n % i == 0):
            return False

    return True


# Driver Code Starts.


import math  ##You will need this for prime checking


def main():
    testcases = int(input())
    while testcases > 0:
        number = int(input())
        print(isPrime(number))
        testcases -= 1


if __name__ == "__main__":
    main()