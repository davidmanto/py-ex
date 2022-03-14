import os.path
import json
from errors import throw_error


def is_primitive(value):
    return not isinstance(value, (list, dict))


def transform(json_object, target_value, paths):
    current_key = paths[0]
    last_key = len(paths) == 1

    if current_key not in json_object:
        throw_error("INVALID_KEY_PATH", {"current_key": current_key})

    if last_key:
        if not is_primitive(json_object[current_key]):
            throw_error("INVALID_LAST_KEY_TYPE", {"current_key": current_key})

        json_object[current_key] = target_value
    else:
        if is_primitive(json_object[current_key]):
            throw_error("INVALID_MIDDLE_KEY_TYPE", {"current_key": current_key})

        if type(json_object[current_key]) == list:
            for element in json_object[current_key]:
                transform(element, target_value, paths[1:])
        else:
            transform(json_object[current_key], target_value, paths[1:])


def process_json(source, key_path, target_value):
    paths = key_path.split(".")
    transform(source, target_value, paths)

    return source


def process_text(textual_json, key_path, target_value):
    source = None
    try:
        source = json.loads(textual_json)
    except ValueError as e:
        throw_error("INPUT_INVALID_JSON", {})

    return process_json(source, key_path, target_value)


def process_file(file_path, key_path, target_value):
    if not os.path.isfile(file_path):
        throw_error("INPUT_INVALID_FILE", {"file_path": file_path})

    file = open(file_path, 'r')
    content = file.read()
    file.close()

    return process_text(content, key_path, target_value)


