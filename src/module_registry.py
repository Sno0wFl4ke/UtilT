import importlib

registered_modules = []

def register(module_name, function_name, display_name):
    module = importlib.import_module(module_name)
    function = getattr(module, function_name)
    registered_modules.append((function, display_name))

def get_registered_functions():
    functions_dict = {}
    for function, display_name in registered_modules:
        if function:
            functions_dict[display_name] = function
    return functions_dict
