def average_of_levels(root, averages, level=0):
    if root:
        if len(averages) <= level:
            averages.append([root.val,1])
        else:
            averages[level][0] += root.val
            averages[level][1] += 1
        average_of_levels(root.left, averages, level+1)
        average_of_levels(root.right, averages, level+1)
    return averages

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
averages = average_of_levels(root, [])
for counts in range(len(averages)):
    averages[counts] = averages[counts][0] / averages[counts][1]


print(averages)