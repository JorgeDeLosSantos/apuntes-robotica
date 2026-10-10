# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
from numpy import sin,cos,tan,pi
import matplotlib.pyplot as plt

def plotvector(p0,u,color="b"):
    plt.plot([p0[0],u[0]],[p0[1],u[1]],color)
    
def test():
    ax = plt.axes()
    ax.arrow(0,0,0.1,0.1,head_width=0.05,head_length=0.1,fc="k",ec="k")
    plt.xlim([0,1])
    plt.ylim([0,1])
    plt.show()


if __name__=='__main__':
    test()
