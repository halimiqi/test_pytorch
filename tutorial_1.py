from __future__ import print_function
import torch

x = torch.ones(2,2, requires_grad=True)
y= x + 2
z = y*y*3
out = z.mean()

print(x)
print(z,out)
