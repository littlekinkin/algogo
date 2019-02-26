
import torch
import torch.autograd as autograd
import torch.nn as nn
import torch.optim as optim

torch.manual_seed(1)


def argmax(vec):
    #1 for row max, and its index
    _, idx = torch.max(vec, 1)
    #item only for one element tensoors
    #convert to python scalars
    #and vec must be a row vector
    return idx.item()

def prepare_sequence(seq, to_ix):
    idxs = [to_ix[w] for w in seq]
    return torch.tensor(idxs, dtype=torch.long)

def log_sum_exp(vec):
    #get max socre
    max_score = vec[0, argmax(vec)]
    #expand max_score to [1, vec.size()[1]]
    max_score_broadcast = max_score.view(1, -1).expand(1, vec.size()[1])
    return max_score +\
        torch.log(torch.sum(torch.exp(vec - max_score_broadcast)))

class BC(nn.module):

    def __init__(self, vocab_size, tag_to_ix, embedding_dim, hidden_dim):
        pass


