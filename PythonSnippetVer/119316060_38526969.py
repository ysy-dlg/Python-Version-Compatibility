import os
if os.path.exists('../a.txt'):
    print 'Exists'
    os.symlink('../a.txt', 'a.txt')
else:
    print 'Does not exist'