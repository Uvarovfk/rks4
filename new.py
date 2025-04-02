import numpy as np
from S import rotation_matrix
from Angle import angle
A = np.array([1., 0., 0.])
lol = np.eye(3)
k = rotation_matrix(90., 0., 0.)
f = np.dot(np.dot(rotation_matrix(90., -90., 0.), rotation_matrix(0., 0., 0.)), [1,0,-1])
print(f)
