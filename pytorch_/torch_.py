import torch
print(torch.__version__)

#tensor scalar
sc=torch.tensor(7)
print(sc)
print(sc.ndim)#find the number of dimsessions
print(sc.item())#return the  in tensor varible

#vector
ve=torch.tensor([7,7])
# Check shape of vector
print(ve.shape)
print(ve)

#matrix
ma=torch.tensor([[[1, 2, 3],
                        [3, 6, 9],
                        [2, 4, 5]]])
print(ma.ndim)
print(ma.shape)

#range of the tensor
one_to_five = torch.arange(start=1, end=6, step=1)
print(one_to_five)

#tensor data types
dt=torch.tensor([.8,.9,.8])
print(dt.dtype)#return the data type(float32)
#parameters
datat=torch.tensor([0.9,0.8],dtype=torch.float16,
                   device=None,#in which twnsor is on
                   requires_grad=False
                   )
print(datat.dtype)



              


