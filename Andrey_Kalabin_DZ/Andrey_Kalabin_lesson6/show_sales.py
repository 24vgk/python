import sys


def main(argv):
    with open('bakery.csv', 'r', encoding='utf-8') as fr:
        program, *args = argv
        result = [i.strip() for i in fr]
        if len(args) == 0:
            for line in fr:
                print(line.strip())
        elif len(args) == 1:
            print(*result[int(args[0]) - 1:], sep='\n')
        elif len(args) == 2:
            print(*result[int(args[0]) - 1: int(args[1])], sep='\n')


main(sys.argv)