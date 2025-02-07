import glob

import pandas as pd

import torch
from torch.utils.data import Dataset
from torch_geometric.data import Batch

class CostumDataset(Dataset):
    def __init__(self, ml_method):
       self.data_location = 'Data/datasets/' + ml_method + '/'
       self.file_names = glob.glob(self.data_location + '*.pkl')
       self.ml_method = ml_method
           
    def __len__(self):
        return len(self.file_names)
    
    def __getitem__(self, index): 
        data = pd.read_pickle(self.file_names[index])
        
        if self.ml_method in ['GNN', 'GNN_plus']:
            return Batch.from_data_list(data[self.ml_method])
        
        else:
            data_list = torch.tensor(data[self.ml_method])
            X, Y = torch.stack(data_list, dim=0)

            # X = torch.tensor(data_list[0], 
            #                  requires_grad = True)
            # Y = torch.tensor(data_list[1], 
            #                  requires_grad = True)
            return X, Y
    
