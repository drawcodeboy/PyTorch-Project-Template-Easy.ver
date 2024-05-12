import torch.nn.functional as F

# 필요한 Loss Function을 구현할 것

def nll_loss(output, target):
    return F.nll_loss(output, target)
