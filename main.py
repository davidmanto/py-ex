from json_manipulator import process_json, process_file
import argparse
import json

parser = argparse.ArgumentParser(description="Change value of a specified key")
parser.add_argument("input", help="The input or the path of the file")
parser.add_argument("key_path", metavar="key-path", help="The path to the value in the JSON")
parser.add_argument("target_value", metavar="target-path", help="The value that the key should be manipualted to")
parser.add_argument("-f", required=False, action="store_true", help="Can be used to read from file")
parser.add_argument("-o", required=False, metavar="output-file", help="Can be used to write to file")


def read_input():
    args = parser.parse_args()
    result = None

    if args.f:
        result = process_file(args.input, args.key_path, args.target_value)
    else:
        result = process_json(args.input, args.key_path, args.target_value)

    final_json = json.dumps(result, indent=4, sort_keys=True)

    if args.o is not None:
        file = open(args.o, "w")
        file.write(final_json)
        file.close()
    else:
        print(final_json)


read_input()
