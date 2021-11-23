#!/bin/python3
from datetime import datetime as dt


fmt = '%a %d %b %Y %H:%M:%S %z'
sec = (dt.strptime("Sun 10 may 2015 13:54:36 -0700", fmt) - dt.strptime("Sun 10 May 2015 13:54:36 -0000", fmt)).total_seconds()
print(str(abs(int(sec))))