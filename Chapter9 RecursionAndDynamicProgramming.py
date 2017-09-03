#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 09:18:07 2017

"""

"""
9.1 A child is running up a staircase with n steps, and can hop either 1step, 
2 steps, or 3 steps at a time. Implement a method to count how many possible 
ways the child can run up the stairs.
"""

def climbStairs(n):
    if n == 0:
        return 0
    a, b, c = 0, 0, 1
    for _ in range(n):
        a, b, c = b, c, a+b+c
    return c
    """ 
    climbStairs(n) = climbStairs(n-1) + climbStairs(n-2) + climbStairs(n-3)
    """
    
"""
9.2 Imagine a robot sitting on the upper left corner of an X by Y grid. The robot
can only move in two directions: right and down. How many possible paths are 
there for the robot to go from (0, 0) to (X, Y) ?
FOLLOW UP
Imagine certain spots are "off limits," such that the robot cannot step on 
them. Design an algorithm to find a path for the robot from the top left to 
the bottom right.
"""

def gridPath(x, y):
    if x == 0 or y == 0:
        return 0
    dp = [[1]*y for i in range(x)]
    for i in range(x):
        for j in range(y):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[-1[-1]]
        
""" follow up """
def obstaclePath(obstacleGrid):
    if not obstacleGrid:
        return 0
    r = len(obstacleGrid)
    c = len(obstacleGrid[0])
    dp = [[0]*c for i in range(r)]
    """ obstacle is marked as '1' """
    dp[0][0] = 1-obstacleGrid[0][0]
    for i in range(1, r):
        dp[i][0] = (1-obstacleGrid[i][0])*dp[i-1][0]
    for i in range(1, c):
        dp[0][i] = (1-obstacleGrid[0][i])*dp[0][i-1]
      
    for i in range(1, r):
        for j in range(1, c):
            dp[i][j] = (dp[i-1][j] + dp[i][j-1])*(1-obstacleGrid[i][j])
    return dp[-1][-1]
 
"""
9.3 A magic index in an arrayA[1...n-1] is defined to be an index such that
A[i] = i. Given a sorted array of distinct integers, write a method to find a 
magic index, if one exists, in array A.
FOLLOW UP
What if the values are not distinct?
"""

def magicIndex(nums):
    n = len(nums)
    start = 0
    end = n-1
    while start <= end:
        mid = (start+end)/2
        if nums[mid] == mid:
            return mid
        if mid < nums[mid]:
            end = mid-1
        else:
            start = mid+1
    return None
    
""" fowllow up """

def magicIndex1(seq, start=None, end=None):
    if start == None:
        start = 0
    if end == None:
        end = len(seq)-1
    while start <= end:
        mid = (start+end)/2
        if mid == seq[mid]:
            return [mid]
        else:
            leftEnd = min(mid-1, seq[mid])
            rightStart = max(mid+1, seq[mid])
            return magicIndex1(seq, start = start, end = leftEnd) + \
                   magicIndex(seq, start = rightStart, end = end)
     
"""
9.4 Write a method to return all subsets of a set.
"""
""" set of distinct integers """
def subsets(nums):
    if len(nums) == 0:
        return [[]]
    s , r = nums[0], nums[1:]
    subset_exc_s = subsets(r)
    subset_inc_s = [[s] + h for h in subset_exc_s]
    
    return subset_exc_s + subset_inc_s

""" set of duplicate integers """

def subsetsWithDup(nums):
    res = [[]]
    nums = sorted(nums)
    for i in range(len(nums)):
        if i == 0 or nums[i] != nums[i-1]:
            l = len(res)
        for j in range(len(res)-l, len(res)):
            res.append(res[j]+res[i])
    return res
    
"""
9.5 Write a method to compute all permutations of a string.
"""
""" string with distinct elements """
def permutation(s):
    if not s:
        return [[]]
    return [[n]+p for i, n in enumerate(s) for p in permutation(s[:i]+s[i+1:])]

""" string with duplicates """

def permuteUnique(nums):
    res = [[]]
    for n in nums:
        res = [l[:i]+[n]+l[i:] for l in res for i in range((l+[n]).index(n)+1)]
        """
        index(n) always returns the index of the first duplicate elements in
        a list and it avoids inserting a number behind any of its duplicates
        """ 
    return res
    
"""
9.6 Implement an algorithm to print all valid (i.e., properly opened and 
closed) combinations of n-pairs of parentheses. 
"""

def validParentheses(s):
    pairs = {')':'(', ']':'[', '}':'{'}
    stack = []
    for c in s:
        if c in pairs.values():
            stack.append(c)
        elif c in pairs.keys():
            if stack == [] or pairs[c] != stack.pop():
                return False
    return stack == []

"""
9.7 Implement the "paint fill" function that one might see on many image 
editing programs. That is, given a screen (represented by a two dimensional 
array of colors), a point, and a new color, fill in the surrounding area until 
the color changes from the original color.
"""

def paintFill(screen, x, y, new_color, original_color=None):
    max_x = len(screen[0])
    """column"""
    max_y = len(screen)
    """rows """
    if x < 0 or x > max_x or y < 0 or y > max_y:
        return 
    if original_color is None:
        original_color = screen[y][x]
    if screen[y][x] == original_color:
        screen[y][x] = new_color
        paintFill(screen, x+1, y, new_color, original_color=original_color)
        paintFill(screen, x, y+1, new_color, original_color=original_color)
        paintFill(screen, x-1, y, new_color, original_color=original_color)
        paintFill(screen, x, y-1, new_color, original_color=original_color)
    return
        
"""
9.8 Given an infinite number of quarters (25 cents), dimes (10 cents), nickels
(5 cents) and pennies (1 cent), write code to calculate the number of ways of 
representing n cents.
"""

def coinChange(n, coins):
    dp = [1] + [0]*n
    for c in coins:
        for i in range(1, n+1):
            if i >= c:
                dp[i] += dp[i-c]
    return dp[-1]
        
""" 
9.9 Write an algorithm to print all ways of arranging eight queens on an 8x8
chess board so that none of them share the same row, column or diagonal. In 
this case, "diagonal" means all diagonals, not just the two that bisect the 
board.
"""

def queens(n):
    def DFS(queens, xy_diff, xy_sum):
        """
        queens is a one-dimension array, [1,3,0,2] means the first queen is placed 
        at column 2, the second queen is placed at column 4, the third queen is 
        placed at column 1 and the fourth queen is placed at column 3.
        """
        p = len(queens)
        if p == n:
            result.append(queens)
            return None
        """ base case """
        for q in range(n):
            if q not in queens and p-q not in xy_diff and p+q not in xy_sum:
            """ column check and diagonal check """
                DFS(queens+[q], xy_diff+[p-q], xy_sum+[p+q])
   
    result = []
    DFS([], [], [])
    return [['.'*i + 'Q' + '.'*(n-i-1) for i in sol] for sol in result]
             
""" 
9.10 You have a stack of n boxes, with widths w., heights l and depths d. The
boxes cannot be rotated and can only be stacked on top of one another if each 
box in the stack is strictly larger than the box above it in width, height, and
depth. Implement a method to build the tallest stack possible, where the height
of a stack is the sum of the heights of each box.
"""

def canStack(box1, box2):
    return box1.length > box2.length and \
        box1.width > box2.width and \
        box1.height > box2.height

def getBoxMaxHeight(boxes,dp,idx):
    if dp[idx] is not None:
        return dp[idx]
    dp[idx] = max([boxes[idx].height]+[boxes[idx].height+getBoxMaxHeight(boxes,dp,x) for x in range(len(boxes)) if canStack(boxes[idx],boxes[x])])  
    return dp[idx]
 
       
def boxStackMaxHeight(boxes):
    num_boxes = len(boxes)
    dp = [None] * num_boxes
    for i in range(num_boxes):
        getBoxMaxHeight(boxes,dp,i)
    return max(dp)
                
    
    
    



        
            
            
        
        
        