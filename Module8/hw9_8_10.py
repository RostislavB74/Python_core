from collections import deque

MAX_LEN = 5

lifo = deque()
lifo.append('second')
lifo.append('third')
lifo.append('forth')
lifo.append("4")
element = 'first'


def push(element):
    lifo.appendleft(element)
    return lifo


def pop(lifo):
    lifo.popleft('first')

    return lifo


push(element)
pop(lifo)
