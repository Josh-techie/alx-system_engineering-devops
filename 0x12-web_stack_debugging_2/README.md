# Web Stack Debugging #2

## Overview

This project is part of the ALX Africa Intranet DevOps and SysAdmin curriculum. It focuses on web stack debugging, specifically tasks related to running software as another user and configuring Nginx to run as the `nginx` user.

## Project Details

- **Start Date:** October 16, 2023 4:00 AM
- **Deadline:** October 18, 2023 4:00 AM
- **Checker Release:** October 17, 2023 11:12 AM

## Concepts Covered

- Web stack debugging
- Running software as another user

## General Requirements

- All files interpreted on Ubuntu 20.04 LTS
- Files end with a new line
- `README.md` file at the root is mandatory
- Bash script files are executable
- Bash scripts pass Shellcheck without any errors
- Bash scripts run without errors
- First line of all Bash scripts is `#!/usr/bin/env bash`
- Second line of all Bash scripts is a comment explaining the script's purpose

## Task 0: Run Software as Another User

### Description

The user `root` is a superuser, and it's a good practice not to be logged in as `root` to avoid accidental catastrophic commands. This script accepts a username as an argument and runs the `whoami` command under that user.

### Usage

```bash
./0-iamsomeoneelse [username]

