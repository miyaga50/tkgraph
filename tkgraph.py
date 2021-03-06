#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
import sys,random,time

"""
node = [0,1,2,3]
graph=[(0,1),(0,2),(1,3),(2,1)]
layout ={0:(100,100),1:(100,50),2:(50,50),3:(160,40),}
"""

class Layout(object):
    @classmethod
    def random(self,g):
        layout = {}
        _ = lambda : random.random()
        for i in g.node:
            layout[i] = (_(),_())
        return layout

class Graph(object):
    def __init__(self,directed = False,canvas = None):
        self.node = []
        self.link = []
        self.directed = directed
        self.canvas = canvas

    def __str__(self):
        out = "node:"+str(self.node)+"\nlink:"+str(self.link)+"\n"
        return out

    def warshall_floyd(self):
        dist = {}
        for i in self.node:
            dist[i] = {}
            for j in self.node:
                dist[i][j] = 0 if i ==j else sys.maxint
        return dist

    def kamada_kawai(self):
        pass


    def add_node(self,*node):
        for x in node:
            self.node.append(x)

    def add_node_from(self,list):
        self.node.extend(list)

    def add_link(self,n1,n2):
        self.link.append((n1,n2))

    def exist_link(self,link):
        return True

    def layout_random(self):
        layout = {}
        _ = lambda : random.random()
        for i in self.node:
            layout[i] = (_(),_())
        return layout

    def plot(self,layout_func = Layout.random):
        layout = layout_func(self)

        for i,(x,y) in layout.iteritems():
            self.canvas.draw_node(x,y,id = i)
        for i,j in self.link:
            self.canvas.draw_line(layout[i][0],layout[i][1],
                    layout[j][0],layout[j][1],
                    arrow = self.directed)

    def plot_random(self):
        _ = lambda : random.random()
        layout = {}
        for i in node:
            layout[i] = (200*_()+20,200*_()+20)

        for x,y in layout.values():
            self.draw_node(x,y)
        for i,j in graph:
            self.draw_line(layout[i][0],layout[i][1],
                    layout[j][0],layout[j][1])


class GraphCanvas(Canvas):
    def __init__(self,master=None,width = 600,height = 600):
        Canvas.__init__(self,master)
        self.master.title("グラフ描画")
        self["width"] = width
        self["height"] = height
        self.pack()
        self.width = width
        self.height = height

    def draw_node(self,x,y,id = None,r = 10,color = "blue"):
        node = self.create_oval(self.width*x-r,self.height*y-r,
                self.width*x+r,self.height*y+r,fill = color)
        name = self.create_text(self.width*x-r,self.height*y-r,
                text = str(id))

    def draw_line(self,x0,y0,x1,y1,arrow = True):
        if arrow:
            self.create_line(self.width*x0,self.height*y0,
                    self.width*x1,self.height*y1,
                    arrow=LAST,arrowshape = (10,10,3) )
        else:
            self.create_line(self.width*x0,self.height*y0,
                    self.width*x1,self.height*y1)
       
    def plot(self,graph,layout):
        _ = lambda : random.random()
        for i,(x,y) in layout.iteritems():
            self.draw_node(x,y,id = i)
        for i,j in graph.link:
            self.draw_line(layout[i][0],layout[i][1],
                    layout[j][0],layout[j][1],
                    arrow = graph.directed)

class Main(object):
    @classmethod
    def plot(self):
        #make a main window
        root = Tk()
        #make a plotting canvas
        mc = GraphCanvas(root)

        #make a sample graph
        g = Graph(directed = True,canvas = mc)
        g.add_node_from(range(100))
        for i in range(100):
            n1,n2 = random.sample(g.node,2)
            g.add_link(n1,n2)

        #plot the graph
        g.plot()
        print g

        #main loop for the main window
        root.mainloop()
        sys.exit()

if __name__ == "__main__":
    Main.plot()
