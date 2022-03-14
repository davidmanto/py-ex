# Json Manipulator

The tool is able to read JSON from a text file or from input via command line, and manipulate a nested field(s)

## Files

A brief explanation of the files in the source code:

- `json_manipulator.py` - Contains core functionality
- `errors.py` - Contains error codes and simple error throwing mechanism
- `main.py` - The main file to be run by the end user to interface using bash/cmd
- `test_json_manipulator.py` - Contains unit tests

## Usage

To use, run the following command
```shell
$ py main.py [-f] [-o output-file] <input> <key-path> <target-path>
```

- `input` - The json itself, use the optional `-f` flag to read from a file relative to the project directory
- `key_path`- The path to the field to be manipulated, can be nested (e.g: `insightMetadata.activated`)
  * The last or the only key must be a primitive type (integer, boolean, string, etc...)
  * If the path contains multiple keys (nested), intermediate paths must be arrays or objects
  * If some key is an array, all the nested keys will be manipulated accordingly
- `target_value` - The value that the key(s) should be manipulated to
- `-o` - Optional flag to write the manipulated json to the specified path, otherwise will be printed in console (e.g: `-o my-file.json`)


## Personal notes

In a realistic day to day scenario, I would have used an existing library such as `jsonpath`,
since there is no need the reinvent to wheel and write functionality that already is maintained and well test.  
For the sake of examining python knowledge, I have decided to implement a primitive and simple json navigation algorithm.