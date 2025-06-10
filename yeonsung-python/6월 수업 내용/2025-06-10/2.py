in_file = None
in_str = ""
in_file = open("", "r", encoding="UTF-8")

is_str = in_file.readline()
print(in_str, end='')

in_file.close()