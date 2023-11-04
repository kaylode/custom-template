import torch

from theseus.base.utilities.cuda import detach, move_to


def multiclass_logits2labels(outputs, return_probs: bool = False):
    probs, outputs = torch.max(torch.softmax(outputs, dim=-1), dim=-1)

    probs = move_to(detach(probs), torch.device("cpu"))
    outputs = move_to(detach(outputs), torch.device("cpu"))

    if return_probs:
        return outputs.long().view(-1), probs
    return outputs


def multilabel_logits2labels(outputs, threshold=0.5, return_probs: bool = False):
    assert threshold is not None, "Please specify threshold value for sigmoid"
    probs = torch.sigmoid(outputs)
    outputs = outputs > threshold

    probs = move_to(detach(probs), torch.device("cpu"))
    outputs = move_to(detach(outputs), torch.device("cpu"))

    if return_probs:
        return outputs.long(), probs
    return outputs


def binary_logits2labels(outputs, threshold=0.5, return_probs: bool = False):
    assert threshold is not None, "Please specify threshold value for sigmoid"
    preds = (outputs.view(-1) > threshold).long()
    preds = move_to(detach(preds), torch.device("cpu"))
    if return_probs:
        probs = move_to(detach(outputs), torch.device("cpu"))
        return preds.long(), probs.view(-1)
    return preds


def logits2labels(
    outputs,
    label_type="multiclass",
    threshold: float = 0.5,
    return_probs: bool = False,
):
    if label_type == "multiclass":
        return multiclass_logits2labels(outputs, return_probs)
    if label_type == "multilabel":
        return multilabel_logits2labels(outputs, threshold, return_probs)
    if label_type == "binary":
        return binary_logits2labels(outputs, threshold, return_probs)
    return outputs
