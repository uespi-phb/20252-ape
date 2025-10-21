
def clear_screen():
    print('\033c', end='')


def break_lines(n):
    print('\n' * n, end='')


def line(width):
    return '-' * width


def print_line(width):
    print(line(width))


def print_title(title, new_lines=0):
    print(title)
    print_line(len(title))
    break_lines(new_lines)
    

def wait_key(prompt, new_lines=0):
    break_lines(new_lines)
    input(prompt)
