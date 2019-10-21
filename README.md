# Test Script executor project

This program clones an exisitng git repository with script.py file in it, checks out specific commit, executes given script and cleans up working directory.

## Usage
`run.py` script takes 3 required arguments: 
- git repository url
- commit hash
- an argument (number, in our case - float) which will be passed to the script.

**Note**: login to your github account in with the command line in case of you don't trust that this program won't steal your credentials :D

## Examples
```
$ python3.7 run.py --help

usage: run.py [-h] url commit x

Executes a script cloned from a given git repo.

positional arguments:
  url         a git repository url which will be cloned
  commit      a commit hash
  x           a float argument for script

optional arguments:
  -h, --help  show this help message and exit
```

The example below does the following:
1. Clones git repository from https://github.com/DmytroMalikin/test_script.
2. Checks out specific commit which hash is 2bfb3372eaae7db83d064acd17ebcfe0a8b6190a
3. Runs the script.py file with 8.0 as the only argument

```
$ python3.7 run.py https://github.com/DmytroMalikin/test_script 2bfb3372eaae7db83d064acd17ebcfe0a8b6190a 8

Running an executor with such arguments:
repo url: https://github.com/DmytroMalikin/test_script
commit hash: 2bfb3372eaae7db83d064acd17ebcfe0a8b6190a
argument: 8.0
=== STEP 1 ===
Script workdir tmp/ created.
Cloning a git repository...
Git repository successfully cloned.
=== STEP 2 ===
Trying to check out a commit..
Checked out at 2bfb3372eaae7db83d064acd17ebcfe0a8b6190a.
=== STEP 3 ===
Trying to execute script..
Result of x * 42 = 336.0
Script was successfully executed!
=== STEP 4 === 
Cleaning up the working directory...
Working directory has been cleaned up.
```

And then you can run the same command with another commit hash:
```
$ python3.7 run.py https://github.com/DmytroMalikin/test_script 20e6bc331a9a85b9cc453e285f9b2b37f76381e6 8

Running an executor with such arguments:
repo url: https://github.com/DmytroMalikin/test_script
commit hash: 20e6bc331a9a85b9cc453e285f9b2b37f76381e6
argument: 8.0
=== STEP 1 ===
Script workdir tmp/ created.
Cloning a git repository...
Git repository successfully cloned.
=== STEP 2 ===
Trying to check out a commit..
Checked out at 20e6bc331a9a85b9cc453e285f9b2b37f76381e6.
=== STEP 3 ===
Trying to execute script..
Result of x ** 2 + x ** 3 = 576.0
Script was successfully executed!
=== STEP 4 === 
Cleaning up the working directory...
Working directory has been cleaned up.
```

Changes in script algorithm are shown in STEP 3 section.
