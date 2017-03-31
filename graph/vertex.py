# vertex class

class Vertex(object):

    def __init__(self, name):
        self.level  = None
        self.parent = None
        self.start  = None
        self.finish = None
        self.name   = name

    def reset(self):
        self.level  = None
        self.parent = None
        self.start  = None
        self.finish = None

    def __str__(self):
        return self.name