## IT309-001 Assignment #4 (A4): Linked List Operations and Maintenance
### Daniel Lee
### Due Date: 10.20.2020

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
        print('Removing element')
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

# <!!!>

    # Have to keep a counter variable to count how many nodes you've passed before inserting after the ith one.
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
                #print('Adding # ', self._size, ' element: ', node.getElement())
                self._size += 1
            # if the specified index is within range of the size of the list, insert node in the position.
            elif int(i) < self._size:
                while count < int(i):
                    if count == i:
                        previous_node.next = element
                        element.next = cursor
                        break
                    previous_node = cursor
                    cursor = cursor.getNext()
                    
                    count+=1
                cursor.setNext(node)
                self._size += 1
        print('Inserted ', node.getElement(), 'after index position #', count)
    
    # Have to save the previous and next node pointers as you loop through the list so you can place your new node after the previous or before the next one.
    def insertElt (self, insrtThis, where, insrtHere):
        """Insert element 'insrtThis' before/after node with element =='insrtHere'.
           Parameter 'where' = "B" (before) or "A' (After) 'insrtHere'.        """
        node = self._Node(insrtThis, None)
        # insert method body below
        # Hint: search for the list node element == 'insrtHere', then insert accordingly...'  
        
        if self.isEmpty():
            self._head = node
        else:
            #insrtHere = cursor.getElement()
            if where == 'A':
                cursor = self._head
                # add insrtThis AFTER insrtHere
                while cursor.getNext() is not None:
                    if insrtHere == cursor.getElement():
                        insrtHere = cursor.getElement()
                        break
                    cursor = cursor.getNext()
                cursor.setNext(node)
                self._size += 1
                print('Inserted ', node.getElement(), 'after ', insrtHere)
            elif where == 'B':
                # add insrtThis BEFORE insrtHere
                cursor = self._head
                current_pos = 0
                while cursor.getNext() is not None:
                    if insrtHere == cursor.getElement():
                        previous_node._next = insrtThis
                        cursor = cursor._next
                        #insrtHere = current_node.getElement()
                        print('HELLO WORLD')
                        break
                    previous_node = cursor
                    cursor = cursor._next
                    current_pos+=1
                previous_node.setNext(node)
                self._size += 1
                print('Inserted ', node.getElement(), 'before ', insrtHere) 
        
# </!!!>
class Empty(Exception):
    """Empty exception class provided to flag that condition. """
    pass


# inserts like 'A,Washington' (add) are inserted after the most tail element
# inserts like 'IE,Wilson,A,TRoosevelt' (insertElt) are inserted after or before the second element parameter. In this case, Wilson will be inserted after the TRoosevelt node.
# inserts like 'IA,40,Kennedy' (insertAfter) are inserted in the index specified. if the index value is greater than the number of items on the SLL, the new node will be inserted after the last item and become the new rear/tail.
# insert 'R' (remove) will simply remove the beginning/head node.  

A3trans = ('A,Washington',
           'A,Adams',
           'A,Jefferson',
           'A,Madison',
           'A,Monroe',
           'A,Quincy Adams',
           'A,Jackson',
           'A,Van Buren',
           'A,Harrison',
           'A,Tyler',
           'A,Polk',
           'A,Taylor',
           'A,Fillmore',
           'A,Pierce',
           'A,Buchanan',
           'A,Lincoln',
           'A,AJohnson',
           'A,Grant',
           'A,Hayes',
           'A,Garfield',
           'A,Arthur',
           'A,Cleveland',
           'A,Harrison',
           'A,Cleveland',
           'A,McKinley',
           'A,TRoosevelt',
           'IE,Wilson,A,TRoosevelt',
           'IE,Taft,B,Wilson',
           'A,Coolidge',
           'R',
           'R',
           'R',
           'A,Harding',
           'IE,Wilson,B,Harding',
           'A,Coolidge',
           'A,FDRoosevelt',
           'IE,Hoover,B,FDRoosevelt',
           'IA,2,Shuman',
           'IA,40,Kennedy',
           'A,LBJohnson',
           'IE,Nixon,A,LBJohnson',
           'IE,Eisenhower,B,Kennedy',
           'IE,Truman,B,Eisenhower')

# SLL1 object created
SLL1 = SinglyLinkedList()
for n in A3trans:
    n = n.split(',')
    if n[0] == 'A':
        # adds node to the end of the list
        SLL1.add(n[1])
    elif n[0] == 'IE':
        # inserts n[1] node to before/after (n[2]) the n[3] node
        SLL1.insertElt(n[1],n[2],n[3])
    elif n[0] == 'IA':
        # inserts n[2] node after the node indexed (n[1])  
        SLL1.insertAfter(n[1],n[2])
    elif n[0] == 'R':
        # removes the head node
        SLL1.remove()
    else:
        pass
print(SLL1._size)

SLL1.showList()

print(id(None))

print(int('286A9C25E10', 16))

SLL1.getSize()

SLL1.remove()

SLL1.showList()

SLL1.getSize()

## Observations
### I have found developing and testing the code to be mostly debugging in terms of most time spent.
### I have developed the functions relatively quickly but it was debugging all the functions when running that took the most time.
### I would say on paper handling the SLL is easy. It is easy to have your mind grasp on whats going on.
### But implementing it through code is more tricky than I had imagined. There's a lot of varying characteristic each node, function, and variable has.
### I think I would prefer implementing the linked list using an array because I can visually see more clearly of whats going on.
### I would say the insertElt was more difficult to code than insertAfter. insertElt you have to take in account the previous and next nodes.
### I think the SLL class is suitable for implementing the Queue ADT, because its remove() function pops out the head while its add function inserts to the tail.
### The SLL class functions as a FIFO