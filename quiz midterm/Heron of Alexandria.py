""" Heron of Alexandria """
import math as m
def main(numa, numb, numc):
    """ Heron of Alexandria """
    numx = (numa + numb + numc)/2
    print("%.3f" %(m.sqrt(numx*(numx-numa)*(numx-numb)*(numx-numc))))
main(float(input()), float(input()), float(input()))
