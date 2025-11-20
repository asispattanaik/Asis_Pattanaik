def count_multiples(nums):
    result = {}
    for i in range(1, 10):
        count = sum(1 for num in nums if num % i == 0)
        result[i] = count
    return result
nums = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
output = count_multiples(nums)
print(output)
