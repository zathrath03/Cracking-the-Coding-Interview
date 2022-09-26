# CtCI 2.6 Implement a function to check if
# a linked list is a palindrome

from LinkedList import LinkedList

def isPalindrome(linked_list: LinkedList) -> bool:
    slow_ptr = fast_ptr = linked_list.head
    stack = []

    while fast_ptr and fast_ptr.next:
        stack.append(slow_ptr.data)
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next
    if fast_ptr:
        slow_ptr = slow_ptr.next
    while stack and slow_ptr:
        if stack.pop() != slow_ptr.data:
            return False
        slow_ptr = slow_ptr.next

    return True

# Test cases: empty LL, single char, two same chars, two different chars
    # odd palendrome, odd non-palendrome, even palendrome, even non-palendrome
test1 = LinkedList() # True
test2 = LinkedList('a') # True
test3 = LinkedList('aa') # True
test4 = LinkedList('ab') # False
test5 = LinkedList('abcba') # True
test6 = LinkedList('abcca') # False
test7 = LinkedList('abcddcba') # True
test8 = LinkedList('dabcdcba') # False
tests = [test1, test2, test3, test4, test5, test6, test7, test8]
assertions = [True, True, True, False, True, False, True, False]

for test, assertion in zip(tests, assertions):
    assert isPalindrome(test) == assertion
    print(f"{test} is {assertion}")