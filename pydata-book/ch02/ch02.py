import json
from collections import defaultdict
from collections import Counter

path = 'usagov_bitly_data2012-03-16-1331923249.txt'
records = [json.loads(line) for line in open(path)]
time_zones = [rec['tz'] for rec in records if 'tz' in rec]


def get_counts(sequence):
    counts = {}
    for x in sequence:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    return counts


def get_counts2(sequence):
    counts = defaultdict(int)
    for x in sequence:
        counts[x] += 1
    return counts


def top_counts(count_dict, n=10):
    value_key_pairs = [(tz, count) for tz, count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]


counts1 = get_counts(time_zones)
# print(counts1)

counts2 = get_counts2(time_zones)
# print(counts2)

counts3 = Counter(time_zones).most_common(10)

print(top_counts(counts1))
print(top_counts(counts2))
print(counts3)
# for i in range(len(records)):
#     print(records[i])
