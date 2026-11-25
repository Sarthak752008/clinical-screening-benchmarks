from src.cross_validation import create_subject_kfold_splits

def test_subject_split_disjointness():
    subjects = [f'PATIENT_{i:03d}' for i in range(50)]
    folds = create_subject_kfold_splits(subjects, k=5)
    for fold in folds:
        intersection = fold['train_subjects'].intersection(fold['val_subjects'])
        assert len(intersection) == 0, f'Subject leakage found: {intersection}'
