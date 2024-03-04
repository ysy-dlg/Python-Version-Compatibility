class Foo(object):

    def __init__(self, a):
        self.a = a
        self.cls_method()

    @classmethod
    def cls_method(cls):
        print 'class %s' % cls.__name__