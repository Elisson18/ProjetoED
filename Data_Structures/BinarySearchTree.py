from typing import List

class Node:
    '''
    Classe that models a dinamic node of a binary tree.
    '''
class Node:
    def __init__(self, data: object, key):
        '''
        Constructor that initializes a node with data and a key,
        and sets the left and right children to None.
        '''
        self.__data = data 
        self.__key = key    
        self.__left = None 
        self.__right = None 

    @property
    def data(self) -> object:
        return self.__data

    @data.setter
    def data(self, newData: object):
        self.__data = newData

    @property
    def left(self) -> 'Node':
        return self.__left

    @left.setter
    def left(self, newleft: 'Node'):
        self.__left = newleft

    @property
    def right(self) -> 'Node':
        return self.__right

    @right.setter
    def right(self, newRightChild: 'Node'):
        self.__right = newRightChild

    def addLeft(self, data: object):
        if self.__left is None:
            self.__left = Node(data)

    def hasLeftChild(self) -> bool:
        return self.__left is not None

    def hasRightChild(self) -> bool:
        return self.__right is not None

    def addRight(self, data: object):
        if self.__right is None:
            self.__right = Node(data)

    def __str__(self):
        return f'{self.__data}'


class BinarySearchTree:
    '''
    Class that models a binary search tree data structure.
    Author: Alex Cunha  
    Date of last modification: 31/10/2023
    Attributes
    ----------
    root (Node): reference to the root node.
    '''
    preorder = 0
    inorder = 1
    postorder = 2

    def __init__(self):
        '''
        Initializes the tree with a root node.
        '''
        self.__root = None

    def getRoot(self) -> any:
        '''
        Gets the data stored in the root node.
        '''
        return self.__root.data if self.__root is not None else None

    def isEmpty(self) -> bool:
        '''
        Checks if the tree is empty.
        '''
        return self.__root is None

    def height(self) -> int:
        '''
        Returns the height of the tree.
        -1 if the tree is empty. The root node has height 0.
        '''
        return self.__height(self.__root)

    def __height(self, root: Node) -> int:
        if root is None:
            return -1
        else:
            return 1 + max(self.__height(root.left), self.__height(root.right))


    def add(self, data: any, key: any) -> None:
        """
        Adds a new node to the tree.
        
        Parameters
        ----------
        data (any): the data to be stored in the new node.
        key: the key associated with the data for the node.
        """
        if self.__root is None:
            self.__root = Node(data, key)
        else:
            self.__add(data, key, self.__root)

    def __add(self, data: any, key: any, node: Node) -> None:
        if key < node.get_key():
            if node.get_left() is not None:
                self.__add(data, key, node.get_left())
            else:
                node.add_left(data, key)
        else:
            if node.get_right() is not None:
                self.__add(data, key, node.get_right())
            else:
                node.add_right(data, key)

    def search(self, key: any) -> any:
        '''
        Perform a search in the tree for a node with the given key.
        Returns
        -------
        data (any): the data stored in the node corresponding to the key.
        None: if the key is not found in the tree.
        '''
        if self.__root is not None:
            node = self.__searchData(key, self.__root)
            return node.data if node is not None else None
        else:
            return None

    def __searchData(self, key: any, node: 'Node'):
        if key == node.data:
            return node
        elif key < node.data and node.left is not None:
            return self.__searchData(key, node.left)
        elif key > node.data and node.right is not None:
            return self.__searchData(key, node.right)
        else:
            return None

    # Returns the number of nodes of the tree
    def __len__(self) -> int:
        '''
        Counts the number of nodes in the tree.
        '''
        return self.__count(self.__root)

    def __count(self, node: 'Node'):
        if node is None:
            return 0
        else:
            return 1 + self.__count(node.left) + self.__count(node.right)

    def traversal(self, order: int = None):
        '''
        Print the nodes of the in pre-order, in-order or post-order traversal.
        Arguments
        ---------
        order (int): the order of traversal. The possible values are:
        preorder, inorder, postorder. If no order is given, the traversal
        is performed in pre-order.
        '''
        if order is None:
            self.__preorder(self.__root)
        elif order == self.__class__.preorder:
            self.__preorder(self.__root)
        elif order == self.__class__.inorder:
            self.__inorder(self.__root)
        elif order == self.__class__.postorder:
            self.__postorder(self.__root)
        else:
            raise ValueError('Invalid order value')
        print()

    def __preorder(self, node):
        if node is not None:
            print(f'{node.data} ', end='')
            self.__preorder(node.left)
            self.__preorder(node.right)

    def __inorder(self, node):
        if node is not None:
            self.__inorder(node.left)
            print(f'{node.data} ', end='')
            self.__inorder(node.right)

    def __postorder(self, node):
        if node is not None:
            self.__postorder(node.left)
            self.__postorder(node.right)
            print(f'{node.data} ', end='')

    def clear(self):
        '''
        Deletes all nodes of the tree.
        '''
        # garbage collector will do the work of removing the nodes automatically.
        self.__root = None

    def delete(self, key: any) -> 'Node':
        '''
        Deletes a node with the given key and returns its data.
        Arguments
        ---------
        key (any): the key used to find the node to be deleted.
        Returns
        -------
        data (any): the data corresponding to the key node. If the key is not found
        return None.
        '''
        if self.__root is None:
            return None
        node = self.__searchData(key, self.__root)
        if node is not None:
            self.__root = self.__deleteNode(self.__root, key)
            return node.data
        else:
            return None

    def __deleteNode(self, root: 'Node', key: any):
        '''
        Deletes a node with the given key and returns the new root node.
        Arguments
        ---------
        root (Node): the node that is the root of the search.
        key (any): the key used to find the node to be deleted.
        '''
        # Primary case: there is no root
        if root is None:
            return root

        # If the key to be deleted is smaller than the root's key
        # then it lies in left subtree
        if key < root.data:
            root.left = self.__deleteNode(root.left, key)

        # If the key to be deleted is greater than the root's key,
        # then it lies in right subtree
        elif key > root.data:
            root.right = self.__deleteNode(root.right, key)

        # If key is same as root's key, then this is the node to be deleted
        else:
            # (1) Node with only one child or no child
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            # (2) Node with two children: Get the inorder successor
            # (smallest in the right subtree)
            temp = self.__minValueNode(root.right)

            # Copy the inorder successor's content to this node
            root.data = temp.data

            # Delete the inorder successor
            root.right = self.__deleteNode(root.right, temp.data)

        return root

    def __minValueNode(self, node: 'Node') -> 'Node':
        '''
        Returns the node with the minimum key value found in the tree.
        Note that the entire tree does not need to be searched.
        Arguments
        ---------
        node (Node): the node that is the root of the search.   
        '''
        current = node

        # Loop down to find the leftmost leaf
        while current.left is not None:
            current = current.left

        return


    