from ArrayStack import ArrayStack as Stack


def reverse_file(file_path):
    stack = Stack()
    with open(file_path, 'r') as file:
        for line in file:
            stack.push(line.rstrip('\n'))
    with open(file_path, 'w') as file:
        while not stack.is_empty():
            file.write(stack.pop() + '\n')


def is_matched(expression):
    matching_symbols = {')': '(', '}': '{', ']': '['}
    for char in expression:
        if char in matching_symbols.values():
            S.push(char)
        elif char in matching_symbols.keys():
            if S.is_empty() or S.pop() != matching_symbols[char]:
                return False
    return S.is_empty()


S = Stack()
reverse_file(r'Z:\DSALGO1-IDB2\MIDTERMS\Activity3Midterms_Castro\myfile.txt')
user_input = input("Enter an expression to check for balanced symbols: ")

if is_matched(user_input):
    print('The symbols are balanced')
else:
    print('The symbols are not balanced')


