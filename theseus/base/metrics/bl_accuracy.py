from typing import Any, Dict

import numpy as np
from sklearn.metrics import balanced_accuracy_score

from theseus.base.metrics.metric_template import Metric
from theseus.base.utilities.logits import logits2labels


def compute_multiclass(outputs, targets, index):
    correct = 0
    sample_size = 0
    for i, j in zip(outputs, targets):
        if j == index:
            sample_size += 1
            if i == j:
                correct += 1
    return correct, sample_size


class BalancedAccuracyMetric(Metric):
    """
    Balanced Accuracy metric for classification
    """

    def __init__(self, label_type: str = "multiclass", **kwargs):
        super().__init__(**kwargs)
        self.type = label_type
        self.threshold = kwargs.get("threshold", 0.5)
        self.reset()

    def update(self, outputs: Dict[str, Any], batch: Dict[str, Any]):
        """
        Perform calculation based on prediction and targets
        """
        outputs = outputs["outputs"]
        targets = batch["targets"]
        outputs = logits2labels(outputs, label_type=self.type, threshold=self.threshold)

        outputs = outputs.detach().cpu()
        targets = targets.detach().cpu().view(-1)

        self.outputs += outputs.numpy().tolist()
        self.targets += targets.numpy().tolist()

    def reset(self):
        self.outputs = []
        self.targets = []

    def get_all_unique_id(self):
        self.unique_ids = np.unique(self.targets)

    def value(self):
        self.get_all_unique_id()

        self.corrects = {str(k): 0 for k in self.unique_ids}
        self.total = {str(k): 0 for k in self.unique_ids}
        if self.type == "binary":
            values = balanced_accuracy_score(self.targets, self.outputs)
        else:
            # Calculate accuracy for each class index
            for i in self.unique_ids:
                correct, sample_size = compute_multiclass(self.outputs, self.targets, i)
                self.corrects[str(i)] += correct
                self.total[str(i)] += sample_size
            each_acc = [
                self.corrects[str(i)] * 1.0 / (self.total[str(i)])
                for i in self.unique_ids
                if self.total[str(i)] > 0
            ]

            # Get mean accuracy across classes
            values = sum(each_acc) / len(self.unique_ids)

        return {"bl_acc": values}
