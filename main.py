def main():
    filename = input("Enter filename: ")
    content = read_file(filename)
    analyze_text(content)

def read_file(filename):
    with open(filename, "r") as f:
        return f.read()

def analyze_text(content):
    print(f"File contains {len(content)} characters")
    # Mer analys här senare
    
main()