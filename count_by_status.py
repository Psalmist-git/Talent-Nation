def count_by_status(entries):
    counts = {}
    for entry in entries:
        counts[entry] = counts.get(entry, 0) + 1
    return counts
