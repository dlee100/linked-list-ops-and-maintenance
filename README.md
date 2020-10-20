# IT309_A4
In this assignment you are to modify the SinglyLinkedListADT class provided to you by (1) adding two methods to the class and then (2) by reading and processing a stream of list transactions that add, insert, and remove from a linked list created as an object of the SinglyLinkedList(with your added methods), hereafter referred to using the abbreviation SLL.

The methods to be added:
1.  insertAfter takes two parameters, an integer index (0 and higher) and a string value, creates a new node object with the string value as the new node’s element, and inserts that node object after the ith element of the SLL.  For the purpose of this method the items of the SLLare numbered starting with 1, not 0.  If the value of the index is greater than the number of items in the SLLthe new node isto be inserted after the last item (after the rear or tail) and becomes the new rear or tail.
2.  insertElt takes three parameters: (1) a string value used as the element for a newly created node (NN) object that is to be inserted into the SLL, (2) an indicator (“B” or “A”) specifying whether the NN is to be inserted before or after a specified SLL node, and (3) a string valueof the element of a node (EN) already in the SLL (maybe)before or after which the NN will be inserted.  If the string value in parameter(3) is not found in the SLL, the NN is added to the end (tail) of the list.     

Both methods will take in the string parameter and create a new node (NN).  They will then execute their code to insert the NN into the SLL.  Cases that need to be handled include (1) inserting into an empty SLL, (2) inserting as the first or head element (index 0 for insertAfter, and ‘B’efore the named head element in insertElt), (3) inserting into the interior of the list(between two existing nodes), and (4) inserting as the last/tail node(when the index exceeds the size for insertAfter, and when the NN element is not found in the SLL for insertElt).    
After the methods are created they are to be tested using a transaction stream to be provided as a list of strings for input, similar to the way the expressions were provided in a previous assignment.  These could also easily be provided in a text filethat could be read and processed in the same way.  The transactions consist of comma-separated elements: (1) a transaction code indicating which SLL ADT operation is to be executed, and (2) a value(s)to use when executing an add or insert, and no value when the operation is ‘remove’. 
