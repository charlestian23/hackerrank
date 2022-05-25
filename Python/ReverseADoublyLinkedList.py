#
# Complete the 'reverse' function below.
#
# The function is expected to return an INTEGER_DOUBLY_LINKED_LIST.
# The function accepts INTEGER_DOUBLY_LINKED_LIST llist as parameter.
#

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#

def reverse(llist):
    # Write your code here
    current_node = llist
    previous_node = None
    while current_node is not None:
        next_node = current_node.next
        current_node.next = current_node.prev
        current_node.prev = next_node
        previous_node = current_node
        current_node = next_node
    return previous_node
