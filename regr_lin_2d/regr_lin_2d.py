import numpy as np

def regr_lin_2d(y,x1,x2):
  if (len(y)!=len(x1)!=len(x2)):
    raise Exception('y, x1 and x2 lenghts must be equals.')

  # number of observations n is len(y) (or len(x1) or len(x2))
  # y = b0 + b1*x1 + b2*x2

  n=len(y)

  # constructing X
  # must be in the form
  # 1 x1,1 x2,1
  # 1 x1,2 x2,2
  # 1 x1,3 x2,3
  # ...                  
  x=np.zeros(n*3).reshape(n,3)
  for i in xrange(n):
    for j in xrange(3):
      if (j==0):
        x[i,j]=1
      elif (j==1):
        x[i,j]=x1[i]
      elif (j==2):
        x[i,j]=x2[i]

  # the coeficients b0, b1, b2 will be found using B=(X'X)^-1X'y
  B=np.linalg.inv((x.T).dot(x)).dot(x.T).dot(y)

  return B.tolist()

if __name__ == "__main__":

  print
  print " Function lin_regr_2(y,x1,x2) to perform a 2d linear regression."
  print " use as:"
  print
  print " from regr_lin_2d import *"
  print " regr_lin_2d(y,x1,x2)"
  print
