"""ROC curve generation and area-under-the-curve computation."""

def compute_roc_coordinates(y_true, scores, thresholds=None):
    if thresholds is None:
        thresholds = sorted(set(scores), reverse=True)
    tpr_list, fpr_list = [], []
    pos_count = sum(1 for y in y_true if y == 1)
    neg_count = sum(1 for y in y_true if y == 0)
    if pos_count == 0 or neg_count == 0:
        return [0.0, 1.0], [0.0, 1.0], 0.5
    for thresh in thresholds:
        tp = sum(1 for y, s in zip(y_true, scores) if y == 1 and s >= thresh)
        fp = sum(1 for y, s in zip(y_true, scores) if y == 0 and s >= thresh)
        tpr_list.append(tp / pos_count)
        fpr_list.append(fp / neg_count)
    # Add bounds
    fpr_sorted, tpr_sorted = [0.0] + fpr_list + [1.0], [0.0] + tpr_list + [1.0]
    auc = sum((fpr_sorted[i] - fpr_sorted[i-1]) * (tpr_sorted[i] + tpr_sorted[i-1]) / 2 for i in range(1, len(fpr_sorted)))
    return fpr_sorted, tpr_sorted, abs(auc)
