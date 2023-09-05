def generate_custom_message(message:str, table_width=50, center_text=True):
    table_char = '─'
    corner_char = '┌┐└┘'
    border_char = '│'
    content_width = table_width - 4

    if center_text:
        message = message.center(content_width)

    top_border = f'{corner_char[0]}{table_char * (content_width - 2)}{corner_char[1]}'
    bottom_border = f'{corner_char[2]}{table_char * (content_width - 2)}{corner_char[3]}'
    message_lines = message.split('\n')
    message_box = [f'{border_char} {line.ljust(content_width - 4)} {border_char}' for line in message_lines]
    full_message = f'{top_border}\n' + '\n'.join(message_box) + f'\n{bottom_border}'

    return full_message
