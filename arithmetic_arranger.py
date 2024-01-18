def arithmetic_arranger(problems, display_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = ""
    second_line = ""
    dashes = ""
    answers = ""

    for problem in problems:
        parts = problem.split()
        first_number, operator, second_number = parts

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if not first_number.isdigit() or not second_number.isdigit():
            return "Error: Numbers must only contain digits."

        if len(first_number) > 4 or len(second_number) > 4:
            return "Error: Numbers cannot be more than four digits."

        length = max(len(first_number), len(second_number)) + 2
        top = str(first_number).rjust(length)
        bottom = operator + str(second_number).rjust(length - 1)
        dash = '-' * length
        answer = ""
        if display_answers:
            if operator == '+':
                answer = str(int(first_number) + int(second_number)).rjust(length)
            else:
                answer = str(int(first_number) - int(second_number)).rjust(length)

        if problem != problems[-1]:
            first_line += top + '    '
            second_line += bottom + '    '
            dashes += dash + '    '
            answers += answer + '    '
        else:
            first_line += top
            second_line += bottom
            dashes += dash
            answers += answer

    arranged_problems = first_line + "\n" + second_line + "\n" + dashes
    if display_answers:
        arranged_problems += "\n" + answers

    return arranged_problems




