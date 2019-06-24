import core


def print_start():
    print('Welcome to GxUtils 0.1')
    print('======================')
    print()


def choose_command():
    print('Choose your command:')
    print('[1] For Each')
    print('[2] New')
    try:
        command = int(input('Command: '))
        return command
    except Exception as exception:
        print('Wrong command', exception)
        return choose_command()


def choose_table():
    return input('Table name: ')


def main():
    core.descartes(['form'])
    print_start()
    command = choose_command()
    # For Each
    if command == 1:
        pass
    # New
    if command == 2:
        print('New Command')
        table = choose_table()
        print(core.command_new(table))


if __name__ == '__main__':
    main()
