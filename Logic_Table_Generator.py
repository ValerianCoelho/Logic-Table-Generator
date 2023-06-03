def getSubExpression(expression):
    subExpression = []
    count = 0
    start = 0

    for i, char in enumerate(expression):
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
            if count == 0:
                subExpression.append(expression[start+1:i])
                start = i + 1

    return subExpression

# Example usage
expression = "(a+b)(c+d)(e+(f+g)(h+i)+j)"
subExpression = getSubExpression(expression)
print(subExpression)
