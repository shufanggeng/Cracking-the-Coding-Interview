#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 20:09:51 2017

"""

"""
11.1 You are given two sorted arrays, A and B, where A has a large enough buffer 
at the end to hold B. Write a method to merge B into A in sorted order.
"""

def merge(A, B):
    m = len(A)
    n = len(B)
    while m > 0 and n > 0:
        if A[m-1] >= B[n-1]:
            A[m+n-1] = A[m-1]
            m -= 1
        else:
            A[m+n-1] = B[n-1]
            n -= 1

    if n > 0:
        """
        if B is not empty, then copy all the elements in B to A
        """
        A[:n] = B[:n]

"""
11.2 Write a method to sort an array of strings so that all the anagrams are 
next to each other.
"""

def groupAnagrams(strs):
    dic = {}
    for str in strs:
        s = ''.join(sorted(str))
        if s in dic:
            dic[s].append(str)
        else:
            dic[s] = [str]
            
    return [dic[x] for x in dic]

"""
11.3 Given a sorted array of n integers that has been rotated an unknown number
of times, write code to find an element in the array. You may assume that the 
array was originally sorted in increasing order.
"""

def rotatedArray(nums, n):
    if not nums:
        return -1
    start = 0
    end = len(nums)-1
    while start <= end:
        mid = (start+end)/2
        if nums[mid] == n:
            return mid
        if nums[start] <= nums[mid]:
            if nums[start] <= n <= nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if nums[mid] <= n <= nums[end]:
                start = mid + 1
            else:
                end = mid - 1
    return -1
                
"""
11.4 Imagine you have a 20 GB file with one string per line. Explain bow you 
would sort the file.
"""

""" external sort
https://github.com/wzhishen/cracking-the-coding-interview/blob/master/src/chap11/Q4.txt
"""

"""
11.5 Given a sorted array of strings which is interspersed with empty strings, 
write a method to find the location of a given string.
"""

def findString(strs, target, start=None, end=None):
    if not strs:
        return -1
    if start == None:
        start = 0
    if end == None:
        end = len(strs)-1
    while start <= end:
        mid = (start+end)/2
        while mid >= start and strs[mid] == '':
            mid -= 1
        if mid >= start and strs[mid] == target:
            return mid   
        if mid <= start or strs[mid] < target:
            return findString(strs, target, (start+end)/2 + 1, end)
        else:
            return findString(strs, target, start, mid-1)
       
    return -1

"""
11.6 Given an MXN matrix in which each row and each column is sorted in 
ascending order, write a method to find an element.
"""

def findElementInMatrix(matrix, target, rowStart=None, rowEnd=None, colStart=None, colEnd=None):
    if rowStart == None:
        rowStart = 0
    if rowEnd == None:
        rowEnd = len(matrix)-1
    if colStart == None:
        colStart = 0
    if colEnd == None:
        colEnd = len(matrix[0])-1
    if rowStart <= rowEnd and colStart <= colEnd:
        rowMid = (rowStart+rowEnd)/2
        colMid = (colStart+colEnd)/2
        if matrix[rowMid][colMid] == target:
            return [rowMid, colMid]
        if matrix[rowMid][colMid] < target:
            r = findElementInMatrix(matrix, target, rowStart, rowMid, colMid+1, colEnd)
            if r:
                return r
            r = findElementInMatrix(matrix, target, rowMid+1, rowEnd, colStart, colMid)
            if r:
                return r
            r = findElementInMatrix(matrix, target, rowMid+1, rowEnd, colMid+1, colEnd)
            if r:
                return r
        else:
            r = findElementInMatrix(matrix, target, rowStart, rowMid-1, colStart, colMid-1)
            if r:
                return r
            r = findElementInMatrix(matrix, target, rowMid, rowEnd, colStart, colMid-1)
            if r:
                return r
            r = findElementInMatrix(matrix, target, rowStart, rowMid-1, colMid, colEnd)
            if r:
                return r
                               
    return []

"""
11.7 A circus is designing a tower routine consisting of people standing atop 
one another's shoulders. For practical and aesthetic reasons, each person must 
be both shorter and lighter than the person below him or her. Given the heights 
and weights of each person in the circus, write a method to compute the largest 
possible number of people in such a tower.
"""

def largestNumberPeople(people):
    people = sorted(people, key=lambda person: person[1])
    dp = [1]*len(people)
    for i in range(1,len(people)):
        for j in range(i):
            if people[j][0] < people[i][0]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)

"

            
            
        
            
    

                
    



    
    

    
