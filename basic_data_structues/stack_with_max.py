
num_of_operations = int(input())
def main(num_of_operations):
    stack, max_stack = [], [0]

    def push(val):
        if val >= head(max_stack):
            max_stack.append(val)
        stack.append(val)

    def head(stack):
        if stack:
            return stack[-1]

    def poper():
        if stack:
            if head(stack) == head(max_stack):
                max_stack.pop()
            stack.pop()

    def maxer():
        if max_stack:
            return head(max_stack)



    for op_ind in range(num_of_operations):
        value = input()
        if value == 'max':
            print(maxer())
        elif value.startswith('pop'):
            poper()
        else:
            value = value.split(' ')
            push(int(value[-1]))

main(num_of_operations)
