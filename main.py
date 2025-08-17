import os
import argparse
from collections import Counter

def main():
    parser = argparse.ArgumentParser(
        description="CLI File Analyzer - Analyze text files for statistics and insights."
    )
    parser.add_argument(
        "filename",
        help="Path to the text file you want to analyze (e.g., file.txt, script.py, notes.md)."
    )
    parser.add_argument(
        "-n", "--top", type=int, default=10,
        help="Number of top most common words to display (default: 10)."
    )
    
    args = parser.parse_args()
    filename = args.filename

    # Check if file exists
    if not os.path.isfile(filename):
        print(f"Error: File '{filename}' not found.")
        return

    # Show file size
    file_size = os.path.getsize(filename)
    print(f"\nAnalyzing '{filename}' ...")
    print(f"File size: {file_size} bytes\n")

    # Read file
    content = read_file(filename)
    if not content:
        print("No content to analyze.")
        return

    # Analyze content
    analyze_text(content, args.top)


def read_file(filename):
    encodings = ["utf-8", "utf-8-sig", "latin-1", "cp1252"]
    for encoding in encodings:
        try:
            with open(filename, "r", encoding=encoding) as f:
                return f.read()
        except UnicodeDecodeError:
            continue
    print(f"Could not decode file '{filename}' with supported encodings.")
    return ""


def analyze_text(content, top_n):
    words = content.split()
    lines = content.split('\n')

    print("=" * 50)
    print("          FILE ANALYSIS RESULTS")
    print("=" * 50)
    print(f"Characters: {len(content)}")
    print(f"Words: {len(words)}")
    print(f"Lines: {len(lines)}")

    # Word frequency analysis
    word_count = Counter(
        word.lower().strip('.,!?";:-()[]{}') for word in words if word.strip()
    )

    if not word_count:
        print("No words found in file.")
        return

    print(f"Unique words: {len(word_count)}")

    # Most & least common words
    most_common = word_count.most_common(1)[0]
    least_common = min(word_count.items(), key=lambda x: x[1])

    print(f"Most common word: '{most_common[0]}' ({most_common[1]} times)")
    print(f"Least common word: '{least_common[0]}' ({least_common[1]} time{'s' if least_common[1] > 1 else ''})")

    # Top N most common words
    print(f"\nTop {top_n} most common words:")
    for word, freq in word_count.most_common(top_n):
        print(f"  {word:<15} {freq}")

    # Reading time estimation
    reading_time = len(words) / 200  # 200 wpm
    print(f"\nEstimated reading time: {reading_time:.1f} minutes")

    print("=" * 50)


if __name__ == "__main__":
    main()
