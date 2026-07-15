def input_and_print():
    exit_str = 'q'
    input_str = input(f'Введите текст({exit_str} для выхода): ')
    if input_str == exit_str:
        return
    print(f'Вы ввели: {input_str}')
    input_and_print()

input_and_print()
