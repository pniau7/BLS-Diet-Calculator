from os import system, name


def clear():
    system('cls' if name == 'nt' else 'clear')


def title():
    size = 80
    clear()
    print('-'*size)
    print('Calorie Calculator and Macronutrients Distribution 1.0'.center(size))
    print()
    print('Based on: Bigger, Leaner, Stronger by Michael Matthews'.center(size))
    print()
    print(f'\033[4mScript by: Pierre Niau\033[m'.center(size))
    print('-'*size)
    print()


def pause():
    print()
    if name == 'nt':
        system('pause')
    else:
        input('Press ENTER to continue...')


def read(fname):
    try:
        file = open(fname, 'rt')
        file.close()
    except FileNotFoundError:
        return False
    return True


def create(fname):
    try:
        print(f'Creating {fname}')
        file = open(fname, 'wt')
        file.close()
    except:
        print('Failed to create file.')
        pause()
    else:
        print('File successfully created.')


def write(fname, arg, string):
    try:
        file = open(fname, arg)
        file.write(string)
        file.close()
    except:
        print('Failed to write on the file.')
        pause()


def readYN(msg):
    while True:
        try:
            out = str(input(msg)).strip().upper()
            if out in 'YN' and out != '':
                break
            else:
                print('Type a valid option: Y or N')
        except (TypeError, ValueError):
            print('Type a valid option: Y or N')
        except KeyboardInterrupt:
            print('User ended the program.')
            exit()
        except:
            print('Unexpected error. Exiting the program.')
            exit()
    return out


def readOpt(msg):
    while True:
        try:
            opt = int(input(msg))
            if 0 < opt < 3:
                return opt
                break
            else:
                print('Choose a valid option.')
        except (ValueError, TypeError):
            print('Choose a valid option.')
        except KeyboardInterrupt:
            print('\nUser ended the program.')
            exit()
        except:
            print('Unexpected error. Exiting the program')
            exit()


def readFloat(obj, msg):
    while True:
        try:
            num = float(input(msg))
            if num > 0:
                return num
                break
            else:
                print(f'Type a valid {obj}!')
        except (ValueError, TypeError):
            print(f'Type a valid {obj}!')
        except KeyboardInterrupt:
            print('\nUser ended the program.')
            exit()
        except:
            print('Unexpected error. Exiting the program')
            exit()