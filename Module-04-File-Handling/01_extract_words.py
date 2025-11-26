"""
Reads a text file and writes all words (one per line) to another file.
The user enters input and output file names.
"""

def extract_words(in_file, out_file):
    try:
        with open(in_file, "r", encoding="utf-8") as f_in:
            text = f_in.read()
        words = text.split()
        with open(out_file, "w", encoding="utf-8") as f_out:
            for w in words:
                f_out.write(w + "\n")
        print(f"Extracted {len(words)} words to {out_file}.")
    except FileNotFoundError:
        print("Input file not found.")


input_file = input("Enter input text file name (e.g., input.txt): ")
output_file = input("Enter output file name (e.g., words.txt): ")
extract_words(input_file, output_file)
