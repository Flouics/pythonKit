# coding=utf-8
# encoding=utf-8

class Box:
    def __init__(self,mass = 1,velocity = 0):
        self.m = mass
        self.v = velocity
        self.count = 0

    def setVelocity(self,velocity):
        self.v = velocity

    def calcCollide(self,box):
        v1 = ((self.m - box.m) * self.v + 2 * box.m * box.v) / (self.m + box.m)   #  弹性碰撞公式
        v2 = v1 + self.v - box.v            # 碰撞公式 A物体碰撞前后速速之和等于物体B速度之和
        # print(v1,v2)
        if v1 > 0:
            v1 = -v1                   # 碰撞之后方向还是向左，就假装撞墙反弹
            self.count +=1
        self.v = v1
        box.v = v2
        self.count += 1

def main():
    factor = 100
    box_a = Box(1 * pow(factor,0) ,1)
    box_b = Box(1000000000, 0)
    while box_b.v - box_a.v < 0:      #追得上
        box_b.calcCollide(box_a)

    print("最后的速度", box_b.v ,box_a.v)
    print("碰撞多多少次",box_b.count)


if __name__ == "__main__" :
    main()
