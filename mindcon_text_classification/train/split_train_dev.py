import random


def split_train_dev(data_file):
    with open(data_file, 'r') as f:
        reader = f.readlines()
        random.shuffle(reader)
    with open("train.txt","w") as f1, open("dev.txt","w") as f2:
        for index, line in enumerate(reader):
            if index <= 0.8 * len(reader):
                f1.write(line)
            else:
                f2.write(line)

if __name__ == "__main__":
    split_train_dev("./data.txt")
