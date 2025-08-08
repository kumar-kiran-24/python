import torch

tensor=torch.tensor([1,2,3,4],device = "cuda" if torch.cuda.is_available() else "cpu")
print(tensor.device)