class speed:

    def __init__(self, frm, to, speed):
        self.frm = frm
        self.to = to
        self.speed = speed

class tris:

    def __init__(self, delta, v, pij):
        self.delta = delta
        self.v = v
        self.pij = pij

class label_t:
    def __init__(self, path, dist_origin, dist_node):
        self.path = path
        self.dist_origin = dist_origin
        self.dist_node = dist_node

class tris_priority_queue(object):
    def __init__(self):
        self.queue = []

    # for checking if the queue is empty

    def isEmpty(self):
        if (len(self.queue) == 0):
            return True
        else:
            return False

    # for inserting an element in the queue

    def insert(self, data):
        self.queue.append(data)

    # for popping an element based on Priority

    def delete(self):
        min = 0
        for i in range(len(self.queue)):
            if self.queue[i].delta < self.queue[min].delta:
                min = i
        item = self.queue[min]
        del self.queue[min]
        return item

    def print_queue(self):
        for element in self.queue:
            print (element)
