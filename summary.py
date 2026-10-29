import sys
from collections import Counter

filename = sys.argv[1]

with open(filename, encoding="utf-8", errors="replace") as f:
    lines = f.readlines()

print("Total lines:", len(lines))

counts = Counter()

for line in lines:
    fields = line.split()

    # macOS log messages start after the timestamp
    # and metadata columns.
    if len(fields) > 6:
        message = " ".join(fields[6:])
        process = message.split(":", 1)[0].strip()

        if process:
            counts[process] += 1

print("Top 5:")
for item, n in counts.most_common(5):
    print(item, n)
