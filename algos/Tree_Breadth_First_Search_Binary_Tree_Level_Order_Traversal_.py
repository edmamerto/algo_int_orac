# Problem Statement #
# Given a binary tree, populate an array to represent its
# level-by-level traversal.
# You should populate the values of all nodes of
# each level from left to right in separate sub-arrays.


# Example 1:

# 	   1
#     / \
#    2   3
#   /\   /\
#  4 5  6  7

# output: [[1],[2,3],[4,5,6,7]]

# Example 2:

#       12
#       / \
#      7   1
#     /    /\
#    9    10 5

# output: [[12],[7,1],[9,10,5]]


from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse(root):
    result = []
    # TODO: Write your code here
    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level order traversal: " + str(traverse(root)))


main()
# ----- end ------
# https://www.educative.io/courses/grokking-the-coding-interview/xV7E64m4lnz


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse(root):
    result = []
    if root is None:
        return result

    queue = deque()
    queue.append(root)
    while queue:
        levelSize = len(queue)
        currentLevel = []
        for _ in range(levelSize):
            currentNode = queue.popleft()
            # add the node to the current level
            currentLevel.append(currentNode.val)
            # insert the children of current node in the queue
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)

        result.append(currentLevel)

    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level order traversal: " + str(traverse(root)))


main()
