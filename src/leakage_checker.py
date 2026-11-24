def check_subject_leakage(train_ids, test_ids):
    intersection = set(train_ids).intersection(set(test_ids))
    assert len(intersection) == 0, f'Patient data leakage detected: {intersection}'
