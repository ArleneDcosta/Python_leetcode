
def solution(messages, width, userWidth):
    # Start with the top border
    result = ["+" + "*" * (width) + "+"]

    # Process each message
    for message in messages:
        user = message[0]
        text = message[1]

        # Split the message into words
        words = text.split()
        current_line = ""

        for word in words:
            #Check if there is space in current line for the word
            if len(current_line) + len(word) + (1 if current_line else 0) > userWidth:
                # Process the current line
                if user == "1":
                    result.append(f"|{current_line.ljust(userWidth)}{' ' * (width - userWidth)}|")
                else:
                    result.append(f"|{' ' * (width  - userWidth)}{current_line.rjust(userWidth)}|")

                # Start a new line with the word
                current_line = word
            else:
                if current_line:
                    current_line += " " + word
                else:
                    current_line = word

        # Process any remaining text in current_line
        if current_line:
            if user == "1":
                result.append(f"|{current_line.ljust(userWidth)}{' ' * (width  - userWidth)}|")
            else:
                result.append(f"|{' ' * (width  - userWidth)}{current_line.rjust(userWidth)}|")

    # End with the bottom border
    result.append("+" + "*" * (width) + "+")

    return result


if __name__ == '__main__':
    print(solution(messages = [["1", "Hello how r u"], ["2", "good ty"], ["2", "u"], ["1", "me too bro"]], width = 15 ,userWidth = 5))
