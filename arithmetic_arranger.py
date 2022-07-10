import re  # Import regex for string parsing.

# Start of function definition. "solve" is an optional parameter that defaults to False; if True, it causes the answer for each calculation to be printed under the dashed line.
def arithmetic_arranger(problems, solve=False):

    # Check for number of problems in the string.
    if len(problems) > 5:
        return "Error: Too many problems."

    # Variable Initialisation
    top_line = ""
    bottom_line = ""
    dash_line = ""
    result_line = ""

    # Iterate through the problem strings in the problems list.
    for problem in problems:
        # Check string only contains digits or the + or - operators.
        if re.search("[^\s\d.+-]", problem):
            if re.search("[/*]", problem):
                return "Error: Operator must be '+' or '-'."
            else:
                return "Error: Numbers must only contain digits."

        # Parse the problems list and obtain the two numbers and the operator from each string.
        first_number = problem.split()[0]
        operator = problem.split()[1]
        second_number = problem.split()[2]

        # Check that each number does not have more than four digits.
        if len(first_number) > 4 or len(second_number) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Calculate the sum of the numbers from each problem.
        sum = ""
        if operator == "+":
            sum = int(first_number) + int(second_number)
        elif operator == "-":
            sum = int(first_number) - int(second_number)

        # Define the line length as the maximum length of the biggest number out of the two, plus two characters (operator and a whitespace).
        line_length = max(len(first_number), len(second_number)) + 2
        # Justify the numbers to the right according to the respective line length.
        top = str(first_number).rjust(line_length)
        bottom = operator + str(second_number).rjust(line_length - 1)
        result = str(sum).rjust(line_length)
        # Create a dashed line with a number of dashes equal to the line length.
        dashes = ""
        for i in range(line_length):
            dashes += "-"

        # If problem is not the last one in the list, append the justified numbers to the displayed lines and add 4 spaces for the next problem.
        if problem != problems[-1]:
            top_line += top + "    "
            bottom_line += bottom + "    "
            dash_line += dashes + "    "
            result_line += result + "    "
        # If the problem is the last one in the list, do not add spaces.
        else:
            top_line += top
            bottom_line += bottom
            dash_line += dashes
            result_line += result

    # Arrange the lines with newlines to separate each string.
    if solve is True:
        arranged = top_line + "\n" + bottom_line + "\n" + dash_line + "\n" + result_line
    else:
        arranged = top_line + "\n" + bottom_line + "\n" + dash_line
    # print(arranged)
    return arranged
