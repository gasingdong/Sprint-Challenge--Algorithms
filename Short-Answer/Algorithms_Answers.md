#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) The pseudocode can be explained as taking steps of size n^2 to reach n^3, which will always be done in n steps. 

Answer: O(n)


b) It's looping through a for loop of size n, so at least O(n). However, inside the for loop is a while loop that's incrementing itself by a factor of 2 each time. The latter scales slower than linearly, so that's O(log n).

Answer: O (n log n)


c) This will recurse through itself n times since it only decrements the initial amount by 1 each time.

Answer: O(n)

## Exercise II

First, go to the middle floor. Drop the egg. If the egg breaks, consider only the lower floors. If the egg doesn't break, consider only the higher floors. For whichever segment you choose, go to the middle floor of that. Drop the egg again. Repeat this process of halving the floors to consider until you find f.

Runtime: O(log n)
