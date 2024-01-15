input_file = open(r'dear_prudence.txt', 'r')
line = input_file.read()
#input_file.write("----------------------------\n")
input_file.close()
new_file = open(r'clear.txt', 'a')
new_file.write(line)


