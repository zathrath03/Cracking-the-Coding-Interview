# CtCI 2.5
# You have two numbers represented by a linked list, where each node contains
# a single digit. The digits are stored in reverse order, such that the 1's
# digit is at the head of the list. Write a function that adds the two numbers
# and returns the sum as a linked list.
from LinkedList.py import LinkedList, Node


def sum_lists(one, two):
    node1, node2 = one, two
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

    while nodes:
        tail.next = Node(nodes.data)
        tail = tail.next
        nodes = nodes.next

    return head.next


list1 = next = Node(1)
next.next = Node(2)
next = next.next
next.next = Node(3)
next = next.next
next.next = Node(4)
next = next.next
next.next = Node(8)
next = next.next
next.next = Node(9)
next = next.next
next.next = Node(1)

print(list1)

# next = list1
# while next:
#     print(next.data, end=" ")
#     next = next.next
# print()

# list2 = next = Node(5)
# next.next = Node(6)
# next = next.next
# next.next = Node(7)

# next = list2
# while next:
#     print(next.data, end=" ")
#     next = next.next
# print()

# result = sum_lists(list1, list2)
# next = result
# while next:
#     print(next.data, end=" ")
#     next = next.next
