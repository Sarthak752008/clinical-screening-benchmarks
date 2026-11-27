"""Precision-Recall curve generation and Average Precision (AP) computation."""

def compute_pr_curve(y_true, scores, thresholds=None):
    if thresholds is None:
        thresholds = sorted(set(scores), reverse=True)
    precision_list, recall_list = [], []
    pos_count = sum(1 for y in y_true if y == 1)
    if pos_count == 0:
        return [0.0], [0.0], 0.0
    for thresh in thresholds:
        tp = sum(1 for y, s in zip(y_true, scores) if y == 1 and s >= thresh)
        fp = sum(1 for y, s in zip(y_true, scores) if y == 0 and s >= thresh)
        precision = tp / (tp + fp) if (tp + fp) > 0 else 1.0
        recall = tp / pos_count
        precision_list.append(precision)
        recall_list.append(recall)
    # Numerical integration for Average Precision
    ap = sum((recall_list[i] - (recall_list[i+1] if i+1 < len(recall_list) else 0.0)) * precision_list[i] for i in range(len(precision_list)))
    return precision_list, recall_list, abs(ap)
