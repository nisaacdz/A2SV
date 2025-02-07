class Solution:
    # Function to check if two arrays are equal or not.
    def checkEqual(self, a, b) -> bool:
        #code here
        a_dict, b_dict = {}, {}
        for a_val in a:
            a_dict[a_val] = a_dict.get(a_val, 0) + 1
        for b_val in b:
            b_dict[b_val] = b_dict.get(b_val, 0) + 1
        
        if len(a_dict) != len(b_dict) or any(v not in a_dict or c != a_dict[v] for v, c in b_dict.items()):
            return False
        return True
