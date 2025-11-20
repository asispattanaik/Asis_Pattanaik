a = int(input("Enter a number: "))
if a < 1:
    print("Please enter a positive integer.")
else:
    k = a if a % 2 == 1 else a - 1
    odds = [2 * i - 1 for i in range(1, k + 1)]
    print(','.join(map(str, odds)))
