from src.leakage_checker import check_subject_leakage

def test_split_integrity():
    check_subject_leakage(['P01', 'P02'], ['P03', 'P04'])
