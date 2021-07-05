def log_it(*args):
    path = r'C:\temp\log_it.txt'

    with open(path, 'a') as f:
        for line in args:
            f.write(line)
            f.write(' ')

        f.write('\n')
    return 0


log_it('Starting processing forecasting')
log_it('ERROR', 'Not enough data', 'invoices', '2020')
