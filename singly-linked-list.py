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
            cursor = cursor.getNext( )
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
    cursor = self._head
    while cursor:
        if key == cursor.getElement():
            return True
        cursor = cursor.getNext()
    return False

#---------------------------------------------------------------------------------
# IT-309 A4 requires you to complete the code for the two methods that follow
#---------------------------------------------------------------------------------

# ^^^^^ SHOULD ONLY BE AROUND 30 LINES OF CODE FOR THESE TWO METHODS COMBINED
# ^^^^^ Review how LINKED STRUCTURES work and OBJECT ID's for pointing elements
# ^^^^^ Textbook pages 255-265 (chapter 7)
  def insertAfter (self, i, element): # 'i' is the 'ith' element, 'element' is the element itself
    """Insert an element after the ith element of the list."""
    node = self._Node(element, None)
  # insert method body below
  # Cases: (1) insert into empty list, (2) insert before the head, (3) insert in the interior

  def insertElt (self, insrtThis, where, insrtHere):
    """Insert element 'insrtThis' before/after node with element =='insrtHere'.
       Parameter 'where' = "B" (before) or "A' (After) 'insrtHere'.        """
    node = self._Node(insrtThis, None)
    # insert method body below
    # Hint: search for the list node element == 'insrtHere', then insert accordingly...'  

class Empty(Exception):
    """Empty exception class provided to flag that condition. """
    pass