"""
Small script to try debugging with pdb.
You can run with:
python -m pdb 04_debugger_demo.py
"""

def compute_average(numbers):
    total = 0
    count = 0
    for n in numbers:
        total += n
        count += 1
    if count == 0:
        return 0
    return total / count


raw = input("Enter numbers separated by space: ")
try:
    nums = [float(x) for x in raw.split()]
    avg = compute_average(nums)
    print("Average =", avg)
except ValueError:
    print("Please enter only numbers.")
