

def check_gen(tutors: list, klasses: list):
    while len(tutors) > len(klasses):
        klasses.append('None')
    for name in zip(tutors, klasses):
        tuple_result = name
        yield tuple_result


if __name__ == '__main__':
    tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
    klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
    generator = check_gen(tutors, klasses)
    print(type(generator))
    # добавьте здесь доказательство, что создали именно генератор
    for _ in range(len(tutors)):
        print(next(generator))
    # next(generator)  # если раскомментировать, то должно падать в traceback по StopIteration