def main():
    filename = input("Enter filename: ")
    content = read_file(filename)
    analyze_text(content)

def read_file(filename):
    with open(filename, "r") as f:
        return f.read()

def analyze_text(content):
    words = content.split()
    lines = content.split('\n')
    print(f"File contains {len(content)} characters")
    print(f"File contains {len(words)} words")
    print(f"File contains {len(lines)} lines")
    # Mer analys här senare
    
main()