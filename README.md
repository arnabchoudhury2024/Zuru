# pyls

`pyls` is a Python program that mimics the `ls` Linux utility. It reads a JSON file representing a directory structure and prints its contents to the console. The program supports various command-line arguments to customize the output.

## Features

- List files and directories in a specified directory.
- Support for hidden files.
- Detailed listing with file permissions, sizes, and modification times.
- Reverse order listing.
- Sorting by modification time.
- Filtering by file type (file or directory).
- Human-readable file sizes.
- Path navigation within the JSON structure.
- 
## Options
- -A: Include hidden files (those starting with .).
- -l: Use a long listing format.
- -r: Reverse the order of the listing.
- -t: Sort by modification time, newest first.
- --filter=<option>: Filter the output by file or dir.
- --help: Display the help message.

## Examples
**List all files and directories in the current directory:**
`python -m src.pyls`

**Include hidden files:**
`python -m src.pyls -A`

**Long listing format:**
`python -m src.pyls -l`

**Reverse order:**
`python -m src.pyls -l -r`

**Sort by modification time:**
`python -m src.pyls -l -t`

**Filter by directories:**
`python -m src.pyls -l -r -t --filter=dir`

**Navigate to a subdirectory:**
`python -m src.pyls -l parser`

**Error Handling:**
If a specified path does not exist, pyls will print an error message:
`error: cannot access 'non_existent_path': No such file or directory`



## Testing
- Include tests using unittest.
- Ensure all features are covered by tests.
