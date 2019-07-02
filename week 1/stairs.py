import sys

num_steps = int(sys.argv[1])

result = ""

for i in range(1, num_steps+1):

    result += " "*(num_steps-i)
    result += "#"*i

    result += "\n"

print(result)
