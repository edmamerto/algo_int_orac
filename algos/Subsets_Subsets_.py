# Problem Statement #
# Given a set with distinct elements, find all of its distinct subsets.

# Example 1:

# Input: [1, 3]
# Output: [], [1], [3], [1,3]
# Example 2:

# Input: [1, 5, 3]
# Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3]
# ----- end ------

# https://www.educative.io/courses/grokking-the-coding-interview/gx2OqlvEnWG

def find_subsets(nums):
    subsets = []
    # start by adding the empty subset
    subsets.append([])
    for currentNumber in nums:
        # we will take all existing subsets and insert the current number in
        # them to create new subsets
        n = len(subsets)
        for i in range(n):
            # create a new subset from the existing subset and insert the
            # current element to it
            set = list(subsets[i])
            set.append(currentNumber)
            subsets.append(set)

    return subsets


def main():

    print("Here is the list of subsets: " + str(find_subsets([1, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))


main()

# notes
# Since, in each step, the number of subsets doubles as we add each element to all the existing subsets, therefore, we will have a total of O(2^N)
# And since we construct a new subset from an existing set, therefore, the time complexity of the above algorithm will be O(N*2^N)