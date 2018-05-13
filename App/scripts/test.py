# Make sure to import sys
import sys

def main():
    # How to receive input
    input = sys.argv[1]

    # Test
    file = open("scripts/test.txt", "w")
    file.write(input)

    # How to output
    print("test")

main()
