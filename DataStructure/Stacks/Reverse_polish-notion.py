#todo:(Stacks):
# Question 2:Reverse Polish Notation
# Evaluate the value of an arithmetic expression in
# Reverse Polish Notation(See example).
# Valid operators are +, -, *, and /. Note that division between two integers
# should truncate toward zero. It is guaranteed that the given RPN expression
# is always valid. That means the expression would always evaluate to a result,
# and there will not be any division by zero operation.
# The Input is an array of strings where each element is either a valid operator
# or an integer. E.g.[“1”,”2”,”+”]

def evaluate_reverse_polish_notation(tokens):
  stack = []
  valid_operators = {
    '+': lambda n1, n2: n1 + n2,
    '-': lambda n1, n2: n1 - n2,
    '*': lambda n1, n2: n1 * n2,
    '/': lambda n1, n2: n1 // n2
  }

  for token in tokens:
    if token in valid_operators:
      n2 = stack.pop()
      n1 = stack.pop()
      result = valid_operators[token](n1, n2)
      stack.append(result)
    else:
      stack.append(int(token, 10))

  return stack.pop()


print(evaluate_reverse_polish_notation(['4', '13', '5', '/', '+']))
