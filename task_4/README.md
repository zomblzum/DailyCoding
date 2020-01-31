# Task №2

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.

## Solution

Python script that 
1 - remove all non positive numbers from array
2 - traverse array and mark presense of element x by making prev elements negative
3 - return the index + 1 of the first positive value