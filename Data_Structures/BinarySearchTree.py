from typing import List
class Node:
    '''
    Classe que modela um nó dinâmico de uma árvore binária.
    '''
    def __init__(self, data: tuple):
        '''
        Construtor que inicializa um nó com dados e
        sem filhos.
        
        Parameters
        ----------
        data (tuple): uma tupla contendo o número da sala e o horário da reserva.
        '''
        self.__data = data  # Agora espera uma tupla (room_number, reservation_time)
        self.__left = None
        self.__right = None

    @property
    def data(self) -> tuple:
        return self.__data

    @data.setter
    def data(self, newData: tuple):
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

    def addLeft(self, data: tuple):
        if self.__left is None:
            self.__left = Node(data)

    def hasLeftChild(self) -> bool:
        return self.__left is not None

    def hasRightChild(self) -> bool:
        return self.__right is not None

    def addRight(self, data: tuple):
        if self.__right is None:
            self.__right = Node(data)

    def __str__(self):
        # Representa os dados como uma string formatada
        return f'Room: {self.__data[0]}, Reservation Time: {self.__data[1]}'



        
class BinarySearchTree:
    '''
    Class that models a binary search tree data structure.
    Author: Alex Cunha  
    Date of last modification: 31/10/2023
    Attributes
    ----------
    root (Node): reference to the root node.
    '''
    preorder  = 0
    inorder   = 1
    postorder = 2
    def __init__(self):
        '''
        Initializes the tree with a root node.
        '''
        self.__root = None

    def getRoot(self)->any:
        '''
        Gets the data stored in the root node.
        '''
        return self.__root.data if self.__root is not None else None

    def isEmpty(self)->bool:
        '''
        Checks if the tree is empty.
        '''
        return self.__root == None

    def height(self)->int:
        '''
        Returns the height of the tree.
        -1 if the tree is empty. The root node has height 0.
        '''
        return self.__height(self.__root)
    
    def __height(self, root:Node)->int:
        if root is None:
            return -1
        else:
            return 1 + max(self.__height(root.left), self.__height(root.right))

    def add(self, room_number: any, reservation_time: any):
        '''
        Adds a new node to the tree with room number and reservation time.
        
        Parameters
        ----------
        room_number (any): the room number to be stored in the new node.
        reservation_time (any): the reservation time to be stored in the new node.
        '''
        if self.__root is None:
            self.__root = Node((room_number, reservation_time))  # Armazena ambos os dados
        else:
            self.__add((room_number, reservation_time), self.__root)

    def __add(self, data: tuple, node: 'Node'):
        if data[0] < node.data[0]:  # Compare apenas room_number
            if node.left is not None:
                self.__add(data, node.left)
            else:
                node.addLeft(data)
        else:
            if node.right is not None:
                self.__add(data, node.right)
            else:
                node.addRight(data)

    
    def search(self, key: any) -> any:
        if self.__root is not None:
            node = self.__searchData(key, self.__root)
            return node.data if node is not None else None
        return None

    def __searchData(self, key, node):
        if node is None:
            return None
        elif key < node.data[0]:  # Aqui você verifica apenas o número da sala
            return self.__searchData(key, node.left)
        elif key > node.data[0]:
            return self.__searchData(key, node.right)
        else:
            return node  # Retorna o nó encontrado


    # Returns the number of nodes of the tree
    def __len__(self)->int:
        '''
        Counts the number of nodes in the tree.
        '''
        return self.__count(self.__root)

    def __count(self, node:'Node'):
        if ( node == None):
            return 0
        else:
            return 1 + self.__count(node.left) + self.__count(node.right)


    def in_order_traversal(self):
        return self.__inorder(self.__root)

    def __inorder(self, node):
        # Método auxiliar para realizar o caminhamento em ordem
        if node is None:
            return []
        return self.__inorder(node.left) + [(node.key, node.data)] + self.__inorder(node.right)

    def traversal(self, order: int = None):
        if order is None or order == self.__class__.preorder:
            self.__preorder(self.__root)
        elif order == self.__class__.inorder:
            return self.__inorder(self.__root)  # Aqui retornamos os valores
        elif order == self.__class__.postorder:
            self.__postorder(self.__root)
        else:
            raise ValueError('Invalid order value')
        print()

    def __preorder(self, node):
        if( node != None):
            print(f'{node.data} ',end='')
            self.__preorder(node.left)
            self.__preorder(node.right)


    def __postorder(self, node):
        if( node != None):
            self.__postorder(node.left)
            self.__postorder(node.right)
            print(f'{node.data} ',end='')

    def clear(self):
        '''
        Deletes all nodes of the tree.
        '''
        # garbage collector will do the work of removing the nodes automatically.
        self.__root = None

 
    def delete(self, key:any)->'Node':
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
        node = self.__searchData(key,self.__root)
        if node is not None:
            self.__root = self.__deleteNode(self.__root, key)
            return node.data
        else:
            return None
        
    
    def __deleteNode(self,root:'Node', key:any):
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
        elif(key > root.data):
            root.right = self.__deleteNode(root.right, key) 
  
        # If key is same as root's key, then this is the node to be deleted
        else:
            # (1) Node with only one child or no child
            if root.left is None : 
                temp = root.right  
                root = None 
                return temp

            elif root.right is None :
                temp = root.left  
                root = None
                return temp 
  
            # (2) Node with two children: Get the inorder successor
            # (smallest in the right subtree)
            temp = self.__minValueNode(root.right) 
  
            # Copy the inorder successor's content to this node
            root.data = temp.data 
  
            # Delete the inorder successor
            root.right = self.__deleteNode(root.right , temp.data)

        return root


    def __minValueNode(self, node:'Node')->'Node':
        '''
        Returns the node with the minimum key value found in the tree.
        Note that the entire tree does not need to be searched.
        Arguments
        ---------
        node (Node): the node that is the root of the search.   
        '''
        current = node 
  
        # Loop down to find the leftmost leaf
        while(current.left is not None): 
            current = current.left  
  
        return current

    def __maxValueNode(self, node:'Node')->'Node':
        '''
        Returns the node with the maximum key value found in the tree.
        Note that the entire tree does not need to be searched.
        Arguments
        ---------
        node (Node): the node that is the root of the search.
        '''
        current = node 
  
         # loop down to find the rightmost leaf
        while(current.right is not None): 
            current = current.right
  
        return current

    def __str__(self)->str:
        '''
        Returns a string representation of the tree in preorder traversal.
        '''
        return self.__preorderToStr(self.__root)[:-2]

    def __preorderToStr(self, root)->str:
        '''
        Returns a string representation of the tree in preorder traversal.
        Arguments
        ---------
        root (Node): the node that is the root of the traverse.
        '''
        if (root is None):
            return ''
    
        result = f'{root.data} | '
        result += self.__preorderToStr(root.left)
        result += self.__preorderToStr(root.right)
        return result

    def treeview(self):
        '''
        Displays the tree in a visual way, in order to understand where
        nodes were inserted.
        Note: call this method only for small trees.
        '''
        if self.__root is None:
            return
        lines, *_ = self.__visual(self.__root)
        for line in lines:
            print(line)

    def __visual(self, node):
        """
        Returns list of strings, width, height, and horizontal coordinate
        of the root.
        """
        # No child.
        if node.right is None and node.left is None:
            line = f'{node.data}'
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if node.right is None:
            lines, n, p, x = self.__visual(node.left)
            s = f'{node.data}'
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if node.left is None:
            lines, n, p, x = self.__visual(node.right)
            s = f'{node.data}'
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x  = self.__visual(node.left)
        right, m, q, y = self.__visual(node.right)
        s = f'{node.data}'
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2     
    
    def build(self,values:List[any]):
        '''
        Builds a binary search tree in the order the values appear in
        the list.        
        Precondition: the tree must be empty

        Arguments
        ---------
        values (List[any]): the list of values to be inserted in 
        the tree.
        '''
        if not values or self.__root != None:
            return None 

        for element in values:
            self.add(element)
    
    def balance(self):
        '''
        Balances the tree.
        '''
        nodes = []
        self.__saveToArray(self.__root, nodes)
        self.__root =  self.__rebuild(nodes, 0, len(nodes) - 1)

    def __saveToArray(self, root:Node,nodes:List[Node]):   
        '''
        A recursive method to get an array of nodes in inorder
        traversal of a given binary tree.
        Arguments
        ---------
        root (Node): the node of the tree.
        nodes (List[Node]): the list that stores the nodes visited
        in inorder traversal.
        Note
        ----
        Method of suport to the method __rebuild().
        '''         
        if not root:  # Base case
            return
        
        # Store nodes in Inorder traversal
        self.__saveToArray(root.left,nodes)
        nodes.append(root)
        self.__saveToArray(root.right,nodes)          

    def __rebuild(self, sorted_list:List[Node],start_index:int,end_index:int):
        '''
        A recursive method to rebuild the BST from a sorted array in
        order to balance it.
        The method computes the middle element of the list and makes it
        the root. Then, it recursively builds the left and right subtrees
        calling itself for the left and right parts of the list.


        Arguments
        ---------
        sorted_list (List[Node]): the list of nodes in inorder traversal.
        start_index (int): the start index of the list.
        end_index (int): the end index of the list.
        Note
        ----
        Method of suport to the public method balance().
        '''        
        if start_index>end_index: # base case 
            return None
    
        # Get the middle element and make it root 
        middle_index=(start_index + end_index)//2
        no = sorted_list[middle_index]
    
        # Using index in Inorder traversal, construct left and right subtress
        no.left = self.__rebuild(sorted_list,start_index,middle_index-1)
        no.right= self.__rebuild(sorted_list,middle_index+1,end_index)
        return no 

    def __iter__(self):
        '''
        Allow the tree to be iterated in preorder traversal.
        '''
        self.__stack = [self.__root]
        return self

    def __next__(self):
        '''
        Returns the next node in the iteration.
        '''
        if not self.__stack:
            raise StopIteration
        node = self.__stack.pop()
        if node.right:
            self.__stack.append(node.right)
        if node.left:
            self.__stack.append(node.left)
        return node.data
    
    def __contains__(self, key:any)->bool:
        '''
        Verifies if a key is present in the tree.
        Method is called when the operator "in" is used.
        '''
        value = self.search(key)
        return True if value else None

    

    
