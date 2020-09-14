"""
This file is for PLTW Activity 1.1.1
It's source can be found at https://github.com/jglosson000/Micro-Projects/blob/master/smile.pyw


smile.pyw is licensed under the

MIT License

Copyright (c) 2020 Josiah Glosson

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


import turtle
import math


turtle.bgcolor('black')
turtle.setworldcoordinates(-10, -10, 10, 10)


def simple_circle(x, y, radius, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.pencolor(color)
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius, None, int(math.ceil(radius * 7.5)))
    turtle.end_fill()


simple_circle(0, -5, 5, 'white')
simple_circle(-2, 1, 0.75, 'blue')
simple_circle(2, 1, 0.75, 'blue')
simple_circle(0, -1, 0.65, 'green')


turtle.penup()
turtle.goto(-2.5, -1.5)
turtle.pendown()
turtle.pensize(3)
turtle.pencolor('red')
turtle.right(90)
turtle.circle(2.5, 180, 10)


turtle.done()
