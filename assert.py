import sys
import os

env_file = os.getenv('GITHUB_ENV')

input_command_line = sys.argv[1]
input_assert_file_path = sys.argv[2]
input_specific_line = sys.argv[3]
input_contains = sys.argv[4]
input_expected_result = sys.argv[5]

print(f"COMMAND LINE: {input_command_line}")
print(f"ASSERT FILE PATH: {input_assert_file_path}")
print(f"SPECIFIC LINE: {input_specific_line}")
print(f"CONTAINS: {input_contains}")
print(f"EXPECTED RESULT: {input_expected_result}")
