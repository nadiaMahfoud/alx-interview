#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics for lines with the
specified format.

Format: <IP> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
After every 10 lines or a keyboard interruption (CTRL + C), print stats:

Total file size: <total size>
Lines by status code (200, 301, 400, 401, 403, 404, 405, 500):
<status code>: <number> (in ascending order)

Line list format: [<IP>, -, [<date>], "GET /projects/260 HTTP/1.1",
<status code>, <file size>]
"""

import sys

total_size = 0
count = 0
# Initialize a dictionary to store the count of each status code
status_codes_dict = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
                     '404': 0, '405': 0, '500': 0}

try:
    for line in sys.stdin:
        line_list = line.split(" ")

        if len(line_list) > 4:
            status_code = line_list[-2]
            file_size = int(line_list[-1])

            # Check if the status code exists in the dictionary and
            # increment its count
            if status_code in status_codes_dict:
                status_codes_dict[status_code] += 1

                # Update total size
            total_size += file_size

            # Update count of lines processed
            count += 1

            # Print statistics after every 10 lines
        if count == 10:
            count = 0  # Reset count
            print('File size: {}'.format(total_size))

            # Print out status code counts
            for key, value in sorted(status_codes_dict.items()):
                if value != 0:
                    print('{}: {}'.format(key, value))

except Exception as err:
    pass

finally:
    # Print final statistics
    print('File size: {}'.format(total_size))
    for key, value in sorted(status_codes_dict.items()):
        if value != 0:
            print('{}: {}'.format(key, value))
