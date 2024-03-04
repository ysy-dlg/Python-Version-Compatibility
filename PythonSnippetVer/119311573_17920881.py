class QuadEq(object):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.answer = []


    def solve_quad_eq(self):
        D = self.b**2-4*self.a*self.c
        if D >= 0:
            x1 = (-self.b-math.sqrt(D))/2*self.a
            x2 = (-self.b+math.sqrt(D))/2*self.a
            self.answer = [x1, x2]
            return self.answer
        else:
            return 0

    def show_result(self):
        print self.answer