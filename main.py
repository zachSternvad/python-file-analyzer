def main():
    filename = input("Enter filename: ")
    content = read_file(filename)
    analyze_text(content)

def read_file(filename):
    encodings = ["utf-8", "utf-8-sig", "latin-1", "cp1252"]
    for encoding in encodings:
        try:
            with open(filename, "r", encoding=encoding) as f:
                return f.read()
        except UnicodeDecodeError:
            continue
    print(f"Could not decode file '{filename}' with any encoding")
    return ""

def analyze_text(content):
    words = content.split()
    lines = content.split('\n')
    print(f"File contains {len(content)} characters")
    print(f"File contains {len(words)} words")
    print(f"File contains {len(lines)} lines")
    
    # Word frequency
    word_count = {}
    for word in words:
        word = word.lower().strip('.,!?";')
        word_count[word] = word_count.get(word, 0) + 1
        
    print(f"Total unique words: {len(word_count)}")
    print(f"Sample words: {list(word_count.items())[:5]}")
        
    # Most common word
    most_common = max(word_count, key=word_count.get)
    print(f"Most common word is: '{most_common}' it appears {word_count[most_common]} times.")    
main()