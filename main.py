import datetime
import os


time_log = datetime.datetime.now()


def decorator(old_fucntion):

    def new_function(*args, **kwargs):
        result = old_fucntion()
        with open('log.txt', 'a', encoding='utf-8') as link:
            link.writelines(f'Время записи:{time_log}\n'
                            f'Имя функции: {old_fucntion.__name__}\n'
                            f'Аргументы: {args}, {kwargs}\n'
                            f'Возвращаемое значение: {result}\n')
        print(f'Log файл рассполложен: {os.getcwd()}')
        return result

    return new_function()


def decor_decorator(old_fucntion):

    def new_fucntion(*args, **kwargs):
        result = old_fucntion(decorator)
        return result

    return new_fucntion()


def selecting_folder():
    user_input = input('Куда сохранить файлы:\n'
                       'folder - для просмотра выбранного пути\n'
                       'change - для смены пути (введите абсолютный путь)\n')
    if user_input == 'folder':
        print(f'Путь для сохранения файлов:\n{os.getcwd()}')
        user_input = input('Введите:\nсonfirm - для подтверждения пути\nback - для возврата в предыдущие меню\n')
        if user_input == 'confirm':
            return f'Файлы будут сохранены в {os.getcwd()}'
        elif user_input == 'back':
            return selecting_folder()
    elif user_input == 'change':
        user_input = input('Введите путь для сохранения файлов:\n')
        os.chdir(user_input)
        print(f'Файлы будут сохранены в {os.getcwd()}')
        user_input = input('Введите:\nсonfirm - для подтверждения пути\nback - для возврата в предыдущие меню\n')
        if user_input == 'confirm':
            return f'Файлы будут сохранены в {os.getcwd()}'
        elif user_input == 'back':
            return selecting_folder()


decorator(selecting_folder)


