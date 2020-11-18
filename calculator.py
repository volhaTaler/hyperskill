# write your code here

DONE = '/exit'
HELP = '/help'
OPERATORS = ['=', '+', '-', '*', '/', '^', '(', ')']
HIGH_POS = ['*', '/', '^']
BRACKETS = [' ', '+', '*', '/', '^', '(', ]


def help_info():
    print('The program calculates the sum and subtraction of numbers.'
          ' \n Letters and other signs are not supported'
          '\n Also multiplication, division and power operations are supported now.')


def finish_calculation():
    print('Bye!')
    return False


def check_digit(d):
    try:
        _ = int(d)
        return True
    except ValueError:
        return False


def check_brackets(input_lst):
    count_b = list()
    for item in input_lst:
        if item == '(':
            count_b.append(item)
        elif item == ')':
            if '(' in count_b and count_b[-1] == '(':
                count_b.pop()
            else:
                return False
    return not len(count_b)


def check_multi_div_op(k):
    len_k = len(k)
    if len_k > 1:
        return False
    elif len_k == 1:
        return True
    else:
        print("This case seems to be ignored!! Need to check")
        return None


def check_expression(input_lst, dict_var):
    # check_list stores check results of all components of the given expression
    check_list = list()
    if '(' in input_lst or ')' in input_lst:
        check_list.append(check_brackets(input_lst))
    for n in input_lst:
        if '+' in n or '-' in n:
            check_list.append(set(n).issubset('++++++++++--------------'))
        elif '*' in n or '/' in n or '^' in n:
            check_list.append(check_multi_div_op(n))
        elif n not in dict_var.keys() and n not in OPERATORS:
            check_list.append(check_digit(n))
        elif n == ')' or n == '(':
            # we have checked this condition already.
            pass
    assert all(d for d in check_list)


# calculate the simplified expression
def calculate_part(v_one, op, v_two):
    if op == '*':
        return v_one * v_two
    elif op == '/':
        return v_one // v_two
    elif op == '^':
        return v_one**v_two
    elif op == '+':
        return v_one + v_two
    elif op == '-':
        return v_one - v_two
    else:
        print('Something went wrong!')
        return None


# this function calculates simplifies the entered expression
def calculate(args_lst, dict_vars):
    if len(args_lst) > 0:
        solution = list()
        keys_d = dict_vars.keys()
        if args_lst[0] in keys_d:
            solution.append(dict_vars.get(args_lst[0]))
        elif args_lst[0] == '(':
            solution.append(args_lst[0])
        else:
            solution.append(int(args_lst[0]))
        # process the rest arguments of expression
        for i in args_lst[1:]:
            if i in HIGH_POS or i == '(':
                solution.append(i)
            elif all(c not in OPERATORS for c in list(i)):
                var = None
                if i in keys_d:
                    var = dict_vars.get(i)
                else:
                    var = int(i)
                if solution[-1] in HIGH_POS:
                    op = solution.pop()
                    var_one = solution.pop()
                    solution.append(calculate_part(var_one, op, var))
                else:
                    solution.append(var)
            elif i == ')':
                var_two = solution.pop()
                op = solution.pop()
                if op == '(':
                    op = solution.pop()
                var_one = solution.pop()
                op_bracket = solution.pop()
                if solution[-1] in HIGH_POS:
                    var_two = calculate_part(var_one, op, var_two)
                    op = solution.pop()
                    var_one = solution.pop()
                    solution.append(calculate_part(var_one, op, var_two))
                else:
                    solution.append(calculate_part(var_one, op, var_two))
            elif set(i).issubset('++++++++++'):
                solution.append('+')
            elif set(i).issubset('---------------'):
                if len(i) % 2 == 0:
                    solution.append('+')
                else:
                    solution.append('-')
    if len(solution) == 1:
        print(solution[0])
    else:
        while len(solution) != 1:
            var_one = solution[0]
            del solution[0]
            op = solution[0]
            del solution[0]
            var_two = solution[0]
            del solution[0]
            solution.insert(0, calculate_part(var_one, op, var_two))
        print(solution[0])


# check if a valid identifier was entered
def check_invalid_id(arg):
    try:
        assert(arg.isalpha())
        return True
    except AssertionError:
        return False


# check if the input sequence is a valid command
def expression_to_calc(args_l):
    if args_l[0] == '/':
        if all(a.isalpha() for a in args_l[1:]):
            print('Unknown command')
            return False
        else:
            print('Invalid expression')
            return False
    else:
        return True


# this function find the end of numbers in the input string
def get_min_index(sequence):
    ind_list = list()
    for i in OPERATORS:
        ind_n = sequence.find(i)
        if ind_n > -1:
            ind_list.append(ind_n)
    if len(ind_list) == 0:
        return len(sequence)
    else:
        return min(ind_list)


# this function parses complex substrings like '(-2*' or '3/45'
# which are not separated by whitespaces
def parse_details(string):
    parsed_lst = list()
    ind_end = -1
    for n in range(len(string)):
        if string[n] in OPERATORS:
            if string[n] == '-' and n > 0 and string[n - 1] in BRACKETS:
                ind_end = get_min_index(string[n + 1:]) + n + 1
                parsed_lst.append(string[n: ind_end])
            else:
                parsed_lst.append(string[n])
        elif string[n].isdigit() or string[n].isalpha():
            if ind_end < n:
                ind_end = get_min_index(string[n:]) + n
                if ind_end == n + 1:
                    parsed_lst.append(string[n])
                elif ind_end > n + 1:
                    parsed_lst.append(string[n: ind_end])
                else:
                    print('Uncoverted case!')
            else:
                pass
        else:
            print('Uncovered case!')
    return parsed_lst


# parse the input expression and store in arg_sub substrings like '+++' or '^^^^^'
def args_stack(arg_list):
    arg_subs = arg_list.split(" ")
    result_exp = list()
    for item in arg_subs:
        if all(c == '+' for c in item):
            result_exp.append(item)
        elif all(c == '-' for c in item):
            result_exp.append(item)
        elif all(c == '/' for c in item):
            result_exp.append(item)
        elif all(c == '*' for c in item):
            result_exp.append(item)
        elif all(c == '^' for c in item):
            result_exp.append(item)
        elif all(c.isalpha() or c.isdigit() for c in item):
            result_exp.append(item)
        elif all(c == '(' or c == ')' for c in item):
            result_exp.append(item)
        else:
            result_exp += parse_details(item)
    return result_exp


def working_mode():
    progress = True
    val_dict = {}
    while progress:
        args = input().strip()
        if args == DONE:
            progress = finish_calculation()
            del val_dict
        elif args == "":
            pass
        elif args == HELP:
            help_info()
        elif check_digit(args):
            print(int(args))
        elif any((c in OPERATORS) for c in args):
            if '=' in args:
                # assignment
                args_lst = list()
                ind = args.index('=')
                args_lst.append(args[:ind].strip())
                args_lst.append('=')
                args_lst.append(args[ind + 1:].strip())
                if len(args_lst) == 3:
                    # arg at position 0 is a variable -- only letters are allowed
                    # arg at position 2 can be digit or variable
                    if check_invalid_id(args_lst[0]):
                        try:
                            val_dict[args_lst[0]] = int(args_lst[2])
                        except ValueError:
                            if check_invalid_id(args_lst[2]) and args_lst[2] in val_dict.keys():
                                val_dict[args_lst[0]] = val_dict.get(args_lst[2])
                            else:
                                print('Invalid assignment')
                    else:
                        print('Invalid identifier')
            # expression calculation
            else:
                if expression_to_calc(args):

                    args = args_stack(args)
                    try:
                        check_expression(args, val_dict)
                    except AssertionError:
                        print('Invalid expression')
                    else:
                        calculate(args, val_dict)
               # else:
                #    pass
        else:
            if check_invalid_id(args):
                if args in val_dict.keys():
                    print(val_dict.get(args))
                else:
                    print("Unknown variable")
            else:
                pass


if __name__ == '__main__':
    working_mode()
