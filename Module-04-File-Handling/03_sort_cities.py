"""
Reads city names from a text file (one city per line),
sorts them alphabetically, and writes to an output file.
"""

def sort_cities(in_file, out_file):
    try:
        with open(in_file, "r", encoding="utf-8") as f_in:
            cities = [line.strip() for line in f_in if line.strip()]
        cities.sort()
        with open(out_file, "w", encoding="utf-8") as f_out:
            for city in cities:
                f_out.write(city + "\n")
        print(f"Sorted {len(cities)} cities and saved to {out_file}.")
    except FileNotFoundError:
        print("Input file not found.")


input_file = input("Enter input file name with city names: ")
output_file = input("Enter output file name for sorted cities: ")
sort_cities(input_file, output_file)
