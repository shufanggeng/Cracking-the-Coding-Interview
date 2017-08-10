# -*- coding: utf-8 -*-

""" 1.1 Implement an algorithm to determine if a string has all unique 
    characters. What if you cannot use additional data structure """
    
def uniqueString(str):
    if not str:
        return
    """compare the length of string with unique characters and that of original
    string """
    return len(set(str)) == len(str)

""" 1.3 Given two strings,write a method to decide if one is a permutation 
    of the other """
    
def permutation(str1, str2):
    if not str1 or not str2:
        return
    """ the length of two strings should be the same if they are permutations
       of each other """
    if len(str1) != len(str2):
        return False
    """ sorted permutation of a string should be the same as the sorted string"""
    return sorted(str1) == sorted(str2)

def permutation1(str1, str2):
    """count characters of two strings"""
    return collections.Counter(str1) == collections.Counter(str2)

""" 1.4 Write a method to replace all spaces in a string with '%20'. 
    You may assume that the string has sufficient space at the end of the 
    string to hold the additional characters, and that you are given the 
    "true" length of the string."""

def replaceSpaces(str):
    s = list(str)
    newStr = ''
    for c in s:
        if c == ' ':
            newStr += '%20'
        else:
            newStr += c
    return newStr
""" challenge: do it in-place """
def replaceSpaces1(str):
    n = len(str)
    space = 0
    for c in str:
        if c == ' ':
            space += 2 
            """ two extra spaces are needed to fit '%20' """
    l = n + space
    index = l-1
    for i in range(n-1, -1, -1):
        if str[i] == ' ':
            str[index] = '0'
            str[index-1] = '2'
            str[index-2] = '%'
            index -= 3
        else:
            str[i] == str[index]
            index -= 1
    return l

""" 1.5 Implement a method to perform basic string compression using the 
    counts of repeated characters. For example, the string 'aabcccccaaa'
    would become a2b1c5a3. If the "compressed" string would not become smaller 
    than the original string, your method should return the original string"""
    
def compress(inputStr):
    if not inputStr:
        return 
    if len(inputStr) == 0:
        return ''
    """ initilize an empty sequence """
    compressed = []
    prev = inputStr[0]
    count = 0
    for c in inputStr:
        if c == prev:
            count += 1
        else:
            compressed.append(prev)
            compressed.append(str(count))
            count = 1
            """ 'count' need to be initialized to be 1 since current 'c' is
                 already scaned """
        prev = c
        
    compressed.append(c)
    compressed.append(str(count))
    outputStr = ''.join(compressed)
    
    if len(inputStr) < len(outputStr):
        return inputStr
    else:
        return outputStr
    
""" 1.6 Given an image represented by an NxN matrix, where each pixel in the 
    image is 4 bytes, write a method to rotate the image by 90 degrees. 
    Can you do this in place? """
    
def rotateImage(matrix):
    n = len(matrix)
     """ start from the 'top-left-quandrat and move elements in parallel """
    for i in range(n/2):
        for j in range(n-n/2):
            matrix[i][j], matrix[n-j-1][i], matrix[n-i-1][n-j-1], matrix[j][n-i-1] = \
            matrix[n-j-1][i],matrix[n-i-1][n-j-1], matrix[j][n-i-1], matrix[i][j]
     
       
""" Clock-wise or counter-clock-wise
Clock-wise, two steps: 1.transpose; 2. Reverse
Zip(*original[::-1])

Counter-clock-wise: 1.reverse (flip the matrix upside down); 2. Transpose
Reversed = original[::-1]
Zipped = zip(*reversed) """

def rotateImage1(matrix):
    return matrix[:] = zip(*matrix[::-1])
      
""" 1.7 Write an algorithm such that if an element in an MxN matrix is 0, 
    its entire row and column are set to 0 """

def zeroMatrix(matrix):
     m = len(matrix)
     n = len(matrix[0])
     row = [0]*m
     col = [0]*n
     if m == 0:
         return
     for i in range(m):
         for j in range(n):
             if matrix[i][j] == 0:
                 for x in range(m):
                     if matrix[x][j] != 0:
                         matrix[x][j] = 'a'
                 for x in range(n):
                     if matrix[i][x] != 0:
                         matrix[i][x] = 'a'
                
     for i in range(m):
         for j in range(n):
             if matrix[i][j] == 'a':
                 matrix[i][j] = 0
        
""" 1.8 Assume you have a method isSubstring which checks if one word is 
    a substring of another. Given two strings, s1 and s2, write code to check 
    If s2 is a rotation of s1 using only one call to isSubstring 
    (e.g., "waterbottLe" is a rotation of "erbot- tLewat"). """
    
def isRotation(s1, s2):
    if len(s1) != len(s2):
        return False
    s = s1 + s1
    """ check whether s2 is a substring of s, 'count' returns number of s2 in 
        s """
    if s.count(s2) > 0:
        return True
    return False
