"""This is the entry point of the program."""


def create_box(height, width, character):
    box = ''
    for h in range(height):
        row = ''
        for w in range(width):
            row += character    
        row += '\n'
        box += row
    return box


if __name__ == '__main__':
    create_box(3, 4, '*')
