nums = [int(num) for num in list(input())]

print(sorted(nums, key=lambda x: x % 3))
