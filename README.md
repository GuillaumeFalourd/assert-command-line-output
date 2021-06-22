# Test CLI commands Action

[![Action test on Ubuntu](https://github.com/GuillaumeFalourd/test-cli-commands-action/actions/workflows/ubuntu_test_command_output.yml/badge.svg)](https://github.com/GuillaumeFalourd/test-cli-commands-action/actions/workflows/ubuntu_test_command_output.yml) [![Action test on MacOs](https://github.com/GuillaumeFalourd/test-cli-commands-action/actions/workflows/macos_test_command_output.yml/badge.svg)](https://github.com/GuillaumeFalourd/test-cli-commands-action/actions/workflows/macos_test_command_output.yml) [![Action test on Windows](https://github.com/GuillaumeFalourd/test-cli-commands-action/actions/workflows/windows_test_command_output.yml/badge.svg)](https://github.com/GuillaumeFalourd/test-cli-commands-action/actions/workflows/windows_test_command_output.yml)

![title](https://user-images.githubusercontent.com/22433243/122581482-7893f400-d02d-11eb-9eee-5e62fe52dadd.png)

Github Action to test or check outputs of CLI commands 🕵️⚙️🖥

This action will compare (using [diff](http://www.linuxguide.it/command_line/linux-manpage/do.php?file=diff)) a _command line output_ (success or error) to a _file content_ located on the repository.

* * *

## 📚 Usage

`✅` When the `diff` execution of the _command line output_ and the _assert file_ is **EQUAL** to the `expected_result` input value, the action will **PASS**.

`❌` When the `diff` execution of the _command line output_ and the _assert file_ is **DIFFERENT** than the `expected_result` input value, the action will **FAIL**.

*Note: This action gather the [command-output-file-action](https://github.com/GuillaumeFalourd/command-output-file-action) and the [diff-action](https://github.com/GuillaumeFalourd/diff-action)*.

### Requirements

⚠️  The [`actions/checkout`](https://github.com/actions/checkout) is mandatory to use this action, as it will be necessary to access the repository files, or to access the output file after the action execution.

⚠️ The [`actions/setup-node`](https://github.com/actions/setup-node) is mandatory to use this action, as it will be necessary to use npm to install [strip-ansi-cli](https://www.npmjs.com/package/strip-ansi-cli) during the action execution.

 * * *

## ♻️ Scenarios

#### Expecting command output to be EQUAL to `assert.txt` file content

```yaml
    steps:
      - uses: actions/checkout@v2.3.4
      - uses: actions/setup-node@v2
        with:
          node-version: '14'
      - uses: GuillaumeFalourd/test-cli-commands-action@v1
        with:
          command_line: ls -lha
          assert_file_path: path/to/assert.txt
          expected_result: PASSED
```

#### Expecting command output to be DIFFERENT than the `assert.txt` file content

```yaml
    steps:
      - uses: actions/checkout@v2.3.4
      - uses: actions/setup-node@v2
        with:
          node-version: '14'
      - uses: GuillaumeFalourd/test-cli-commands-action@v1
        with:
          command_line: ls -lha
          assert_file_path: path/to/assert.txt
          expected_result: FAILED
```

#### Expecting command output line 3 to be EQUAL than the `assert.txt` file content in line 3

```yaml
    steps:
      - uses: actions/checkout@v2.3.4
      - uses: actions/setup-node@v2
        with:
          node-version: '14'
      - uses: GuillaumeFalourd/test-cli-commands-action@v1
        with:
          command_line: ls -lha
          assert_file_path: path/to/assert.txt
          expected_result: PASSED
          specific_line: 3
```

#### Expecting command output line 3 to be DIFFERENT than the `assert.txt` file content in line 3

```yaml
    steps:
      - uses: actions/checkout@v2.3.4
      - uses: actions/setup-node@v2
        with:
          node-version: '14'
      - uses: GuillaumeFalourd/test-cli-commands-action@v1
        with:
          command_line: ls -lha
          assert_file_path: path/to/assert.txt
          expected_result: FAILED
          specific_line: 3
```

* * *

## ▶️ Action Inputs

Field | Mandatory | Observation
------------ | ------------  | -------------
**command_line** | YES | e.g: `ls -lha`
**assert_file_path** | YES | e.g: `path/to/assert.txt`
**expected_result** | NO | e.g: `PASSED` (*default*) or `FAILED`
**specific_line** | NO | e.g: `1` (*integer value only*)

_NOTE: You can then access the **output.txt file** in the repository directory **where you ran the action**._

* * *

## Licensed

This repository uses the [Apache License 2.0](https://github.com/GuillaumeFalourd/aws-cliaction/blob/main/LICENSE)
