def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("String lengths must be the same")
    return len([1 for (a,b) in zip(strand_a, strand_b) if a != b])
