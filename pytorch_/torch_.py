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
                   device=None,#in which device tensor is on
                   requires_grad=False
                   )
print(datat.dtype)
datat1=torch.tensor([1,2,3],dtype=torch.int32)
print(f"Device tensor is on{datat1.device}")    

#manipulating Tensors(Tensors Operations)
tensor=torch.tensor([1,2,3],dtype=torch.int16)
addition=tensor+10#retuen[11,12,13]
add_method=torch.add(tensor,10)
substract=tensor-1#return[0,1,2]
#like method mul,div,sub

#Matrix mulptiplication
tensor2=torch.tensor([[[1,2,3],
                     [1,2,3],
                     [1,2,3]]])
matrix_mul=torch.matmul(tensor2,tensor2)
print(matrix_mul)

#methods in tensor
print(torch.max(tensor))#max method
print(torch.mean(tensor.to(torch.float32)))  #mean method
print(torch.sum(tensor))#sum method

#postion of min and max values
print(tensor.argmin())#return the postion of the mean value
print(tensor.argmax())#return the postion of the max value

# #reshaping ,stacking,squeezing and unsqueezing in tensors
tensor=torch.tensor([1,2,3,4,5,6,7,8],dtype=torch.int16)
reshaped=tensor.reshape(2,4)
print(reshaped)

#stacks
stack_=torch.stack([tensor,tensor,tensor])
print(stack_)

#squeeze-remove all single dimesions from a target tensor
print(f"squezed tensor:{stack_.squeeze()}")

#unsqueezing add the single dimessions to target tensor
print(f"unsqueezed:{stack_.unsqueeze()}")

#permuting-rearranges the dimensions of a targets tensors in specifed order
x=torch.rand(size=(224,224,3))#(hieght,width,color_chanels)
x_permute=x.permute([2,0,1])
print(f"orginal size of x:{x.shape}")
print(f"perumte of x{x_permute.shape}")

#indexing in pytorch
tensor2=torch.arange(1,10).reshape(1,3,3)
print(tensor2)
print(f"indexing:{tensor2[0][0][0]}")
print(f"indexing {tensor2[0][0]}")

#Reproductivity in pytorch
#Random Seed-choose the same random numbers when every time code wiil excute
torch.manual_seed(42)
random_a=torch.rand(3,4)
random_b=torch.rand(3,4)
print(random_a==random_b)#retuen false
print(random_a)


torch.manual_seed(42)
random_c=torch.rand(3,4)

torch.manual_seed(42)
random_d=torch.rand(3,4)
print(random_c==random_d)#return true
