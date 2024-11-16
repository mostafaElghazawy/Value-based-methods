import torch
import torch.nn as nn
import torch.nn.functional as F

class QNetwork(nn.Module):
    """Actor (Policy) Model."""

    def __init__(self, state_size, action_size, seed):
        """Initialize parameters and build model.
        Params
        ======
            state_size (int): Dimension of each state
            action_size (int): Dimension of each action
            seed (int): Random seed
        """
        super(QNetwork, self).__init__()
        self.seed = torch.manual_seed(seed)
        
        hidden1_num=128
        
        hidden2_num=128
        
        hidden3_num=128
        
        self.fc1 = nn.Linear(state_size, hidden1_num)
        
        self.fc2 = nn.Linear(hidden1_num, hidden2_num)
        
        self.fc3 = nn.Linear(hidden2_num, hidden3_num)
        
        self.fc4 = nn.Linear(hidden3_num, action_size)
        
    def forward(self, state):
        """Network that maps state -> action values."""
        
        x = F.relu(self.fc1(state))
        
        x = F.relu(self.fc2(x))
        
        x = F.relu(self.fc3(x))
        
        output = self.fc4(x)
        
        return output