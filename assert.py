import sys
import os


ENV_FILE = os.getenv('GITHUB_ENV')


def main():
	input_command_line = sys.argv[1]
	input_assert_file_path = sys.argv[2]
	input_specific_line = sys.argv[3]
	input_contains = sys.argv[4]
	input_expected_result = sys.argv[5]

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
		expected_output = process_text(input_contains)
	elif input_specific_line:
		if not input_assert_file_path:
			sys.exit("Expected assert_file_path variable and got none.")
		with open(input_assert_file_path) as file:
			expected_output = process_text(file.readlines()[input_specific_line - 1])
	elif input_assert_file_path:
		with open(input_assert_file_path) as file:
			expected_output = process_text(file.readlines()[input_specific_line - 1])
	else:
		sys.exit("Not enough inputs.")

	# Checking if tests passed and comparing to expected result.

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
