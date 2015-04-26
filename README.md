# MineWhat-Questions
Questions solved in Java

<h1>File Merger</h1>
Given 2 large files of order of around 10M lines of records each. Write a program to efficiently merge these files to get a complete record set.  Dont assume order of records and keep the code memory efficient. Merge even the header for columns.
eg. file1 
 Id , name , linkedin
 1, Randy , linkedin.com 
eg. file.
 name , company , lead status
 Paul , XYZ, warm lead
 Randy , ABCD , cold lead

eg. output file
Id , name ,  linkedin , company, lead status
1, Randy , linkedin.com , ABCD, cold lead
, Paul,  - , XYZ, warm lead

<h1>Array Merge Largest Number</h1>
Arrange given numbers to form the biggest number

Given an array of numbers, arrange them in a way that yields the largest value. For example, if the given numbers are {54, 546, 548, 60}, the arrangement 6054854654 gives the largest value. And if the given numbers are {1, 34, 3, 98, 9, 76, 45, 4}, then the arrangement 998764543431 gives the largest value.
