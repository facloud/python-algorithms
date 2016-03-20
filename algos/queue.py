class Queue(list):
    def __init__(self, *args):
        self.extend(args)

    def push(self, element):
        self.append(element)

    def pop(self):
        return list.pop(self, 0)

    def empty(self):
        return len(self) == 0
