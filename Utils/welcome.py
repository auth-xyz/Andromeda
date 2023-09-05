def generate_custom_message(message:str, table_width=50, center_text=True):
    # Define the table characters
    table_char = '─'
    corner_char = '┌┐└┘'
    border_char = '│'
    inner_char = ' '

    # Calculate the width for the message box
    content_width = table_width - 4  # 2 characters for each side border

    # Center the text if required
    if center_text:
        message = message.center(content_width)

    # Create the top and bottom border of the table
    top_border = f'{corner_char[0]}{table_char * (content_width - 2)}{corner_char[1]}'
    bottom_border = f'{corner_char[2]}{table_char * (content_width - 2)}{corner_char[3]}'

    # Create the message box with the message inside
    message_lines = message.split('\n')
    message_box = [f'{border_char} {line.ljust(content_width - 4)} {border_char}' for line in message_lines]

    # Create the final message with borders
    full_message = f'{top_border}\n' + '\n'.join(message_box) + f'\n{bottom_border}'

    return full_message
