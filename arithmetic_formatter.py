def arithmetic_arranger(problems, calc=False):

    if len(problems) > 5:
        return '''Error: Too many problems.'''

    parsed_equations = []

    for problem in problems:
        problem = problem.split()
        if problem[1] != "+" and problem[1] != "-":
            return '''Error: Operator must be '+' or '-'.''' 
        equation = {}

        equation["len1"] = len(problem[0])
        equation["len2"] = len(problem[2])
        try:
            equation["num1"] = int(problem[0])
            equation["num2"] = int(problem[2])
        except:
            return '''Error: Numbers must only contain digits.'''
    
        if (equation["len1"] or equation["len2"]) > 4:
            return '''Error: Numbers cannot be more than four digits.'''

        equation["op"] = problem[1]
        equation["max"] = max(equation["len1"], equation["len2"])
        parsed_equations.append(equation)

    to_print = ""

    for equation in parsed_equations:
        to_print += (equation["max"] + 2 - equation["len1"]) * " "
        to_print += str(equation["num1"])
        to_print += "    "
    to_print += "\n"

    for equation in parsed_equations:
        to_print += equation["op"]
        to_print += (equation["max"] + 1 - equation["len2"]) * " "
        to_print += str(equation["num2"])
        to_print += "    "
    to_print += "\n"

    for equation in parsed_equations:
        to_print += (equation["max"] + 2) * "-"
        to_print += "    "
    to_print += "\n"

    if calc:
        for equation in parsed_equations:
            res = equation["num1"] + equation["num2"] if equation["op"] == "+" else equation["num1"] - equation["num2"]
            res = str(res)
            to_print += (equation["max"] + 2 - len(res)) * " "
            to_print += res
            to_print += "    "

    return to_print


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))
