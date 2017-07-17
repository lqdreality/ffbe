from Descriptors import *

s1 = Stats()
s2 = Stats()
s2.update('ATK', 20)
s3 = s1 + s2
s3.print()
