num_of_vars, num_of_equals, num_of_unequals = (int(num) for num in input().split(' '))
array_of_vars = [var for var in range(num_of_vars)]
symlinc_indexes, result = [], 1


def relative_check(var, change_symlinks = False):
    if var == array_of_vars[var]:
        return var
    symlinc_indexes.append(var)
    return relative_check(array_of_vars[var])


def link_swapper(changer):
    if symlinc_indexes:
        for ind in symlinc_indexes:
            array_of_vars[ind] = changer
        symlinc_indexes.clear()


def add_equals(vars_input, cut_path=True):
    left_var = relative_check(int(vars_input[0]) - 1, cut_path)
    link_swapper(left_var)
    right_var = relative_check(int(vars_input[1]) - 1, cut_path)
    link_swapper(right_var)
    return left_var, right_var


for _ in range(num_of_equals):
    vars_input = input().split(' ')
    left_var, right_var = add_equals(vars_input)
    if left_var != right_var:
        array_of_vars[right_var] = left_var

for _ in range(num_of_unequals):
    vars_input = input().split(' ')
    left_var, right_var = add_equals(vars_input, False)
    if left_var == right_var:
        result = 0
        break


print(result)


