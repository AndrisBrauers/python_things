def arithmetic_arranger(problems):

  if len(problems) > 5:
    return '''Error: Too many problems.'''

  parsed_equeations = []
  for problem in problems:
    problem = problem.split()
    if problem[1] != '+' or problem[1] != '-':
      return '''Error: Operator must be '+' or '-'.'''
    try:
      problem[0] = int(problem[0])
      problem[2] = int(problem[2])
    except:

      return '''Error: Numbers must only contain digits.'''

  return 0


arithmetic_arranger(["2 + 2", "2.4 + 2"])
