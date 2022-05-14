"""
assert.py is a module for asserting the actual output of a given command is equal to a given
expected output.
This can be used for asserting in any language as long as you pass in the correct cmd command that
will run your code. It will then compare it to either your written input in "_<Contains>" or the
contents of a file.

This module should be called in accord to the following pattern:
python assert.py "<CommandLine>" "_<AssertFilePath>" "_<SpecificLineNumber>" "_<Contains>" "<ExpectedResult>"
e.g. python assert.py "echo Hi" "_" "_" "_Hi" "PASSED"

As an usage example, let's say you want to assert your fibonacci series program
is calculating the correct fibonacci sequence. You could write your input and output
in text files such as test1.in and test1.out, respectively, and call:

If your program expects inputs from stdin (e.g. input(...), scanf(...), etc):
python assert.py "python fib.py < test1.in" "_test1.out" "_" "_" "PASSED"
python assert.py "fib.exe < test1.in" "_test1.out" "_" "_" "PASSED"

If your program expects the file from command line arguments:
python assert.py "python fib.py test1.in" "_" "_" "_test1.out" "PASSED"
python assert.py "fib.exe test1.in" "_" "_" "_test1.out" "PASSED"

If your program statically reads the file:
python assert.py "python fib.py" "_" "_" "_test1.out" "PASSED"
python assert.py "fib.exe" "_" "_" "_test1.out" "FAILED"

Other examples:
python assert.py "python fib.py 1" "_" "_" "_1" "PASSED"
python assert.py "python fib.py 1" "_" "_" "_0" "FAILED"
python assert.py "echo Hi" "_" "_" "_Hello" "FAILED"
"""

import sys
import os


ENV_FILE = os.getenv('GITHUB_ENV')


def main():
    """The main function should only run in the following conditions:
    1. sys.argv should have exactly 6 values (including the file path);
        a. This means this module received 5 arguments when called.
    2. The second to fourth arguments should always start with "_".
    """
    if len(sys.argv) != 6:
        sys.exit(
            f"Invalid usage: not enough arguments. \"Empty\" arguments should receive \"_\".\n\
            \rExpected:\n{sys.argv[0]} \"<CommandLine>\" \"_<AssertFilePath>\" \"_<SpecificLineNumber>\" \"_<Contains>\" \"<ExpectedResult>\"\n"
        )
    if not ((sys.argv[2][0] == '_') and (sys.argv[3][0] == '_') and (sys.argv[4][0] == '_')):
        sys.exit(
            f"Invalid usage: arguments in the middle should have a \"_\" before the actual input.\n\
            \rExpected:\n{sys.argv[0]} \"<CommandLine>\" \"_<AssertFilePath>\" \"_<SpecificLineNumber>\" \"_<Contains>\" \"<ExpectedResult>\""
        )

    # The first and last argument will always exist given the workflow's
    # requirements.
    # The ones in the middle may not exist, so the workflow needs to ensure
    # they do.

    input_command_line = sys.argv[1]
    input_assert_file_path = sys.argv[2].replace('_', '', 1)
    input_specific_line = sys.argv[3].replace('_', '', 1)
    input_contains = sys.argv[4].replace('_', '', 1)
    input_expected_result = sys.argv[5]

    if input_specific_line:
        try:
            input_specific_line = int(input_specific_line)
        except ValueError:
            sys.exit("Expected a number for \"specific line\".")

    print("********************************")
    print(f"COMMAND LINE: {input_command_line}")
    print(f"ASSERT FILE PATH: {input_assert_file_path}")
    print(f"SPECIFIC LINE: {input_specific_line}")
    print(f"CONTAINS: {input_contains}")
    print(f"EXPECTED RESULT: {input_expected_result}")
    print("********************************\n")

    OUTPUT_FILE = "output.txt"
    
    # Running cmd input and saving logs to OUTPUT_FILE.
    os.system(f"{input_command_line} > {OUTPUT_FILE}")
    # Reading OUTPUT_FILE and processing output text.
    with open(OUTPUT_FILE, encoding='utf-8') as file:
        actual_output = file.read()
    actual_output = process_text(actual_output)


    # Checking chosen option and getting the raw expected output.
    if input_contains:
        raw_expected_output = input_contains
    elif input_assert_file_path:
        with open(input_assert_file_path, encoding='utf-8') as file:
            raw_expected_output = file.read()
        if type(input_specific_line) is int:
            raw_expected_output = raw_expected_output.split('\n')[input_specific_line - 1]
    else:
        sys.exit("Not enough inputs.")

    expected_output = process_text(raw_expected_output)

    # Checking if tests passed and comparing against expected result.
    test_result = "PASSED" if expected_output in actual_output else "FAILED"
    print(
        f"Expected: {input_expected_result}",
        f"Actual: {test_result}",
        sep='\n'
    )
    
    sys.exit(test_result != input_expected_result)


def process_text(input_text):
    """Removes trailing spaces, (extra) new lines ('\\n') and carriage return ('\\r') 
    \rfrom each line of some 'input_text' and returns it"""

    processed_text = [line.strip(" \r\n") for line in input_text.strip(" \r\n").split("\n")]

    for _ in range(processed_text.count('')):
        processed_text.remove('')

    return '\n'.join(processed_text)


if __name__ == "__main__":
    main()
