#!/usr/bin/python3
"""a script that reads stdin line by line and computes metrics"""


import sys
import signal

def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)

status_codes = {'200', '301', '400', '401', '403', '404', '405', '500'}
file_sizes = []
status_count = {code: 0 for code in status_codes}

def print_stats():
    total_size = sum(file_sizes)
    print(f"Total file size: {total_size}")
    for code in sorted(status_codes, key=int):
        if status_count[code] > 0:
            print(f"{code}: {status_count[code]}")

signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) != 10:
            continue

        ip, _, _, date, _, method, path, _, status, size = parts

        try:
            file_size = int(size)
            status_code = status.strip()
            if status_code in status_codes:
                file_sizes.append(file_size)
                status_count[status_code] += 1
        except ValueError:
            continue

        if len(file_sizes) == 10:
            print_stats()
            file_sizes = []
except KeyboardInterrupt:
    print_stats()
