import sys


def main(argv):
    program, *args = argv
    result = args
    return result


with open('bakery.csv', 'a+', encoding='utf-8') as fr:
    a = main(sys.argv)
    fr.writelines(f'{main(sys.argv)[0]}\n')