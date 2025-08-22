#Divide and conquer algorithm
#Worst case: O(n2)
#Average case: O(nlogn)

'''Choosing last element as pivot element 
Pointer i traverse from left finding big ele than pivot
Pointer j traverse from right before pivot element finding small ele than pivot ele
swaps the i and j pointer if smaller and larger are found
if pointer j crosses pointer i then swap the pivot ele with the ele in pointer i'''