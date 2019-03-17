from collections import deque
if __name__ == '__main__':
    d=deque()
    d.append("dddd")
    d.append("kjfldjfl")
    d.append("kfldlf")
    print(d)
    print(d.popleft())
    print(type(d.pop()))
    print(d.pop())
    print(len(d))
