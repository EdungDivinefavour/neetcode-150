class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Hopefully you already understand reverse polish notation so I won't bother explaining that
        # If you look carefully at how RPN works, we can gain some intuition
        # The key idea is that once we encounter an operator, we expect to have already seen operands and we can then use the operator to evaluate the last 2 operands
        # So the question for us now is... how do we remember the most recent thing(s) we saw... Hopefully you are already thinking "Stack!"

        stack = []

        for token in tokens:
            # If the token is not a sign, we can just add it to the stack
            if token not in ("+-*/"): 
                stack.append(int(token))
                continue

            # We are sure that we will have atleast 2 elements in the stack at this point
            # Because the first 2 tokens that we encounter will definitely be operands and not operators
            right = stack.pop()
            left = stack.pop()

            if token == "+":
                stack.append(left + right)
            elif token == "-":
                stack.append(left - right)
            elif token == "*":
                stack.append(left * right)
            elif token == "/":
                stack.append(int(left / right))
        
        return stack[0]
