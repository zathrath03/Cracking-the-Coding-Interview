# CtCI 2.5
# You have two numbers represented by a linked list, where each node contains
# a single digit. The digits are stored in reverse order, such that the 1's
# digit is at the head of the list. Write a function that adds the two numbers
# and returns the sum as a linked list.
from LinkedList import LinkedList, Node


def sum_lists(one, two):
    node1, node2 = one.head, two.head
    tail = head = Node()
    carry = False

    while node1 and node2:
        res = node1.data + node2.data + 1 if carry else node1.data + node2.data
        if res >= 10:
            carry = True
            res -= 10
        else:
            carry = False
        tail.next = Node(res)
        tail = tail.next
        node1 = node1.next
        node2 = node2.next

    nodes = node1 if node1 else node2

    while carry and nodes:
        res = nodes.data + 1
        if res >= 10:
            carry = True
            res -= 10
        else:
            carry = False
        tail.next = Node(res)
        tail = tail.next
        nodes = nodes.next

    if carry:
        tail.next = Node(1)

    #TODO: handle if all remaining nodes are zero
    while nodes:
        tail.next = Node(nodes.data)
        tail = tail.next
        nodes = nodes.next
    ans = LinkedList()
    ans.head = head.next
    ans.tail = ans.head
    while ans.tail.next:
        ans.tail = ans.tail.next
    return ans


list1 = LinkedList((1, 2, 3, 4))
list2 = LinkedList((4, 5, 6, 7))
result = sum_lists(list1, list2)
print(result)
