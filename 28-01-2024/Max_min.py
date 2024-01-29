"""
You will be given a list of integers, , and a single integer . You must create an array of length  from elements of  such that its unfairness is minimized. Call that array . Unfairness of an array is calculated as

Where:
- max denotes the largest integer in 
- min denotes the smallest integer in 

Example



Pick any two elements, say .

Testing for all pairs, the solution  provides the minimum unfairness.

Note: Integers in  may not be unique.

Function Description

Complete the maxMin function in the editor below.
maxMin has the following parameter(s):

int k: the number of elements to select
int arr[n]:: an array of integers
Returns

int: the minimum possible unfairness
Input Format

The first line contains an integer , the number of elements in array .
The second line contains an integer .
Each of the next  lines contains an integer  where .

Constraints




Sample Input 0

7
3
10
100
300
200
1000
20
30
Sample Output 0

20
"""


def maxMin(k, arr):
    # Write your code here
    arr.sort()

    min_unfairness = float('inf')

    for i in range(len(arr) - k + 1):

        current_unfairness = arr[i + k - 1] - arr[i]

        min_unfairness = min(min_unfairness, current_unfairness)

    return min_unfairness
