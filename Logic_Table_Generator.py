expression = "(a+b)(c+d)(e+(f+g))"
sub_equations = expression.replace(')(', ')|(').replace(') ', ')|').replace(' (', '|(').split('|')
print(sub_equations)