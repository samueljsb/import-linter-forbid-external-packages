# Contributing

## Set up a development environment

To set up a development environment:

1. Clone the repository.

    ```sh
    git clone git@github.com/samueljsb/import-linter-forbid-external-packages
    cd import-linter-forbid-external-packages
    ```

2. Create a virtual environment
   and install the development dependencies.

    ```sh
    uv venv
    uv pip install --editable . --group dev
    ```

3. Activate the new virtual environment.

    ```sh
    . .venv/bin/activate
    ```

4. Configure pre-commit.

    ```sh
    pre-commit install
    ```

## Run development jobs with `tox` (recommended)

This project uses [`tox`] to run development and CI jobs
and [`pre-commit`] to run linters.

By default, `tox` will run the testing jobs in succession.
During development, run `tox` to execute those jobs and verify your changes.

[`pre-commit`]: https://pre-commit.com
[`tox`]: https://tox.wiki/en/4.48.1/

## Run development jobs directly

The commands necessary to run development jobs are configured in the `tox.ini` file.
