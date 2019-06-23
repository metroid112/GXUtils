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


def main():
    print_start()
    command = choose_command()
    # For Each
    if command == 1:
        pass
    # New
    if command == 2:
        print('Command is new')
        core.command(command)


if __name__ == '__main__':
    main()
