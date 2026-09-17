class Solution:
    def isValid(self, s: str) -> bool:
        # The key thing to note with this problem is that 
        # 1. We are trying to keep track of what we have seen in the past
        # 2. We are trying to ensure that if we saw multiple things, we are able to look them up in the order we saw them
        # 3. If we see three opening brackets and three closing brackets, we want to match the most recent open, with the most recent close. 
        # If this makes you think about a stack, you're right!
        # When we see an opening, we can store it in the stack.. and if we see a closing, we pop it from the stack

        stack = []
        for char in s:
            if not stack:
                stack.append(char)
                continue

            top = stack[-1]
            if ( # If we see a closing, and our top is an equivalent opening
                (char == ")" and top == "(") or
                (char == "]" and top == "[") or
                (char == "}" and top == "{")
            ):
                stack.pop()
            else:
                stack.append(char)
    
        return len(stack) == 0 # We expect the stack to be empty after everything