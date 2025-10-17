import sys
import os
import shlex

# ANSI colors
RED = "\033[31m"
RESET = "\033[0m"
YELLOW = "\033[33m"
GREEN = "\033[32m"
BOLD = "\033[1m"
UNDERLINE = "\033[4m"

def tokenizer(code):
    tokens = []
    keywords = ["PRINT", "GOTO", "VAR"]

    with open(code, 'r') as file:
        lines = file.readlines()

    for index, line in enumerate(lines, start=1):
        # Skip empty lines
        if not line.strip():
            continue

        individual_line_tokens = []

        # Detect comments
        if line.strip().startswith("//"):
            individual_line_tokens.append(["COMMENT", line.strip()])
            tokens.append(individual_line_tokens)
            continue

        try:
            parts = shlex.split(line, posix=False)
        except ValueError:
            print(f"{RED}Error{RESET} on line {index}: Unclosed string literal")
            print(f"{index} | {line.strip()}")
            print(" " * (len(str(index)) + 3) + "^")
            return

        for key in parts:
            if key in keywords:
                individual_line_tokens.append(["KEYWORD", key])
            elif key.startswith('"') and key.endswith('"'):
                individual_line_tokens.append(["STRING", key.strip('"')])
            elif key.isdigit():
                individual_line_tokens.append(["INTEGER", int(key)])
            elif key == "=":
                individual_line_tokens.append(["OPERATOR", key])
            elif key.isalpha():
                individual_line_tokens.append(["INDENIFIER", key])
            else:
                print(f"{RED}Error{RESET} on line {index}: Unknown syntax '{key}'")
                print(f"{index} | {line.strip()}")
                print(" " * (len(str(index)) + 3) + "^")
                return

        tokens.append(individual_line_tokens)

    run_program(tokens)


def run_program(tokens):
    index = 0
    variables = {}
    while index < len(tokens):
        individual_line_token = tokens[index]

        if not individual_line_token:
            index += 1
            continue

        first_token = individual_line_token[0]
        if first_token[0] not in ("KEYWORD", "COMMENT"):
            error_line = first_token[1]
            print(f"\n{RED}Error{RESET} on line {index + 1}: Unexpected start of line")
            print(f"{index + 1} | {RED}{error_line}{RESET}")
            print(" " * (len(str(index + 1)) + 3) + "^")
            return

        keyword = first_token[1].upper()
        # ------[ VARIABLES ]------
        if keyword == "VAR":
            print(individual_line_token)
        # ------[ PRINT ]------
        if keyword == "PRINT":
            if len(individual_line_token) <= 1:
                print(f"\n{RED}Error{RESET} on line {index + 1}: Incomplete statement")
                print(f"{index + 1} | {' '.join(str(tok[1]) for tok in individual_line_token)}")
                print(" " * 10 + "^")
                return

            arg_token = individual_line_token[1]
            if arg_token[0] != "STRING":
                print(f"\n{RED}Error{RESET} on line {index + 1}: Wrong argument type.")
                print(f"{index + 1} | {' '.join(str(tok[1]) for tok in individual_line_token)}")
                print(" " * 10 + "^")
                return

            print(arg_token[1])

        # ------[ GOTO ]------
        elif keyword == "GOTO":
            if len(individual_line_token) <= 1:
                print(f"\n{RED}Error{RESET} on line {index + 1}: Incomplete statement")
                print(f"{index + 1} | {' '.join(str(tok[1]) for tok in individual_line_token)}")
                print(" " * 10 + "^")
                return

            arg_token = individual_line_token[1]
            if arg_token[0] != "INTEGER":
                print(f"\n{RED}Error{RESET} on line {index + 1}: Wrong argument type.")
                print(f"{index + 1} | {' '.join(str(tok[1]) for tok in individual_line_token)}")
                print(" " * 10 + "^")
                return

            index = int(arg_token[1])
            continue

        index += 1

    print(f"\n{GREEN}Finished executing file.{RESET}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"{RED}> Error:{RESET} You need to provide a .kx file.")
        sys.exit()

    file = sys.argv[1]

    if not os.path.exists(file):
        print(f"{RED}> Error:{RESET} File does not exist.")
        sys.exit()

    if not file.endswith(".kx"):
        print(f"{RED}> Error:{RESET} Invalid file type. Please provide a .kx file.")
        sys.exit()

    tokenizer(file)
