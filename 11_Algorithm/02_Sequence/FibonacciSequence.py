import time


class FibonacciA():
    def __init__(self, input_number):
        start_time = time.time()
        self.result = self.fib(input_number)
        end_time = time.time()
        self.run_time = end_time-start_time

    def fib(self, n):
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            a = self.fib(n - 1)
            b = self.fib(n - 2)
            return a + b


class FibonacciB:
    def __init__(self, input_number):
        self.memo = {0:0, 1:1}
        start_time = time.time()
        self.result = self.fib(input_number)
        end_time = time.time()
        self.run_time = end_time-start_time

    def fib(self, n):
        if n in self.memo:
            print('cache hit')
            return self.memo[n]
        else:
            print('need to calculate')
            self.memo[n] = self.fib(n-1) + self.fib(n-2)
            return self.memo[n]

if __name__ == "__main__":
    for tmp in range(40, 41):
        a = FibonacciA(input_number=tmp)
        print(tmp, a.result, a.run_time)

        b = FibonacciB(input_number=tmp)
        print(tmp, b.result, b.run_time)
        print()
