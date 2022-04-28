class Square_sum:

    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        return self.x**2+self.y**2+self.z**2

obj_square = Square_sum(1,3,5)

print(obj_square.sqSum())

