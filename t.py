#!/usr/bin/env python3

import logging
logging.basicConfig(level=logging.DEBUG)

import pymonetdb

#conn = pymonetdb.connect('demo', port=44001, replysize=1, binary=False)
conn = pymonetdb.connect('monetdb://127.0.0.1:50000/demo')
c = conn.cursor()

c.execute("SELECT value from sys.generate_series(0,9); SELECT 100 + value as i, 1000 + value as j FROM sys.generate_series(0,100_000)")

go = True
while go:
    print('RESULT SET', 50 * '-')
    for row in c:
        print(row)
    go = c.nextset()
