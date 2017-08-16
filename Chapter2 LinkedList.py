#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 14:44:01 2017

"""

"""
2.1 Write code to remove duplicates from an unsorted linked list. FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed? 
"""

def removeDuplicates(head):
    cur = head
    while cur and cur.next:
        """ two pointers without temporary buffer"""
        if cur.val == cur.next.val:
            cur = cur.next.next
        else:
            cur = cur.next
    return head

""" 
2.2 Implement an algorithm to find the kth to last element of a singly 
    linked list.
"""

def findkthFromEnd(head, k):
    """ two pointers """
    slow = fast = head
    """fast pointer moves k nodes father than the slow one """
    for _ in range(k):
        fast = fast.next
    """" two pointers move at the same pace """
    while fast.next:
        slow = slow.next
        fast = fast.next
    return head

"""
2.3 Implement an algorithm to delete a node in the middle of a singly 
   linked list, given only access to that node.
"""
   
def deleteMiddleNode(head):
    """ 
    copy value of the next node over to the current node and then delete
        the next node 
    """
    if not head or not head.next:
        return
    cur = head
    cur = cur.next
    cur.val = cur.next.val
    cur = cur.next.next
    
""" 
2.4 Write code to partition a linked list around a value x, such that all 
    nodes less than x come before alt nodes greater than or equal to x.
"""
    
def partitionLinkedList(head, x):
    """ 
    create two different linked lists: one for elements less than x, 
        another one for elements greater or equal to x 
    """
    h1 = l1 = ListNode(0)
    h2 = l2 = ListNode(0)
    while head:
        if head.val < x:
            l1.next = head
            l1 = l1.next
        else:
            l2.next = head
            l2 = l2.next
        head = head.next
    """ avoid cycle in linked list """
    l2.next = None
    """ join two linked lists """
    l1.next = h2.next 
    
    return h1.ne
xt

""" 
2.4 You have two numbers represented by a linked list, where each node 
    contains a single digit.The digits are stored in reverse order,such that
    the 1's digit is at the head of the list. Write a function that adds the 
    two numbers and returns the sum as a linked list.
    FOLLOW UP
    Suppose the digits are stored in forward order. Repeat the above problem 
"""
        
def addNumbers(l1, l2):
    cur = dummy = ListNode(0)
    """ 
    the lengthes of two linked list might be different, use temporary 
        dummy node 
    """
    carry = 0
    while l1 or l2 or carry:
        v1 = v2 = 0
        if l1:
            v1 = l1.val
            l1 = l1.next
        if l2:
            v2 = l2.val
            l2 = l2.next
        val, carry = (v1 + v2 + carry)%10, (v1 + v2 + carry)/10
        cur.next = ListNode(val)
        cur = cur.next
        
    return dummy.next
        
""" 
2.6 Given a circular linked list, implement an algorithm which returns the
    node at the beginning of the loop. 
"""

def detecCycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        """ two pointers meet in the cycle. Initialize one pointer to the head 
            and the two pointers will meet at the beginning of the loop again"""
        if slow == fast:
            slow = head
            while fast != slow:
                slow = slow.next
                fast = fast.next
        return slow
    
""" 
2.7 Implement a function to check if a linked list is a palindrome. 
"""

def palindrome(head):
    if not head:
        return True
    """ fast pointer is one step ahead and slow pointer will be at the middle"""
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next
    """split the linked list to two parts """
    second = slow.next
    """ it is the end of the second linked list """
    slow.next = None 
    node = None
    """ reverse second linked list """
    while second:
        second.next, node, second = node, second, second.next
    """ compare two linked list """
    while node:
        if head.val != node.val:
            return False
        else:
            head = head.next
            node = node.next
    return True
   

    
    
            
    
    

    
        
        
