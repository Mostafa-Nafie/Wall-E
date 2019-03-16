from OpenGL.GL import*
from OpenGL.GLUT import*
import numpy as np
from math import *

def drawCircle(r=0.1, xc=0, yc=0):
    glBegin(GL_POLYGON)
    for theta in np.arange(0, 2 * pi, 0.001):
        x = r * cos(theta)
        y = r * sin(theta)
        glVertex(x + xc, y + yc)
    glEnd()

def drawHalfCircle(r=0.1, xc=0, yc=0):
    glBegin(GL_POLYGON)
    for theta in np.arange(pi,2 * pi, 0.001):
        x = r * cos(theta)
        y = r * sin(theta)
        glVertex(x + xc, y + yc)
    glEnd()


def draw():
    glClearColor(1, 1, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT)

    #BaseGround
    glColor3f(0.13, 0.27, 0.45)
    glLineWidth(4)
    glBegin(GL_LINES)
    glVertex(-1, -0.8)
    glVertex(1, -0.8)
    glVertex(-0.5, -0.85)
    glVertex(-0.1, -0.85)
    glVertex(0.1, -0.85)
    glVertex(0.5, -0.85)
    glVertex(-0.2, -0.9)
    glVertex(0.2, -0.9)
    glEnd()

    #wheels
    for i in (1, -1):
        glColor3f(0.5, 0.5, 0.5)
        glBegin(GL_QUADS)
        glVertex(i * 0.8, -0.8)
        glVertex(i * 0.5, -0.8)
        glVertex(i * 0.5, -0.3)
        glVertex(i * 0.8, -0.3)
        glEnd()

        glColor3f(0.13, 0.27, 0.45)
        glLineWidth(4)
        glBegin(GL_LINE_LOOP)
        glVertex(i * 0.8, -0.8)
        glVertex(i * 0.8, -0.3)
        glVertex(i * 0.5, -0.3)
        glVertex(i * 0.5, -0.8)
        glEnd()

        glLineWidth(2)
        glBegin(GL_LINES)
        for j in range(0, 7):
            glVertex(i * 0.8, -0.765 + j * (0.8 - 0.3) / 7)
            glVertex(i * 0.5, -0.765 + j * (0.8 - 0.3) / 7)
        glEnd()


        #legs
        glLineWidth(4)
        for ((R, G, B), type) in ( ((0.67, 0.72 , 0.74), GL_POLYGON), ((0.13, 0.27, 0.45), GL_LINE_LOOP)):
            glColor3f(R, G, B)

            glBegin(type)
            glVertex(i * 0.5, -0.65)
            glVertex(i * 0.45, -0.65)
            glVertex(i * 0.45, -0.6)
            glVertex(i * 0.5, -0.6)
            glEnd()

            glBegin(type)
            glVertex(i * 0.45, -0.7)
            glVertex(i * 0.34, -0.7)
            glVertex(i * 0.30, -0.63)
            glVertex(i * 0.30, -0.55)
            glVertex(i * 0.45, -0.55)
            glEnd()


            glBegin(type)
            glVertex(i * 0.30, -0.55)
            glVertex(i * 0.45, -0.55)
            glVertex(i * 0.5, -0.5)
            glVertex(i * 0.5, -0.35)
            glVertex(i * 0.30, -0.35)
            glEnd()




        glColor3f(0.13, 0.27, 0.45)
        drawCircle(0.08, i * 0.1, 0.55)
        glColor3f(1, 1, 1)
        drawCircle(0.065, i * 0.1, 0.55)


    #body
    for (R, G, B, type) in ((0.49, 0.56, 0.58, GL_POLYGON), (0.13, 0.27, 0.45, GL_LINE_LOOP)):  #upper
        glColor3f(R, G, B)
        glBegin(type)
        glVertex(-0.45, 0)
        glVertex(-0.45, 0.2)
        glVertex(0.45, 0.2)
        glVertex(0.45, 0)
        glEnd()

    for (R, G, B, type) in ((1, 0.82, 0.3, GL_POLYGON),(0.13, 0.27, 0.45, GL_LINE_LOOP)):       #lower
        glColor3f(R, G, B)
        glBegin(type)
        glVertex(0.45, -0.5)
        glVertex(-0.45, -0.5)
        glVertex(-0.45, 0)
        glVertex(0.45, 0)
        glEnd()


        #nick
        glBegin(type)
        glVertex(-0.1, 0.2)
        glVertex(0.1, 0.2)
        glVertex(0.1, 0.4)
        glVertex(-0.1, 0.4)
        glEnd()

        glBegin(type)
        glVertex(-0.05, 0.4)
        glVertex(0.05, 0.4)
        glVertex(0.05, 0.5)
        glVertex(-0.05, 0.5)
        glEnd()

        glBegin(type)
        glVertex(-0.05, 0.5)
        glVertex(-0.15, 0.6)
        glVertex(-0.15, 0.8)
        glVertex(0.15, 0.8)
        glVertex(0.15, 0.6)
        glVertex(0.05, 0.5)
        glEnd()



    drawHalfCircle(0.12, 0, 0.69)       #smile
    glColor(1, 0.82, 0.3)
    drawHalfCircle(0.11, 0, 0.7)


    #chest
    glColor3f(0.13, 0.27, 0.45)
    glLineWidth(2)
    glBegin(GL_LINES)
    glVertex(-0.1, 0.267)
    glVertex(0.1, 0.267)
    glVertex(-0.1, 0.33)
    glVertex(0.1, 0.33)
    glVertex(-0.2, 0.7)
    glVertex(0.2, 0.7)
    glVertex(-0.45, 0)
    glVertex(0.45, 0)
    glEnd()


    glLineWidth(6)
    glColor3f(0.13, 0.27, 0.45)
    for i in (1, -1):
        glBegin(GL_LINES)
        glVertex(i * 0.3, 0)
        glVertex(i * 0.3, 0.2)
        glVertex(i * 0.45, 0.06)
        glVertex(i * 0.3, 0.06)
        glVertex(i * 0.45, 0.14)
        glVertex(i * 0.3, 0.14)
        glEnd()


    glLineWidth(4)
    for (R, G, B, type) in ((0.52, 0.8, 1, GL_POLYGON), (0.13, 0.27, 0.45, GL_LINE_LOOP)):
        glColor3f(R, G, B)
        glBegin(type)
        glVertex(-0.05, 0.18)
        glVertex(-0.2, 0.18)
        glVertex(-0.2, 0.08)
        glVertex(-0.05, 0.08)
        glEnd()

    drawCircle(0.03, -0.16, 0.04)
    glColor3f(0.8, 0.37, 0.35)
    drawCircle(0.015, -0.16, 0.04)

    for (R, G, B, type) in ((0.3, 0.3, 0.25, GL_POLYGON), (0.13, 0.27, 0.45, GL_LINE_LOOP)):
        glColor3f(R, G, B)
        glBegin(type)
        glVertex(0.05, 0.18)
        glVertex(0.2, 0.18)
        glVertex(0.2, 0.02)
        glVertex(0.05, 0.02)
        glEnd()

    glColor3f(0.69, 0.66, 0.18)
    glBegin(GL_QUADS)
    glVertex(0.12, 0.16)
    glVertex(0.18, 0.16)
    glVertex(0.18, 0.04)
    glVertex(0.12, 0.04)
    glEnd()
    drawCircle(0.02, 0.08, 0.14)


    #eyes
    for i in (-1, 1):
        glColor3f(0.13, 0.27, 0.45)
        for j in np.arange(0.05, 0.14, 0.01):
              drawCircle( j + 0.01, i * 0.05 + i * 1.6 * j, 0.9 - 2 * j)
        glColor3f(0.83, 0.92, 0.95)
        for j in np.arange(0.05, 0.14, 0.01):
              drawCircle( j, i * 0.05 + i * 1.6 * j, 0.9 - 2 * j)
        glColor3f(0.13, 0.27, 0.45)
        drawCircle(0.1 + 0.01, i * 0.21, 0.7)
        glColor3f(0.345, 0.443, 0.56)
        drawCircle(0.1, i * 0.21, 0.7)
        glColor3f(0.2, 0.3, 0.47)
        drawCircle(0.06, i * 0.21, 0.7)
        glColor3f(0.76, 0.8, 0.84)              #inner white
        drawCircle(0.02, i * 0.178, 0.66)
        drawCircle(0.03, i * 0.23, 0.75)
        glPointSize(5)
        glColor3f(0.13, 0.27, 0.45)             #dots
        drawCircle(0.01, i * 0.13, 0.82)
        drawCircle(0.01, i * 0.21, 0.55)
        drawCircle(0.01, i * 0.35, 0.66)
        drawCircle(0.01, i * 0.35, -0.65)

        # hands
    for i in (-1, 1):
        for (R, G, B, type) in ((1, 0.82, 0.3, GL_POLYGON), (0.13, 0.27, 0.45, GL_LINE_LOOP)):
            glColor3f(R, G, B)
            glBegin(type)
            glVertex(i * 0.45, 0.1)
            glVertex(i * 0.45, 0.2)
            glVertex(i * 0.51, 0.15)
            glVertex(i * 0.51, 0.1)
            glEnd()

        glColor3f(0.78, 0.9, 92)
        glBegin(GL_QUADS)
        glVertex(i * 0.25, 0.02)
        glVertex(i * 0.25, 0.1)
        glVertex(i * 0.55, 0.1)
        glVertex(i * 0.55, 0.02)
        glVertex(i * 0.55, 0.02)
        glVertex(i * 0.5, 0.02)
        glVertex(i * 0.5, -0.02)
        glVertex(i * 0.55, -0.02)
        glVertex(i * 0.25, -0.02)
        glVertex(i * 0.55, -0.02)
        glVertex(i * 0.55, -0.1)
        glVertex(i * 0.25, -0.1)
        glEnd()
        glColor3f(0.13, 0.27, 0.45)
        glBegin(GL_LINE_LOOP)
        glVertex(i * 0.25, 0.02)
        glVertex(i * 0.25, 0.1)
        glVertex(i * 0.55, 0.1)
        glVertex(i * 0.55, -0.1)
        glVertex(i * 0.25, -0.1)
        glVertex(i * 0.25, -0.02)
        glVertex(i * 0.5, -0.02)
        glVertex(i * 0.5, 0.02)
        glEnd()

        glBegin(GL_LINES)
        glVertex(i * 0.4, 0.1)
        glVertex(i * 0.4, 0.02)
        glVertex(i * 0.4, -0.1)
        glVertex(i * 0.4, -0.02)
        glEnd()

        for (R, G, B, type) in ((0.78, 0.9, 92, GL_POLYGON), (0.13, 0.27, 0.45, GL_LINE_LOOP)):
            glColor3f(R, G, B)
            glBegin(type)
            glVertex(i * 0.57, 0.06)
            glVertex(i * 0.5, 0.06)
            glVertex(i * 0.5, -0.06)
            glVertex(i * 0.57, -0.06)
            glEnd()

        for (R, G, B, type) in ((0.54, 0.63, 0.65, GL_POLYGON), (0.13, 0.27, 0.45, GL_LINE_LOOP)):
            glColor3f(R, G, B)
            glBegin(type)
            glVertex(i * 0.27, 0.02)
            glVertex(i * 0.5, 0.02)
            glVertex(i * 0.5, -0.02)
            glVertex(i * 0.27, -0.02)
            glEnd()



    glFlush()



glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowPosition(200, 200)
glutInitWindowSize(500, 500)
glutCreateWindow(b"Wall-E")
glutDisplayFunc(draw)
glutMainLoop()
