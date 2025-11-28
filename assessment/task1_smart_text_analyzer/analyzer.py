from collections import Counter

def analyze_text(text):
    words = text.split()
    word_count = len(words)
    average_word_length = round(sum(len(w) for w in words) / word_count, 2)

    max_length = max(len(w) for w in words)
    longest_words = [w for w in words if len(w) == max_length]

    word_frequency = Counter(w.lower() for w in words)

    return {
        "word_count": word_count,
        "average_word_length": average_word_length,
        "longest_words": longest_words,
        "word_frequency": dict(word_frequency)
    }

if __name__ == "__main__":
    # Example usage
    sample_text = "The quick brown fox jumps over the lazy dog the fox"
    result = analyze_text(sample_text)
    print(result)
