x = int(input("Enter a number: "))
if x < 1:
    print("Please enter a positive integer.")
else:
    odds = [2 * i - 1 for i in range(1, x + 1)]
    print(','.join(map(str, odds)))
