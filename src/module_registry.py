import importlib

registered_modules = []

def register(module_name, display_name):
    module = importlib.import_module(module_name)
    registered_modules.append((module, display_name))

def get_registered_functions():
    functions_dict = {}
    for module, display_name in registered_modules:
        functions = [(name, func) for name, func in module.__dict__.items() if callable(func)]
        if functions:
            functions_dict[display_name] = functions
    return functions_dict
