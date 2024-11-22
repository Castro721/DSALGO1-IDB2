from LinkedStack import LinkedStack as LinkStack
from PositionalList import PositionalList as PositionalList
import re

'''Part 1'''
expression = input("Enter an Expression: ")

precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
operators = set(precedence.keys())
stack = LinkStack()
temp_stack = LinkStack()

expression = re.sub(r'([+\-*/^()])', r' \1 ', expression)
tokens = expression.split()

for token in tokens:
    if token.isalnum():
        temp_stack.push(token)
    elif token in operators:
        while not stack.is_empty() and stack.top() != '(' and precedence.get(stack.top(), 0) >= precedence[token]:
            temp_stack.push(stack.pop())
        stack.push(token)
    elif token == '(':
        stack.push(token)
    elif token == ')':
        while not stack.is_empty() and stack.top() != '(':
            temp_stack.push(stack.pop())
        stack.pop()
    else:
        raise ValueError(f"Unknown token: {token}")
while not stack.is_empty():
    if stack.top() == '(':
        raise ValueError("Mismatched parentheses")
    temp_stack.push(stack.pop())

postfix1_stack = LinkStack()
while not temp_stack.is_empty():
    postfix1_stack.push(temp_stack.pop())

print("Postfix expression:", end=' ')
while not postfix1_stack.is_empty():
    print(postfix1_stack.pop(), end=' ')
print()


'''Part 2'''


def insertion_sort_descending(L):
    '''Sort the Positional List of comparable elements into non decreasing order.'''
    if len(L) > 1: #otherwise, no need to sort it
        marker = L.first()
        while marker != L.last():
            pivot = L.after(marker)#next item to place
            value = pivot.element()
            if value < marker.element():#pivot is already sorted
                marker = pivot#pivot becomes new marker
            else:#must relocate pivot
                walk = marker#find the leftmost value greater than pivot
                while walk != L.first() and L.before(walk).element() < value:
                    walk = L.before(walk)
                L.delete(pivot)#remove pivot
                L.add_before(walk, value)#insert pivot


def insertion_sort(L):
    '''Sort the Positional List of comparable elements into non decreasing order.'''
    if len(L) > 1: #otherwise, no need to sort it
        marker = L.first()
        while marker != L.last():
            pivot = L.after(marker)#next item to place
            value = pivot.element()
            if value > marker.element():#pivot is already sorted
                marker = pivot#pivot becomes new marker
            else:#must relocate pivot
                walk = marker#find the leftmost value greater than pivot
                while walk != L.first() and L.before(walk).element() > value:
                    walk = L.before(walk)
                L.delete(pivot)#remove pivot
                L.add_before(walk, value)#insert pivot


P = PositionalList()

P.add_first(1)
P.add_last(72)
P.add_last(81)
P.add_last(25)
P.add_last(65)
P.add_last(91)
P.add_last(11)

insertion_sort(P)
print("Insertion Sort Ascending:", end=' ')
for x in P:
    print(x, end=' ')
print()


insertion_sort_descending(P)
print("Insertion Sort Descending:", end=' ')
for x in P:
    print(x, end=' ')
