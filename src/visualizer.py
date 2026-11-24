def print_confusion_matrix(matrix, labels):
    print('       ' + '  '.join(f'{l[:4]:>4}' for l in labels))
    for i, row in enumerate(matrix):
        print(f'{labels[i][:4]:>4}: ' + '  '.join(f'{v:>4}' for v in row))
