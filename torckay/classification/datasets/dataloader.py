import numpy as np
import torch
from torch.utils.data.sampler import WeightedRandomSampler

def class_imbalance_sampler(labels):
    class_count = torch.bincount(labels.squeeze())
    class_weighting = 1. / class_count
    sample_weights = np.array([class_weighting[t] for t in labels.squeeze()])
    sample_weights = torch.from_numpy(sample_weights)
    sampler = WeightedRandomSampler(sample_weights, len(sample_weights))
    return sampler

class CSVLoader(torch.utils.data.DataLoader):
    def __init__(self, dataset, batch_size, train=True, **kwargs):

        if train:
            labels = torch.LongTensor(dataset.classes_dist).unsqueeze(1)
            sampler = class_imbalance_sampler(labels)
        else:
            sampler = None
            
        super(CSVLoader, self).__init__(
            dataset,
            batch_size=batch_size,
            collate_fn = dataset.collate_fn,
            sampler=sampler,
            **kwargs
        )