def balancedBrackets(string):
    openBrackets = "([{"
    closingBrackets =")]}"
    brackets = {")":"(","}":"{","]":"["}
    stack=[]
    for c in string:
        if c in openBrackets:
            stack.append(c);
        elif c in closingBrackets:
            if len(stack)==0:
                return False
            if stack[-1]==brackets[c]:
                stack.pop()
            else:
                return False
    return len(stack)==0 
        #IF it is ( then we append
     
