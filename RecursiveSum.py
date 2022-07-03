def RecursiveSum(num):
    # print(num)
    if num == 0: # base case
        return 0
    else:
        digit = num % 10
        # print(digit)
        num = int(num / 10)
        return digit + RecursiveSum(num)


number = 1234
print(RecursiveSum(number))
