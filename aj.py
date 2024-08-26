from collections import Counter
def min_removals_to_equal_frequency(s: str) -> int:
    char_freq = Counter(s)
    freq_count = Counter(char_freq.values())
    unique_freqs = list(freq_count.keys())
    min_removals = float('inf')
    for target_freq in range(1, max(unique_freqs) + 1):
        removals = 0
        for freq, count in freq_count.items():
            if freq > target_freq:
                removals += (freq - target_freq) * count
            elif freq < target_freq:
                removals += freq * count

        min_removals = min(min_removals, removals)
        
    return min_removals