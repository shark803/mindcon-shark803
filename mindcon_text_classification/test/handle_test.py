import random


def handle_test(data_file):
    with open(data_file, 'r') as f:
        reader = f.readlines()
    with open("test.txt","w") as f:
        for index, line in enumerate(reader):
            f.write("0,"+line)

if __name__ == "__main__":
    handle_test("./test.txt")
