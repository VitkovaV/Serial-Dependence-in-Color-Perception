# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 13:35:49 2017

@author: toelch
"""
import numpy as np
from skimage import color 
import random

def lab2rgb(lab):
    thres1 = 216/24389
    thres2 = 24389/27
    thres3 = 0.0031308
    y=(lab[0]+16)/116
    x=lab[1]/500+y
    z= y-lab[2]/200        
    xyz=(x,y,z)
    if ((x**3)>thres1):
        x=x**3 
    else:
        x = (116*x-16)/thres2
        
    if lab[0]>thres1*thres2:
        y = y**3
    else:
        y = lab[0]/thres2
        
    if z**3>thres1:
        z=z**3
    else:
        z=(116*z-16)/thres2
    xyz=np.array((x,y,z))
    Minv=np.array([3.2404542,-1.5371385,-0.4985314,-0.9692660,1.8760108,0.0415560,0.0556434,-0.2040259,1.0572252]).reshape(3,3)    
    RGB=np.dot(xyz,Minv)
    RGB[np.greater(RGB,1)]=1
    RGB[np.less(RGB,0)]=0
    RGBthresh = np.less(RGB,thres3)
    RGB[RGBthresh] = 1.055 * (RGB[RGBthresh]**(1/2.4)) - 0.055
    RGB[np.invert(RGBthresh)] = 12.92 * RGB[np.invert(RGBthresh)]
    RGB[np.greater(RGB,1)]=1
    RGB[np.less(RGB,0)]=0
    return(RGB);

lab2rgb(alle)


Minv




alle=(random.random(),random.random(),random.random())
alle2=(0,0,0)
([[alle]])
color.xyz2rgb([[lab2rgb(alle)]])


alle=(1,1,1)
alle[2]
lab2rgb(alle)
xyzthresh=[1 if x>0.008856 else 0 for x in xyz ]
xyz2 = [a*(b**3) for a,b in zip(xyzthresh,xyz)]
xyzthresh_inv=[1-i for i in xyzthresh] 
xyz3 = [a*((b - 16 / 116) / 7.787) for a,b in zip(xyzthresh_inv,xyz)]
xyz=[a+b for a,b in zip(xyz2,xyz3)]
xyz=np.array(xyz)
Minv=np.array([3.240479,-1.537150,-0.498535,-0.969256,1.875992,0.041556,0.055648,-0.204043,1.057311]).reshape(3,3)
Minv=np.transpose(Minv)
RGB=np.dot(xyz,Minv) 
np.greater(RGB,0.0001)
RGBthresh =np.greater(RGB,0.001)
RGBthresh
RGB[RGBthresh]=1.055 * RGB[RGBthres]**(1/2.4) - 0.055
RGB[np.invert(RGBthresh)] <- 12.92 * RGB[np.invert(RGBthresh)]
RGBthresh
* ((xyz - 16 / 116) / 7.787)



 * ((xyz - 16 / 116) / 7.787)



#Lab2RGB <- function(mat) {
#	# cast mat in case of a single numeric vector
#	mat <- matrix(mat, ncol=3)
#	# same spec as RGBtoLab
#	# Lab -> XYZ
#	thres1 <- 0.008856
#	thres2 <- 0.0031308
#	
#	y <- (mat[,1] + 16) / 116
#	x <- mat[,2] / 500 + y
#	z <- y - mat[,3] / 200
#	xyz <- cbind(x,y,z)
#	xyzthres <- xyz > thres1
#	xyz <- xyzthres * (xyz^3) + (!xyzthres) * ((xyz - 16 / 116) / 7.787)
#	xyz <- sweep(xyz, 2, c(0.950456,1,1.088754), "*")
#	
#	# XYZ -> RGB
#	Minv = c(3.240479,-1.537150,-0.498535,
#            -0.969256, 1.875992, 0.041556,
#             0.055648,-0.204043, 1.057311)
#    Minv <- matrix(Minv, nrow=3, byrow=TRUE)
#    RGB <- xyz %*% t(Minv)
#	RGBthres <- RGB > thres2
#	# manage NaN risk with x^a and a<1
#	RGB[RGBthres] <- 1.055 * RGB[RGBthres]^(1/2.4) - 0.055
#	RGB[!RGBthres] <- 12.92 * RGB[!RGBthres]
#	# bound in case of very small absolute <0 values, and resp. for >1 values.
#	RGB[RGB<0] <- 0
#	RGB[RGB>1] <- 1
#    return(RGB)
#}
