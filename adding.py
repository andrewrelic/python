import sys

class adding:
    def add(self, number):
        return number + 2

# Create an instance of the adding class
addition = adding()

if len(sys.argv) > 1:
    input_num = int(sys.argv[1])

print(addition.add(input_num))
