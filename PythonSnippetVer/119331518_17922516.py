from collections import defaultdict
lookup = defaultdict(dict)
lookup['name']['John'] = 1
lookup['name']['Jane'] = 2
lookup['name']['Joe'] = 3
lookup['gender']['Male'] = 1
lookup['gender']['Female'] = 2
lookup['country']['Japan'] = "jp"
lookup['country']['China'] = "ch"

print lookup['name']['Jane']
print lookup['gender']['Female']
print lookup['country']['China']