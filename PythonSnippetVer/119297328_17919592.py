import datetime
import re
timeformat = "%Y%m%d_%H%M%S" # this is how your timestamp looks like
regex = re.compile("^ListOfFiles(\d*_\d*)")
def gettimestamp(thestring):
    m = regex.search(thestring)
    return datetime.datetime.strptime(m.groups()[0], timeformat)
list_of_filenames = [
    'ListOfFiles20111012_123717_GwUcRlmXrfCPhDSJBXE2TNEQ7h0TC7iJSnHvLxUlCQIdERLcpzw.txt',
    'ListOfFiles20111012_123742_GwRlmXrfCPhDSJBXE2TNEQ7h0TC7iJSnHvLxUlCQIdERLcpzw.txt',
    'ListOfFiles20111012_123807_PjTmt-Cd5f6ZHYO80gA608F9YCJWyM1S1KmF1rG6CvsrtFg8rCs.txt',
    'ListOfFiles20111012_123808_PjTmt-wCd5f6ZHYO80gA608F9YCJWyM1S1KmF1rG6CvsrtFg8rCs.txt',
    'ListOfFiles20111012_125217_GwRqdolmXrfCPhDSJBXE2TNEQ7h0TC7iJSnHvLxUlCQIdERLcpzw.txt',
    'ListOfFiles20111012_125307_PjTmt-wCd5f6ZHYO80gA608F9YCJWyM1S1KmF1rG6CvsrtFg8rCs.txt',
    'ListOfFiles20111012_130716_GwRqdofCPhDSJBXE2TNEQ7h0TC7iJSnHvLxUlCQIdERLcpzw.txt',
    'ListOfFiles20111012_130808_PjTmt-5f6ZHYO80gA608F9YCJWyM1S1KmF1rG6CvsrtFg8rCs.txt',
    'ListOfFiles20111012_132218_GwRqdoJBXE2TNEQ7h0TC7iJSnHvLxUlCQIdERLcpzw.txt',
    'ListOfFiles20111012_132308_PjTmt-Cd5f6ZHYO80gA608F9YCJWyM1S1KmF1rG6CvsrtFg8rCs.txt',
    'ListOfFiles20111012_133904_PjTmt-QwCd5f6ZHYO80gA608F9YCJWyM1S1KmF1rG6CvsrtFg8rCs.txt',
    'ListOfFiles20111012_135218_GwRqdorfCPhDSJBXE2TNEQ7h0TC7iJSnHvLxUlCQIdERLcpzw.txt',
]
for fn in sorted(list_of_filenames, key=gettimestamp):
    print fn