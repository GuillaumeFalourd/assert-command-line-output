# Assert Command Line Output

[![Public workflows that use this action.](https://img.shields.io/endpoint?url=https%3A%2F%2Fapi-endbug.vercel.app%2Fapi%2Fgithub-actions%2Fused-by%3Faction%3DGuillaumeFalourd%2Fassert-command-line-output%26badge%3Dtrue)](https://github.com/search?o=desc&q=GuillaumeFalourd+assert-command-line-output+path%3A.github%2Fworkflows+language%3AYAML&s=&type=Code) [![Action test on Ubuntu](https://github.com/GuillaumeFalourd/assert-command-line-output/actions/workflows/ubuntu_test_command_output.yml/badge.svg)](https://github.com/GuillaumeFalourd/check-command-line-output/actions/workflows/ubuntu_test_command_output.yml) [![Action test on MacOs](https://github.com/GuillaumeFalourd/assert-command-line-output/actions/workflows/macos_test_command_output.yml/badge.svg)](https://github.com/GuillaumeFalourd/assert-command-line-output/actions/workflows/macos_test_command_output.yml) [![Action test on Windows](https://github.com/GuillaumeFalourd/assert-command-line-output/actions/workflows/windows_test_command_output.yml/badge.svg)](https://github.com/GuillaumeFalourd/assert-command-line-output/actions/workflows/windows_test_command_output.yml)

![title](https://user-images.githubusercontent.com/22433243/138319283-f2c06465-8ad5-4366-99d1-504a92e6b51e.png)

Github Action to assert / check a command line output 🕵️⚙️🖥

This action allows to compare a _command line output_ (success or error) with a _file content_ located on the repository, or to check if it contains a specific _expression_.

---

## 📚 Usage

<!-- [![Public workflows that use this action (V1).](https://img.shields.io/endpoint?url=https%3A%2F%2Fapi-endbug.vercel.app%2Fapi%2Fgithub-actions%2Fused-by%3Faction%3DGuillaumeFalourd%2Ftest-cli-commands-action%26badge%3Dtrue)](https://github.com/search?o=desc&q=GuillaumeFalourd+test-cli-commands-action+path%3A.github%2Fworkflows+language%3AYAML&s=&type=Code) ☞ [Who is using this action? (V1) 🧑‍💻](https://github.com/search?q=GuillaumeFalourd+test-cli-commands-action+path%3A.github%2Fworkflows+language%3AYAML&type=code)

[![Public workflows that use this action (V2).](https://img.shields.io/endpoint?url=https%3A%2F%2Fapi-endbug.vercel.app%2Fapi%2Fgithub-actions%2Fused-by%3Faction%3DGuillaumeFalourd%2Fassert-command-line-output%26badge%3Dtrue)](https://github.com/search?o=desc&q=GuillaumeFalourd+assert-command-line-output+path%3A.github%2Fworkflows+language%3AYAML&s=&type=Code) ☞ [Who is using this action? (V2) 🧑‍💻](https://github.com/search?q=GuillaumeFalourd+assert-command-line-output+path%3A.github%2Fworkflows+language%3AYAML&type=code) -->

### How does the action work?

![how does the action work](https://user-images.githubusercontent.com/22433243/123486342-39901080-d5e2-11eb-94f2-3f45b4ed6205.png)

### Requirements

⚠️ The [`actions/checkout`](https://github.com/marketplace/actions/checkout) is mandatory to use this action, as it will be necessary to access the repository files, or to access the command line output file after the action execution.

☞ _Note: This action gathers the logic from the [command-output-file-action](https://github.com/GuillaumeFalourd/command-output-file-action) and the [diff-action](https://github.com/GuillaumeFalourd/diff-action)_.

---

## ♻️ Scenarios

### `1️⃣ Assert file content`

#### Expecting command output to be EQUAL to `assert.txt` file content

```yaml
steps:
  - uses: actions/checkout@v3
  - uses: GuillaumeFalourd/assert-command-line-output@v2.2
    with:
      command_line: ls -lha
      assert_file_path: path/to/assert.txt
      expected_result: PASSED
```

#### Expecting command output to be DIFFERENT than the `assert.txt` file content

```yaml
steps:
  - uses: actions/checkout@v3
  - uses: GuillaumeFalourd/assert-command-line-output@v2.2
    with:
      command_line: ls -lha
      assert_file_path: path/to/assert.txt
      expected_result: FAILED
```

### `2️⃣ Assert specific file line`

#### Expecting command output line 3 to be EQUAL than the `assert.txt` file content in line 3

```yaml
steps:
  - uses: actions/checkout@v3
  - uses: GuillaumeFalourd/assert-command-line-output@v2.2
    with:
      command_line: ls -lha
      assert_file_path: path/to/assert.txt
      expected_result: PASSED
      specific_line: 3
```

#### Expecting command output line 3 to be DIFFERENT than the `assert.txt` file content in line 3

```yaml
steps:
  - uses: actions/checkout@v3
  - uses: GuillaumeFalourd/assert-command-line-output@v2.2
    with:
      command_line: ls -lha
      assert_file_path: path/to/assert.txt
      expected_result: FAILED
      specific_line: 3
```

### `3️⃣ Assert specific expression`

#### Expecting command output to contain specific expression

```yaml
steps:
  - uses: actions/checkout@v3
  - uses: GuillaumeFalourd/assert-command-line-output@v2.2
    with:
      command_line: ls -lha
      contains: runner
      expected_result: PASSED
```

#### Expecting command output NOT to contain specific expression

```yaml
steps:
  - uses: actions/checkout@v3
  - uses: GuillaumeFalourd/assert-command-line-output@v2.2
    with:
      command_line: ls -lha
      contains: error
      expected_result: FAILED
```

### `4️⃣ Multiple-line commands`

The assert may fail while using multiple-line commands. When this is necessary, use single quotes `'`.

```yaml
steps:
  - uses: actions/checkout@v3
  - uses: GuillaumeFalourd/assert-command-line-output@v2.2
    with:
      command_line: | 
        'a_very_long_command --that --need
        --multiple --lines --to --write'
      assert_file_path: path/to/assert.txt
      expected_result: PASSED
```

---

## ▶️ Action Inputs

| Field                | Mandatory | Observation                                                                                                                                      |
| -------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| **command_line**     | YES       | Command Line to assert / check. <br/> _e.g: `ls -lha`_                                                                                           |
| **assert_file_path** | NO        | Path to assert file that will be compared to command line output. <br/> _e.g: `path/to/assert.txt`_                                              |
| **specific_line**    | NO        | Specific line to check from output file with assert file. <br/> **NEEDS** `assert_file_path` configured. <br/> _e.g: `1` (*integer value only*)_ |
| **contains**         | NO        | String expression to check on the command line output. <br/> _e.g: `string expression`_                                                          |
| **expected_result**  | NO        | Expected assert output. <br/> _e.g: `PASSED` (*default*) or `FAILED`_                                                                            |

### 🔎 Good to know

- At least **one type of assert** between `contains`, `specific_line` and `assert_file_path` has to be configured.

- If **more than one type of assert** is set, the priority between them is:

  - 1️⃣ `contains`
  - 2️⃣ `specific_line`
  - 3️⃣ `assert_file_path`

- You can access the **output.txt file** in the repository directory **after running the action**.

---

## 🤝 Contributing

☞ [Guidelines](https://github.com/GuillaumeFalourd/test-cli-commands-action/blob/main/CONTRIBUTING.md)

## 🏅 Licensed

☞ This repository uses the [Apache License 2.0](https://github.com/GuillaumeFalourd/assert-command-line-output/blob/main/LICENSE)
