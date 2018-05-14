# Make sure to import sys
import sys
import json

def main():
    # How to receive input
    input = sys.argv[1]

    # Test
    file = open("scripts/test.txt", "w")
    testString = {"test" : 1}
    testJSON = json.dumps(testString)
    file.write(input)

    # How to output
    print(testJSON)
    sys.stdout.flush()

main()
