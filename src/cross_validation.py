"""Subject-aware partition generator to strictly prevent patient data leakage."""

def create_subject_kfold_splits(subjects, k=5):
    unique_subjects = sorted(list(set(subjects)))
    fold_size = len(unique_subjects) // k
    folds = []
    for i in range(k):
        val_subjects = set(unique_subjects[i * fold_size : (i + 1) * fold_size] if i < k - 1 else unique_subjects[i * fold_size:])
        train_subjects = set(unique_subjects) - val_subjects
        folds.append({'train_subjects': train_subjects, 'val_subjects': val_subjects})
    return folds
