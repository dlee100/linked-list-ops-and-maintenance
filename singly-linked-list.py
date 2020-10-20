class SinglyLinkedList:
    """LIFO Stack implementation using a singly linked list for storage."""

 #-------------------------- nested _Node class --------------------------
    class _Node:         # "inner" class
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'           # streamline memory usage

        def __init__(self, element, next):        # initialize node's fields
            self._element = element               # reference to user's element
            self._next = next                     # reference to next node

        def setNext(self, next):
            self._next = next
    
        def getNext(self):
            return self._next
  
        def setElement(self, element):
            self.element = _element
    
        def getElement(self):
            return self._element
        
  #------------------------------- stack methods -------------------------------
    def __init__(self, head = None, size = 0):
        """Create an empty list."""
        self._head = head                       # reference to the head node
        self._size = size                       # number of stack elements

    def getSize(self):
        """Return the number of elements in the list."""
        return self._size

    def isEmpty(self):
        """Return True if the list is empty."""
        return self._size == 0

    def add (self, element):
        """Add element element to the end of the list."""
        node = self._Node(element, None)
        if self.isEmpty():
            self._head = node
        else:
            cursor = self._head
            while cursor.getNext() is not None:
                cursor = cursor.getNext()
            cursor.setNext(node)
        print('Adding # ', self._size, ' element: ', node.getElement())
        self._size += 1
        
    def remove(self):
        """Remove the element at the head of the list. Raise Empty if the list is empty."""
        if self.isEmpty():
            raise Empty('List is empty')
        self._size -= 1
        out = self._head.getElement()      # save the head element and return to the caller
        self._head = self._head.getNext()  # Reset the head to the second (next) list element
        return out

    def showList(self):
        """Display the contents of the list, from head to tail. Raise Empty exception if the List is empty. """
        if not self.isEmpty():
            cursor = self._head
            while True:
                print(cursor.getElement(), ' reference: ', id(cursor), id(cursor.getNext()))
                if cursor.getNext() == None: break
                cursor = cursor.getNext()
        return
        
    def search(self, key):
        """ Search the list using 'key. """        
        cursor = self._head #'cursor' is the node pointer, starting at the list head.
        while cursor: #loop until cursor is 'None', the list tail was reached.
            if key == cursor.getElement(): #is the node element equal to the 'key' search target?
                return True
            cursor = cursor.getNext() #point to the next node by setting cursor to next.
        return False

#"""The above searches the SLL one node at a time, starting with the head, until it finds a node whose element (data or key) equals the parameter 'key' value or it reaches the node after the tail, which is 'None'.  Lines 3, 4, and 7 are the way you loop through the list.  I've added some comments to help you understand what's going on, but the code itself was provided with the assignment as a Jupyter notebook file.  Copy it in and start from there if you haven't already done it.   """
#"""Remember that a pointer ('cursor' in the above code) is the object reference - the long number representing the place in storage where the object's data is kept.  Each node is located at a difference place and is usually not in consecutive locations.  How to follow and manipulate these pointers is the thing I'm trying to get across here. """
#"""For 'insertAfter' you have to keep a counter variable to count how many nodes you've passed before inserting after the ith one.  For 'insertElt' you have to save the previous and next node pointers as you loop through the list so you can place your new node after the previous or before the next one.  """

#---------------------------------------------------------------------------------
# IT-309 A4 requires you to complete the code for the two methods that follow
#---------------------------------------------------------------------------------

# ^^^^^ SHOULD ONLY BE AROUND 30 LINES OF CODE FOR THESE TWO METHODS COMBINED
# ^^^^^ Review how LINKED STRUCTURES work and OBJECT ID's for pointing elements
# ^^^^^ Textbook pages 255-265 (chapter 7)
# <!!!>

    # You have to keep a counter variable to count how many nodes you've passed before inserting after the ith one.
    def insertAfter (self, i, element):
        node = self._Node(element, None)
        #i = int
        if self.isEmpty():
            self._head = node
        else:
            cursor = self._head #'cursor' is the node pointer, starting at the list head.
            count = 0
            # if the specified index is greater than the size of the list, add the node to the end of the list.
            if int(i) >= self._size: # same function as add()
                while cursor.getNext() is not None:
                    count+=1
                    cursor = cursor.getNext()
                cursor.setNext(node)
                print('Adding # ', self._size, ' element: ', node.getElement())
                self._size += 1
            elif int(i) < self._size:
                while int(i) != count:
                    count+=1
                    cursor = cursor.getNext() #goes to the next node
                cursor.setNext(node)
                #print('Adding # ', self._size, ' element: ', node.getElement())
                self._size += 1
            #count+=1
        print('Inserted ', node.getElement(), 'after index position #', count)
    
    # You have to save the previous and next node pointers as you loop through the list so you can place your new node after the previous or before the next one.
    def insertElt (self, insrtThis, where, insrtHere):
        """Insert element 'insrtThis' before/after node with element =='insrtHere'.
           Parameter 'where' = "B" (before) or "A' (After) 'insrtHere'.        """
        node = self._Node(insrtThis, None)
        # insert method body below
        # Hint: search for the list node element == 'insrtHere', then insert accordingly...'  
        
        if self.isEmpty():
            self._head = node
        else:
            cursor = self._head
            #insrtHere = cursor.getElement()
            if where == 'A':
                # add insrtThis AFTER insrtHere
                while cursor.getNext() is not None:
                    if insrtHere == cursor.getElement():
                        insrtHere = cursor.getElement()
                        pass
                    cursor = cursor.getNext()
                    print('iterating ... ')
                cursor.setNext(node)
                self._size += 1
                print('Inserted ', node.getElement(), 'after ', insrtHere)
            elif where == 'B':
                # add insrtThis BEFORE insrtHere
                
                while cursor.getNext() is not None:
                    if insrtHere == cursor.getElement():
                        insrtHere = cursor.getElement()
                        pass
                    cursor = cursor.getNext()
                    print('iterating ... ')
                cursor.
                self._size += 1
                print('Inserted ', node.getElement(), 'before ', insrtHere)
            else:
                pass
        
    
    
    
    
    
        
# </!!!>
class Empty(Exception):
    """Empty exception class provided to flag that condition. """
    pass