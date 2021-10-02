class BinarySearchTree:
    # left: BinarySearchTree
    # right: BinarySearchTree
    # key: string
    # size: int
    def __init__(self, debugger = None):
        self.left = None
        self.right = None
        self.key = None
        self.item = None
        self._size = 1
        self.debugger = debugger

    @property
    def size(self):
         return self._size

     # a setter function
    @size.setter
    def size(self, a):
        debugger = self.debugger
        if debugger:
            debugger.inc_size_counter()
        self._size = a

    ####### Problem 1 #######
    '''
    Calculates the size of the tree
    returns the size at a given node
    '''
    def calculate_sizes(self, debugger = None):
        # Debugging code
        # No need to modify
        # Provides counts
        if debugger is None:
            debugger = self.debugger
        if debugger:
            debugger.inc()

        # Implementation
        self.size = 1
        if self.right is not None:
            self.size += self.right.calculate_sizes(debugger)
        if self.left is not None:
            self.size += self.left.calculate_sizes(debugger)
        return self.size

    '''
    Select the ind-th key in the tree

    ind: a number between 0 and n-1 (the number of nodes/objects)
    returns BinarySearchTree/Node or None
    '''
    def select(self, ind):
        left_size = 0
        if self.left is not None:
            left_size = self.left.size
        if ind == left_size:
            return self
        if left_size > ind and self.left is not None:
            return self.left.select(ind)
        if left_size < ind and self.right is not None:
            return self.right.select(ind -(left_size+1))
        return None


    '''
    Searches for a given key
    returns a pointer to the object with target key or None (Roughgarden)
    '''
    def search(self, key):
        if self is None:
            return None
        elif self.key == key:
            return self
        elif self.key < key and self.right is not None:
            return self.right.search(key)
        elif self.left is not None:
            return self.left.search(key)
        return None


    '''
    Inserts a key into the tree

    key: the key for the new node;
        ... this is NOT a BinarySearchTree/Node, the function creates one

    returns the original (top level) tree - allows for easy chaining in tests
    '''
    def insert(self, key):
        if self.key is None:
            self.key = key
            return self
        self.size += 1
        if self.key > key:
            if self.left is None:
                self.left = BinarySearchTree(self.debugger)
            self.left.insert(key)
        elif self.key < key:
            if self.right is None:
                self.right = BinarySearchTree(self.debugger)
            self.right.insert(key)
        return self


    ####### Problem 2 #######

    '''
    Deletes a key from the tree
    Returns the root of the tree or None if the tree has no nodes
    '''

    def get_pred(self, parent):
        pred = self.left
        while pred.right is not None:
            pred.size -= 1
            parent = pred
            pred = pred.right
        return pred, parent

    # swaps data from delete node and predecessor
    def pred_swap(self, pred):
        k_i_tmp = self.key, self.item
        self.key = pred.key
        self.item = pred.item
        pred.key = k_i_tmp[0]
        pred.item = k_i_tmp[1]
        return pred

    # searches for delete node and decrements sizes on the path
    # returns delete node, parent tuple
    def search_dec(self, key, parent):
        self.size -= 1
        if self.key == key:
            return self, parent
        elif key > self.key:
            return self.right.search_dec(key, self)
        else:
            return self.left.search_dec(key, self)

    # def delete(self, key):
    #     if self is None:
    #         return None
    #     if self.search(key) is None:
    #         return self
    #     # del: tuple (<node to delete>, <parent>)
    #     del_node, del_parent = self.search_dec(key, None)
    #     # Two children
    #     if del_node.left is not None and del_node.right is not None:
    #         # Find greatest predecessor and swap data
    #         del_node.pred_swap(del_node.get_pred())
    #         # Delete swapped node
    #         if del_parent is None:
    #             return del_node.delete(key)
    #         elif del_parent.left is del_node:
    #             del_parent.left = del_node.delete(key)
    #         else:
    #             del_parent.right = del_node.delete(key)
    #     else:
    #         # delete node is the root
    #         if del_parent is None:
    #             # No children
    #             if del_node.left is None and del_node.right is None:
    #                 self = None
    #             # Left child
    #             elif del_node.right is None and del_node.left is not None:
    #                 self = del_node.left
    #             # Right child
    #             else:
    #                 self = del_node.right
    #         # delete node is left subtree of parent
    #         elif del_parent.left is del_node:
    #             # No children
    #             if del_node.left is None and del_node.right is None:
    #                 del_parent.left = None
    #             # Left child
    #             elif del_node.right is None and del_node.left is not None:
    #                 del_parent.left = del_node.left
    #             # Right child
    #             else:
    #                 del_parent.left = del_node.right
    #         # delete node is right subtree of parent
    #         else:
    #             # No children
    #             if del_node.left is None and del_node.right is None:
    #                 del_parent.right = None
    #             # Left child
    #             elif del_node.right is None and del_node.left is not None:
    #                 del_parent.right = del_node.left
    #             # Right child
    #             else:
    #                 del_parent.right = del_node.right
    #     return self

    def delete(self, key):
        if self is None:
            return None
        if self.search(key) is None:
            return self
        del_node, del_parent = self.search_dec(key, None)
        # Two children
        if del_node.left is not None and del_node.right is not None:
            # Find greatest predecessor and swap data
            pred, d_par2 = del_node.get_pred(del_node)
            d_node2 = del_node.pred_swap(pred)
            # Delete swapped node
            if d_par2.left is d_node2:
                d_par2.left = None
            else:
                d_par2.right = None
        else:
            # delete node is the root
            if del_parent is None:
                # no children
                if del_node.left is None and del_node.right is None:
                    return None
                # left child
                elif del_node.right is None and del_node.left is not None:
                    return del_node.left
                # right child
                else:
                    return del_node.right
            # delete node is left subtree of parent
            elif del_parent.left is del_node:
                # No children
                if del_node.left is None and del_node.right is None:
                    del_parent.left = None
                # Left child
                elif del_node.right is None and del_node.left is not None:
                    del_parent.left = del_node.left
                # Right child
                else:
                    del_parent.left = del_node.right
            # delete node is right subtree of parent
            else:
                # No children
                if del_node.left is None and del_node.right is None:
                    del_parent.right = None
                # Left child
                elif del_node.right is None and del_node.left is not None:
                    del_parent.right = del_node.left
                # Right child
                else:
                    del_parent.right = del_node.right
        return self

    '''
    Performs a `direction`-rotate the `side`-child of (the root of) T (self)

    direction: "L" or "R" to indicate the rotation direction
    child_side: "L" or "R" which child of T to perform the rotate on

    Returns: the root of the tree/subtree

    Example:

    Original Graph
      10
       \
        11
          \
           12

    Execute: NodeFor10.rotate("R", "L") -> Outputs: NodeFor10

    Output Graph
      10
        \
        12
        /
       11
    '''
    def left_rotate(self):
        # save relevant nodes and sizes
        left = self
        rootSize = self.size
        llExists = 0
        lrExists = 0
        leftRight = self.right.left
        if self.left is not None:
            llSize = self.left.size
            llExists = 1
        if self.right.left is not None:
            lrSize = leftRight.size
            lrExists = 1
        # set pointers and adjust sizes
        self = self.right
        self.size = rootSize
        self.left = left
        self.left.right = leftRight
        if lrExists and llExists:
            self.left.size = llSize + lrSize + 1
        elif lrExists:
            self.left.right = leftRight
            self.left.size = lrSize + 1
        elif llExists:
            self.left.size = llSize + 1
        else:
            self.left.size = 1
        return self

    def right_rotate(self):
        # save relevant nodes and sizes
        right = self
        rootSize = self.size
        rrExists = 0
        rlExists = 0
        rightLeft = self.left.right
        if self.right is not None:
            rrSize = self.right.size
            rrExists = 1
        if self.left.right is not None:
            rlSize = rightLeft.size
            rlExists = 1
        # set pointers and adjust sizes
        self = self.left
        self.size = rootSize
        self.right = right
        self.right.left = rightLeft
        if rlExists and rrExists:
            self.right.size = rrSize + rlSize + 1
        elif rlExists:
            self.right.left = rightLeft
            self.right.size = rlSize + 1
        elif rrExists:
            self.right.size = rrSize + 1
        else:
            self.right.size = 1
        return self

    # Return tree with rotated node as root
    def rotate(self, direction, child_side):
        if direction == 'L':
            # left-rotate left-child
            if child_side == 'L':
                self.left = self.left.left_rotate()
            # left-rotate right-child
            else:
                self.right = self.right.left_rotate()
        else:
            # right-rotate left-child
            if child_side == 'L':
                self.left = self.left.right_rotate()
            # right-rotate right-child
            else:
                self.right = self.right.right_rotate()
        return self

    def print_bst(self):
        if self.left is not None:
            self.left.print_bst()
        print( self.key),
        if self.right is not None:
            self.right.print_bst()
        return self

def printBTree(node, spaces=0, child=""):
    if node is None:
        return ""
    else:
        for i in range(spaces):
            print(" ", end="")
        print(child + str(node.key))
        spaces += 2
        printBTree(node.left, spaces, "L")
        printBTree(node.right, spaces, "R")

def construct_tree_example():
    T = BinarySearchTree()
    T.key = 4
    T.insert(2)
    T.insert(6)
    T.insert(3)
    T.insert(1)
    T.insert(80)
    T.insert(60)
    # T.print_bst()
    return T

bst = construct_tree_example()
printBTree(bst)
bst.delete(2)
printBTree(bst)

# llRot = bst.rotate("L", "L")
# print(llRot.key)
# print(llRot.left.key)
# print(llRot.right.key)
# printBTree(llRot)
