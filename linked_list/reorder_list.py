# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def append(head, data):
    new_node = ListNode(data)
    if not head:
        head = new_node
        return head
    last_node = head
    while last_node.next:
        last_node = last_node.next
    last_node.next = new_node
    return head

def create_linked_list(elements):
    linked_list = None
    for element in elements:
        linked_list = append(linked_list, element)
    return linked_list

def find_middle_point(head):
    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def reverse_linked_list(head):
    current_node = head.next
    previous_node = None
    head.next = None
    while current_node:
        next_node = current_node.next
        current_node.next = previous_node
        previous_node = current_node
        current_node = next_node
    return previous_node

def reorderList(head):
    """
    :type head: ListNode
    :rtype: None Do not return anything, modify head in-place instead.
    """
    middle = find_middle_point(head)
    second_half = reverse_linked_list(middle)
    first_half = head
    while first_half and second_half:
        first = first_half.next
        second = second_half.next
        first_half.next = second_half
        second_half.next = first
        first_half, second_half = first, second


if __name__ == '__main__':
    head = create_linked_list([1, 2, 3, 4, 5])
    reorderList(head)
    while head.next:
        print(head.val)
        head = head.next
    print(head.val)

