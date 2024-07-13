from src.utils.tokenizer import tokenize

operators = ['+', '-', '*', '/']


def gatherFunction(function: str):
    tokenized_function = tokenize(function)
    if(tokenized_function.__contains__('+')):
        print(f"Addition detected")

    print(f"Evaluated function {eval(function)}")


if __name__ == "__main__":
    gatherFunction(input("Enter a function: "))


def addIntegers(a: int, b: int) -> int:
    return a + b


def subtractIntegers(a: int, b: int) -> int:
    return a - b


def multiplyIntegers(a: int, b: int) -> int:
    return a * b


def divideIntegers(a: int, b: int) -> int:
    return a / b
