def read_txt():
    with open('numbers.txt') as f:
        numbers = f.readlines()
        numbers = numbers[0].split(",")
        for number in numbers:
            print(number)

if __name__ == '__main__':
    read_txt()