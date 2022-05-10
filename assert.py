import sys
import os


ENV_FILE = os.getenv('GITHUB_ENV')


def main():
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
	# Read the above sys.exit exceptions for guidance.

	input_command_line = sys.argv[1]
	input_assert_file_path = sys.argv[2].replace('_', '')
	input_specific_line = sys.argv[3].replace('_', '')
	input_contains = sys.argv[4].replace('_', '')
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
	with open(OUTPUT_FILE) as file:
		actual_output = process_text(file.read())


	# Checking chosen option and getting the expected output.
	if input_contains:
		raw_expected_output = input_contains
	elif type(input_specific_line) is int:
		if not input_assert_file_path:
			sys.exit("Expected assert_file_path variable and got none.")
		with open(input_assert_file_path) as file:
			raw_expected_output = file.readlines()[input_specific_line - 1]
	elif input_assert_file_path:
		with open(input_assert_file_path) as file:
			raw_expected_output = file.read()
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
	
	sys.exit(test_result == input_expected_result)


def process_text(input_text):
	"""Removes trailing spaces, (extra) new lines ('\\n') and carriage return ('\\r') 
	from each line of some 'input_text' and returns it"""

	processed_text = [line.strip(" \r\n") for line in input_text.strip(" \r\n").split("\n")]

	for _ in range(processed_text.count('')):
		processed_text.remove('')

	return '\n'.join(processed_text)


if __name__ == "__main__":
	main()
