# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
from numpy import sin,cos,tan,pi
import matplotlib.pyplot as plt
from mem import *

r1 = 2
theta = pi/4
O = [0,0]
R1 = [r1*cos(theta),r1*sin(theta)]
plotvector(O,R1,'b-o')
plt.show()
