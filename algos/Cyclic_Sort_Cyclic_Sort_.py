# Problem Statement #
# We are given an array containing n objects.
# Each object, when created, was assigned a unique number
# from 1 to n based on their creation sequence.
# This means that the object with sequence number 3 was created just
# before the object with sequence number 4.

# Write a function to sort the objects in-place on their creation sequence number in O(n)O(n) and without any extra space.
# For simplicity, let’s assume we are passed an integer array containing
# only the sequence numbers, though each number is actually an object.

# Example 1:

# Input: [3, 1, 5, 4, 2]
# Output: [1, 2, 3, 4, 5]
# Example 2:

# Input: [2, 6, 4, 3, 1, 5]
# Output: [1, 2, 3, 4, 5, 6]
# Example 3:

# Input: [1, 5, 6, 4, 3, 2]
# Output: [1, 2, 3, 4, 5, 6]

# ----- end ------

def cyclic_sort(nums):
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]  # swap
        else:
            i += 1
    return nums


def main():
    print(cyclic_sort([3, 1, 5, 4, 2]))
    print(cyclic_sort([2, 6, 4, 3, 1, 5]))
    print(cyclic_sort([1, 5, 6, 4, 3, 2]))


main()

"""
*notes

if input is range 1 to n then we can use this fact to efficiently sort the array

[1, 2, 3]
 0  1  2

remember this formula, if current iteration is in proper place, this is always true

j = nums[i]-1

nums[i] == nums[nums[j] #j

if current iteration is not in its proper place, swapping them out would put current item to its proper place

[3, 1, 2]
 0  1  2

nums[i], nums[j] = nums[j], nums[i]

---> [2, 1, 3]

this check can also work 
if nums[i] != i+1:
"""
