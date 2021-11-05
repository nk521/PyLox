import sys
import os

hadError: bool = False

def report(line: int, where: str, message: str) -> None:
    print(f"[line {line}] Error {where}: {message}")
    hadError = True


def error(line: int, message: str) -> None:
    report(line, "", message)


def execCode(code: str) -> None:
    tokens = code
    print(tokens)


def execRepl() -> None:
    def kill() -> None:
        print("Exiting...")
        sys.exit(0)

    while True:
        try:
            line = input("lox > ")
            if not line:
                continue
            execCode(line)
            hadError = False
        
        except EOFError:
            print("^D")
            kill()


def execFile(filename: str) -> None:
    if filename.split(".")[-1] != "lox":
        print(f"{filename} is not a lox file.")
        sys.exit(64)

    try:
        with open(filename) as f:
            code = f.read()
        execCode(code)

        if hadError:
            sys.exit(65)
    
    except FileNotFoundError:
        print(f"Error: {filename} doesn't exist!")


if __name__ == "__main__":
    if len(sys.argv) > 2:
        print(f"Usage: {sys.argv[0]} [script.lox]")
        sys.exit(64)

    elif len(sys.argv) == 2:
        execFile(sys.argv[1])

    else:
        execRepl()