# Contribution guidelines

Before sending a Pull Request, please make sure that you're assigned the task on
a GitHub issue.

- If a relevant issue already exists, discuss on the issue and get it assigned
  to yourself on GitHub.
- If no relevant issue exists, open a new issue and get it assigned to yourself
  on GitHub.

Please proceed with a Pull Request only after you're assigned. It'd be bad time
if your Pull Request and your hardwork isn't accepted just because it isn't
ideologically compatible.

## Developing the Project

1. Install with

    ```sh
    git clone https://github.com/terrvis/terrvis-backend
    cd terrvis-backend
    make build
    ```

2. Make your changes in a different git branch (eg, `enhancement/new-feature`).
   These changes can be:

    - enhancing the service
    - fixing a bug
    - adding additional tests

3. (Optional) To test whether `terrvis-backend` was built successfully.
    ```sh
    # No tests at this time
    ```

4. (Required for new steps) Add command to both `.travis.yml` file and `Makefile`.
