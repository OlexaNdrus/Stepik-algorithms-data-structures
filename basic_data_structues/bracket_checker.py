string = str(input())


def bracket_checker(brackets):
    qeue_list, mapper = [], {}
    mapper[')'] = '('
    mapper[']'] = '['
    mapper['}'] = '{'

    for ind, brack in enumerate(brackets):
        if brack in mapper.values():
            qeue_list.append(ind)

        elif brack in mapper:
            if not qeue_list:
                return ind + 1
            elif mapper[brack] != brackets[qeue_list.pop()]:
                return ind + 1
        else:
            continue

    if qeue_list:
        return qeue_list[-1]+1
    return "Success"


print(bracket_checker(string))

