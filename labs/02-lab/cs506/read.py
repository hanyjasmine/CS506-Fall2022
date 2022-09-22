import csv 

def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    res = []
    MONTHS = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
    
    with open(csv_file_path) as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if row[0] in MONTHS:
                sub = [int(row[i]) for i in range(1, len(row))]
                row = [row[0]] + sub
            else:
                row = [int(row[i]) for i in range(len(row))]
            res.append(row)
    return res
