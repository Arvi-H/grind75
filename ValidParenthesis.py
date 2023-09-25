class Solution(object):
    def isValid(self, s):
        # map ( -> ) , [ -> ] , { -> }
        # stack to keep track of opening brackets 
        
        # If it's an opening bracket push it onto the stack 
        # If it's a closing bracket:
            # Pop the top element from the stack (if the stack is not empty) 
            # Check if the popped element matches the current character using validMap. If they don't match, return False.
            
            # After processing all characters in the string, check if the stack is empty.
                # If the stack is empty return true
                # If the stack is not empty return False

        validMap = {'(':')', '[':']', '{':'}'} 
        stack = []

        # loop through s
        for i in s:
            if i in validMap:
                stack.append(i)
            else: 
                if not stack or validMap[stack.pop()] != i:
                    return False
        
        return not stack