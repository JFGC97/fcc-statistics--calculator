import numpy as np

def calculate(lista):
  size=len(lista)
  if size==9:
    ar=np.array(lista).reshape(3,3)
    return      {
                'mean':[list(ar.mean(axis=0)), list(ar.mean(axis=1)), ar.mean()],
                'variance':[list(ar.var(axis=0)),list(ar.var(axis=1)),ar.var()],
                'standard deviation':[list(ar.std(axis=0)),list(ar.std(axis=1)),ar.std()],
                'max':[list(ar.max(axis=0)),list(ar.max(axis=1)),ar.max()],
                'min':[list(ar.min(axis=0)),list(ar.min(axis=1)),ar.min()],
                'sum':[list(ar.sum(axis=0)),list(ar.sum(axis=1)),ar.sum()]
                }
  else:
    return 'ValueError: List must contain nine numbers'


