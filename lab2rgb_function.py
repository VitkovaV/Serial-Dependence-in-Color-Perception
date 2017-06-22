# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 13:35:49 2017

@author: toelch
"""

def lab2rgb(rgb):
    thres1 = 0.008856
    thres2 = 0.0031308
    y=(rgb[0]+16)/116
    x=rgb[1]/500+y
    z= y-rgb[2]/200        
    xyz=(x,y,z)
    xyzthresh = [1 if x>0.008856 else 0 for x in xyz]
    xyz2 = [a*b**3 for a,b in zip(xyzthresh,xyz)]+
    return(xyz);




alle=(1,1,1)
alle[2]
xyz=lab2rgb(alle)
xyzthresh=[1 if x>0.008856 else 0 for x in kick ]
xyzthresh*xyz

xyz2 = [a*b**3 for a,b in zip(xyzthresh,xyz)]
xyzthresh_inv=[1-i for i in xyzthresh] 
xyz3 = [a*b**3 for a,b in zip(xyzthresh,xyz)]* ((xyz - 16 / 116) / 7.787)



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
