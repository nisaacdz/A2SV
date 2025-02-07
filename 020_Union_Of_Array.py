class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def findUnion(self, a, b):
        # code here
        union = set()
        for a_val in a:
            union.add(a_val)
        for b_val in b:
            union.add(b_val)
        return len(union)
