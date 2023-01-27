import datetime


def logger(path):
    def __logger(old_function):
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)
            f_date = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            f_name = old_function.__name__
            f_args = args
            f_kwargs = kwargs
            log = f'Дата и время вызова функции: {f_date}\nИмя функции: {f_name}\nПозиционные аргументы: {f_args}\nИменованные аргументы: {f_kwargs}\nВозвращаемое значение: {list(result)}\n***\n'
            with open(path, 'w', encoding='utf-8') as file:
                file.write(log)
            return result
        return new_function
    return __logger


@logger('result.log')
def flat_generator(list_of_lists):
    outer_cursor = 0
    inner_cursor = 0
    while outer_cursor < len(list_of_lists):
        inner_list_len = len(list_of_lists[outer_cursor])
        if inner_list_len > inner_cursor:
            yield list_of_lists[outer_cursor][inner_cursor]
            inner_cursor += 1
        else:
            outer_cursor += 1
            inner_cursor = 0


if __name__ == '__main__':
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    flat_generator(list_of_lists_1)
