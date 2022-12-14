# find_divisible(6,11,2) should return 3. 6, 8, and 10 are all divisible by 2.
# find_divisible(0,12,3) should return 5. 0, 3,6, 9, and 12 are all divisible by 3.


def find_divisible(a, b, k):
    nums = range(a, b + 1)
    return len([num for num in nums if num % k == 0])


print(find_divisible(6, 11, 2))
print(find_divisible(0, 12, 3))
