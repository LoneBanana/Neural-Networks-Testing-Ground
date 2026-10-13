#Purpose: Understand torch registry for debugging later

import torch
from torch import nn

class Demo(nn.Module):
	def __init__(self):
		super().__init__()
		self.linear = nn.Linear(3,1)
		self.raw = nn.Parameter(torch.randn(3, requires_grad = True))
		self.p = nn.Parameter(torch.randn(3))

m = Demo()
print(m._modules.keys())
print(m._parameters.keys())
print([n for n, _ in m.named_parameters()])

"""

Big takeaway:

1. If private variable inside a class (that is subclass of nn.Module) has something like nn.Parameter(torch.randn(3)), for instance, internally a dictionary will be created

 - This dictionary, in this case named self._parameter, will contain the names of all such registered 'nn.Parameter's

"""
