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

def reorderList(head):
    """
    :type head: ListNode
    :rtype: None Do not return anything, modify head in-place instead.
    """
    values = []
    cursor = head
    while cursor.next:
        values.append(cursor.val)
        cursor = cursor.next
    values.append(cursor.val)
    start = 1
    end = len(values) - 1
    last = head
    while start < end:
        last.next = ListNode(values[end], ListNode(values[start]))
        start += 1
        end -= 1
        last = last.next.next
    if start == end:
        last.next = ListNode(values[start])

if __name__ == '__main__':
    head = create_linked_list([1, 2, 3, 4, 5])
    reorderList(head)
    while head.next:
        print(head.val)
        head = head.next
    print(head.val)

