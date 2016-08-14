#!/etc/python3
"""log analyze
but what ?
"""

import sys
def dictify_logline(line):
    split_line = line.split()
    print split_line
    return {'date': split_line[0],
            'bytes_sent': split_line[0]
           }

def generate_log_report(logfile):
    report_dic = {}
    for line in logfile:
        line_dict = dictify_logline(line)
        print(line_dict)
        try:
            bytes_sent = int(line_dict['bytes_sent'])
        except ValueError:
           continue
        report_dic.setdefault(line_dict['data'],[]).append(bytes_sent)
    return report_dic

if __name__ == "__main__":
    if not len(sys.argv) > 1:
        print(__doc__)
        sys.exit(1)
    infile_name = sys.argv[1]
    try:
        infile = open(infile_name, 'r')
    except IOError:
        print("You must choose file")
        print(__doc__)
        sys.exit(1)
    log_report = generate_log_report(infile_name)
    print(log_report)
    infile.close()
