#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# rrr.py - Relish Race Results
#
# Turning race results published as PDF into something useful

import pdftables
import sys
import tablib


def build_dataset(pdf):
    tables = pdftables.get_tables(pdf)
    header = []
    rows = []

    for table in tables:
        for row in table:
            if not row[0]:
                continue

            if 'position' in map(lambda x: x.lower(), row):
                header = row
                continue

            rows.append(row)

    return tablib.Dataset(header, *rows, title="Results")


def results(pdf, fmt='csv'):
    d = build_dataset(pdf)
    return getattr(d, fmt)


if __name__ == '__main__':
    print results_as_csv(open(sys.argv[1]))
