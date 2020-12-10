"""
Unit Cell Volume

The following function calculates the volume of a unit cell of any crystal system 
given the lattice parameters a,b,c,alpha,beta,gamma
"""
from numpy import cos, array, deg2rad, sqrt
from numpy.linalg import det

def ucvol(a,b,c,alpha,beta,gamma):
    """

    some helpful info can go here

    """

    g= array([[a*a, a*b*cos(deg2rad(gamma)), a*c*cos(deg2rad(beta))], 
                 [b*a*cos(deg2rad(gamma)), b*b, b*c*cos(deg2rad(alpha))], 
                 [c*a*cos(deg2rad(beta)),c*b*cos(deg2rad(alpha)),c*c]])
    return(sqrt(det(g)))

