errors = {
    "INPUT_INVALID_FILE": lambda params: f'File {params["file_path"]} does not exist',
    "INPUT_INVALID_JSON": lambda params: f'The input JSON is invalid',
    "INVALID_LAST_KEY_TYPE": lambda params: f'The key ({params["current_key"]}) is expected to be primitive, but is an object or an array',
    "INVALID_MIDDLE_KEY_TYPE": lambda params: f'The key ({params["current_key"]}) is expected to have nested attributes, but is primitive type',
    "INVALID_KEY_PATH": lambda params: f'The key ({params["current_key"]}) does not exist in hierarchy'
}

class ManipulationException(Exception):

    def __init__(self, code, message):
        self.code = code
        self.message = message

def throw_error(code, params):
    if code in errors:
        message = errors[code](params)
    else:
        message = "An unkown error has occured"

    raise ManipulationException(code, message)

