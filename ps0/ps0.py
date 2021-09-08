#################
#               #
# Problem Set 0 #
#               #
#################



#
# Setup
#

class BinaryTree:
    # left : BinaryTree
    # right : BinaryTree
    # key : string
    # temp : int
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key
        self.temp = None

#
# Problem 1
#

# Sets the temp of each node in the tree T
# ... to the size of that subtree
def calculate_size(T):
    # Set the temp for each node in the tree
    # The return value is up to you

    # Your code goes here
    # Base case: T is None
    if T is None:
        return 0
    else:
        T.temp = calculate_size(T.left) + calculate_size(T.right) + 1
        return T.temp


#
# Problem 3
#

# Outputs a subtree subT of T of size in the interval [L,U]
# ... and removes subT from T by replacing the pointer
# ... to subT in its parent with `None`
def FindSubtree(T, L, U):
    # Instructions:
    # Implement your Part 2 proof in O(n)-time
    # The return value is a subtree that meets the constraints

    # Your code goes here
    # Invariants:
    calculate_size(T)
    if T.left is not None and T.left.temp >= L:
        if T.left.temp <= U:
            subT = T.left
            T.left = None
            return subT
        else: return FindSubtree(T.left, L, U)
    elif T.right is not None and T.right.temp >= L:
        if T.right.temp <= U:
            subT = T.right
            T.right = None
            return subT
        else: return FindSubtree(T.right, L, U)
    else: return None
