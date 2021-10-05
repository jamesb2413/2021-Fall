from ps3 import BinarySearchTree

def multi_getattr(obj, attr, default=None):
    """
    Get a named attribute from an object; multi_getattr(x, 'a.b.c.d') is
    equivalent to x.a.b.c.d. When a default argument is given, it is
    returned when any attribute in the chain doesn't exist; without
    it, an exception is raised when a missing attribute is encountered.

    """
    attributes = attr.split(".")
    for i in attributes:
        try:
            obj = getattr(obj, i)
        except AttributeError:
            return default
    return obj

def construct_tree_example():
    T = BinarySearchTree()
    T.key = 4
    T.insert(2)
    T.insert(6)
    T.insert(3)
    T.insert(-1)
    T.insert(80)
    T.insert(60)
    T.insert(100)
    T.insert(70)

    # T.print_bst()
    return T

def construct_tree_example_2():
    T = BinarySearchTree()
    T.key = 4
    T.insert(2)
    T.insert(3)
    T.insert(6)
    T.insert(-1)
    T.insert(60)
    T.insert(70)
    T.insert(80)
    T.insert(100)

    # T.print_bst()
    return T
#full tree
def construct_tree_example_3():
    T = BinarySearchTree()
    T.key = 10
    T.insert(5)
    T.insert(15)
    T.insert(2)
    T.insert(1)
    T.insert(4)
    T.insert(3)
    T.insert(7)
    T.insert(6)
    T.insert(8)
    T.insert(9)
    T.insert(13)
    T.insert(11)
    T.insert(14)
    T.insert(12)
    T.insert(17)
    T.insert(16)
    T.insert(18)
    T.insert(20)
    T.insert(19)

    return T

def construct_tree_example_4():
    T = BinarySearchTree()
    T.key = 10
    T.insert(5)
    T.insert(15)
    T.insert(2)
    T.insert(1)
    T.insert(7)
    T.insert(6)
    T.insert(8)
    T.insert(9)
    T.insert(13)
    T.insert(11)
    T.insert(14)
    T.insert(12)
    T.insert(17)
    T.insert(16)
    T.insert(18)
    T.insert(20)
    T.insert(19)

    return T
