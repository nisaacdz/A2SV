#User function Template for python3

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        a_dict, b_dict = {}, {}
        for a_val in a:
            a_dict[a_val] = a_dict.get(a_val, 0) + 1
        for b_val in b:
            b_dict[b_val] = b_dict.get(b_val, 0) + 1
            
        for num, count in b_dict.items():
            if num not in a_dict or a_dict[num] < count:
                return False
        return True
    
    
    
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while (T > 0):
        a1 = [int(x) for x in input().strip().split()]
        a2 = [int(x) for x in input().strip().split()]
        ob = Solution()
        if ob.isSubset(a1, a2):
            print("true")
        else:
            print("false")

        T -= 1

        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends
