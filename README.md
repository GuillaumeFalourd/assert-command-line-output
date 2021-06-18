# test-cli-commands-output-action

[![Action test on Ubuntu](https://github.com/GuillaumeFalourd/test-cli-commands-output-action/actions/workflows/ubuntu_test_command_output.yml/badge.svg)](https://github.com/GuillaumeFalourd/test-cli-commands-output-action/actions/workflows/ubuntu_test_command_output.yml) [![Action test on MacOs](https://github.com/GuillaumeFalourd/test-cli-commands-output-action/actions/workflows/macos_test_command_output.yml/badge.svg)](https://github.com/GuillaumeFalourd/test-cli-commands-output-action/actions/workflows/macos_test_command_output.yml) [![Action test on Windows](https://github.com/GuillaumeFalourd/test-cli-commands-output-action/actions/workflows/windows_test_command_output.yml/badge.svg)](https://github.com/GuillaumeFalourd/test-cli-commands-output-action/actions/workflows/windows_test_command_output.yml)

![title](https://user-images.githubusercontent.com/22433243/122581482-7893f400-d02d-11eb-9eee-5e62fe52dadd.png)

Github Action to test or check outputs of CLI commands 🕵️⚙️🖥

*Note: This action gather the [command-output-file-action](https://github.com/GuillaumeFalourd/command-output-file-action) and the [diff-action](https://github.com/GuillaumeFalourd/diff-action)*

* * *

## 📚 How to use this action?

The [`actions/checkout`](https://github.com/actions/checkout) is mandatory to use this action, as it will be necessary to access the repository files to get the output file after the action execution.

Field | Mandatory | Observation
------------ | ------------  | -------------
**command_line** | YES | ex: `ls -lha`
**assert_file_path** | YES | ex: `path/to/assert.txt` or `assert.txt` if on root directory
**expected_result** | NO | `PASSED` (default) or `FAILED`
**specific_line** | NO | ex: `1` (integer value only)

_NOTE: You can then access the **output.txt file** in the directory **where you ran the action**._

* * *

### ✅ Expected behaviour

#### Will return FAIL 

If the `diff` output of the command and the assert file is different than the `expected_result` input value.

#### Will return SUCCESS 

If the `diff` output of the command and the assert file is equal the `expected_result` input value.

 * * *

### 🕵️📋 Comparing 2 files

#### Expecting command output to be EQUAL to assert.txt file content

```yaml
    steps:
      - uses: actions/checkout@v2.3.4
      - uses: GuillaumeFalourd/test-cli-commands-output-action@main
        with:
          command_line: ls -lha
          assert_file_name: assert.txt
          expected_result: PASSED
```

#### Expecting command output to be DIFFERENT than the assert.txt file content

```yaml
    steps:
      - uses: actions/checkout@v2.3.4
      - uses: GuillaumeFalourd/test-cli-commands-output-action@main
        with:
          command_line: ls -lha
          assert_file_name: assert.txt
          expected_result: FAILED
```

### 🕵📝 Comparing 2 lines

#### Expecting command output line 3 to be EQUAL than the assert.txt file content in line 3

```yaml
    steps:
      - uses: actions/checkout@v2.3.4
      - uses: GuillaumeFalourd/test-cli-commands-output-action@main
        with:
          command_line: ls -lha
          assert_file_name: assert.txt
          expected_result: PASSED
          specific_line: 3
```

#### Expecting command output line 3 to be DIFFERENT than the assert.txt file content in line 3

```yaml
    steps:
      - uses: actions/checkout@v2.3.4
      - uses: GuillaumeFalourd/test-cli-commands-output-action@main
        with:
          command_line: ls -lha
          assert_file_name: assert.txt
          expected_result: FAILED
          specific_line: 3
```

## Licensed

This repository uses the [Apache License 2.0](https://github.com/GuillaumeFalourd/aws-cliaction/blob/main/LICENSE)
