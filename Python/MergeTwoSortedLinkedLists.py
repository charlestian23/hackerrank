#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def mergeLists(head1, head2):
    head = None
    one = head1
    two = head2
    if head1.data < head2.data:
        head = head1
        one = one.next
    else:
        head = head2
        two = two.next
    current = head
    while one is not None and two is not None:
        if one.data < two.data:
            current.next = one
            one = one.next
        else:
            current.next = two
            two = two.next
        current = current.next
    if one is not None:
        current.next = one
    elif two is not None:
        current.next = two
    return head
