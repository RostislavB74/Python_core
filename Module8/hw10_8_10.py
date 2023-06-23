from collections import deque

MAX_LEN = 10
fifo = deque(maxlen=MAX_LEN)


def push(element):
    fifo.append(element)
    return fifo


def pop():
    return (fifo.popleft())


# push(element)
# pop()
