from collections import deque

MAX_LEN = 10
lifo = deque(maxlen=MAX_LEN)


def push(element):
    lifo.appendleft(element)
    return lifo


def pop():
    return (lifo.popleft())


# push(element)
# pop()
