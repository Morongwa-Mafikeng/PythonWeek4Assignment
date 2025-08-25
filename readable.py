#reading from a file readable
with open('readable.txt', 'r') as f:
    data = f.read()
    print(data)
#modifying a file readable
with open("readable.txt", "w") as f:
    data = f.write("Everything is possible with python")
#handling exceptions of a file

filename = (input("Enter file name"))
try:
    with open(filename, 'r') as f:
        data = f.read()
except FileNotFoundError:
    print("File cannot be read as it does not exist")
