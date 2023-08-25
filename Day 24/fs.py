file = open("./Python 1-100/Day 24/fs.txt")
content = file.read()
print(content)
file.close()


with open("./Python 1-100/Day 24/fs.txt") as w_file:
    w_content = w_file.read()
    print(w_content)

with open("./Python 1-100/Day 24/fs.txt", mode="w") as r_file:
    r_file.write("Hello There Two!")

with open("./Python 1-100/Day 24/fs.txt", mode="a") as a_file:
    a_file.write("\nNew Hello There!")
