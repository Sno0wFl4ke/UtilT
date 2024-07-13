from src.utils.tokenizer import tokenize


def evaluate_expression(expression: str):
    # List of safe functions
    safe_list = ['+', '-', '*', '/', 'sin', 'cos']

    # Split the expression into parts
    parts = expression.split()

    # Check each part of the expression
    for part in parts:
        if part not in safe_list and not part.isdigit():
            raise ValueError(f"Invalid character: {part}")

    # Replace sin and cos with their math equivalents
    expression = expression.replace('sin', 'math.sin')
    expression = expression.replace('cos', 'math.cos')

    # Evaluate the expression
    result = eval(expression)

    return result

# TODO: ERROR
"""
15
Traceback (most recent call last):
  File "/Users/philiplangenbrink/Documents/PyCharm Projects/TheUtilT/src/funcmodules/math_module.py", line 31, in <module>
    print(evaluate_expression("sin(0)"))  # Output: 0.0
  File "/Users/philiplangenbrink/Documents/PyCharm Projects/TheUtilT/src/funcmodules/math_module.py", line 14, in evaluate_expression
    raise ValueError(f"Invalid character: {part}")
ValueError: Invalid character: sin(0)
"""

# Test the function


if __name__ == "__main__":
    print(evaluate_expression("5 + 10"))  # Output: 15
    print(evaluate_expression("sin(0)"))  # Output: 0.0
    print(evaluate_expression("cos(0)"))  # Output: 1.0
