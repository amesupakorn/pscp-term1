"""FibonacciRecursionV1"""
def main(num):
    """FibonacciRecursionV1"""
    if num not in (0, 1):
        return main(num-1) + main(num-2) 
    else:
        return num
print(main(int(input())))
