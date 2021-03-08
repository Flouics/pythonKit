import turtle as T
from random import *
from math import *


def tree(n,l,t):
    t.pd()#下笔
    #阴影效果
    t1 = cos(radians(t.heading()+45))/8+0.25
    t.pencolor(t1,t1,t1)
    t.pensize(n/3)
    t.forward(l)#画树枝

    if n>0:
        b = random()*15+10 #右分支偏转角度
        c = random()*15+10 #左分支偏转角度
        d = l*(random()*0.25+0.7) #下一个分支的长度
        #右转一定角度,画右分支
        t.right(b)
        tree(n-1,d,t)
        #左转一定角度，画左分支
        t.left(b+c)
        tree(n-1,d,t)
        #转回来
        t.right(c)
    else:
        #画叶子
        t.right(90)
        n=cos(radians(t.heading()-45))/4+0.5
        t.pencolor(n,n*0.8,n*0.8)
        t.circle(3)
        t.left(90)
        #添加0.3倍的飘落叶子
        if(random()>0.7):
            t.pu()
            #飘落
            th = t.heading()
            an = -40 +random()*40
            t.setheading(an)
            dis = int(800*random()*0.5 + 400*random()*0.3 + 200*random()*0.2)
            t.forward(dis)
            t.setheading(th)
            #画叶子
            t.pd()
            t.right(90)
            n = cos(radians(t.heading()-45))/4+0.5
            t.pencolor(n*0.5+0.5,0.4+n*0.4,0.4+n*0.4)
            t.circle(2)
            t.left(90)
            t.pu()
            #返回
            t1=t.heading()
            t.setheading(an)
            t.backward(dis)
            t.setheading(t1)
    t.pu()
    t.backward(l)#退回

t = T.Turtle()
#t.bgcolor(0.5,0.5,0.5)#背景色
t.ht()#隐藏turtle
t.speed(0)#速度 1-10渐进，0 最快
#tracer(0,0)
t.pu()#抬笔
t.backward(100)
t.left(90)#左转90度
t.pu()#抬笔
t.backward(300)#后退300
tree(7,100,t)#递归7层
t.done()
