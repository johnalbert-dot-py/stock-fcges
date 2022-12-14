"""
rotate([3, 8, 9, 7, 6], 3) returns [9, 7, 6, 3, 8]
rotate([0, 0, 0], 1) returns [0, 0, 0]
rotate([1, 2, 3, 4], 4) returns [1, 2, 3, 4]
"""


def rotate(arr, k):
    return arr[-k:] + arr[:-k]


print(rotate([3, 8, 9, 7, 6], 3))
print(rotate([0, 0, 0], 1))
print(rotate([1, 2, 3, 4], 4))
