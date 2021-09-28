def isBalanced(x):
    stack = []
    for bracket in x:
        if stack:
            if stack[-1] == "{" and bracket == "}":
                stack.pop(-1)
            elif stack[-1] == "(" and bracket == ")":
                stack.pop(-1)
            elif stack[-1] == "[" and bracket == "]":
                stack.pop(-1)   
            else:
                stack.append(bracket)
        else:
            stack.append(bracket)

    return len(stack) == 0


x = "([]"
print(isBalanced(x))