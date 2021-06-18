# test-cli-commands-output-action

Github Action to test or check outputs of CLI commands

* * *

## 🖥 Supported OS

OS | SUPPORTED
---------- | ------------
**LINUX** | YES
**MACOS** | YES
**WINDOWS** | YES

## 📚 How to use this action?

The [`actions/checkout`](https://github.com/actions/checkout) is mandatory to use this action, as it will be necessary to access the repository files to get the output file after the action execution.

Field | Mandatory | Observation
------------ | ------------  | -------------
**command_line** | YES | ex: `ls -lha`
**assert_file_name** | YES | ex: `assert.txt`
**expected_result** | NO | `PASSED` (default) or `FAILED`
**specific_line** | NO | ex: `1` (integer value only)

_**Note**: You can then access the **output.txt file** in the directory **where you ran the action**._

**Will return FAIL**: If the `diff` output of the command and the assert file is different than the `expected_result` input value.

**Will return SUCCESS**: If the `diff` output of the command and the assert file is equal the `expected_result` input value.

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
