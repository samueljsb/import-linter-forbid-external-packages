# Forbid External Packages contract

A contract for [import-linter]
that forbids imports of external (i.e. not in the standard library) packages.

[https://import-linter.readthedocs.io/en/stable/]: https://import-linter.readthedocs.io/en/stable/

## Usage

1. Install this package in the same virtual environment as import-linter.

2. Add the contract type to your config file, e.g:

    ```diff

      [importlinter]
      root_package = my_project
      include_external_packages = True
    + contract_types=
    +     forbid_external_packages: importlinter_forbid_external_packages.Contract
    ```

    N.B. `include_external_packages` must be enabled
    for this contract type to have any effect.

3. Create a contract with `type = forbid_external_packages`.
   This contract must specify the `source_modules` value,
   as [documented for the built-in `forbidden` contract type][forbidden contract type]

[forbidden contract type]: https://import-linter.readthedocs.io/en/stable/contract_types/forbidden/

### Example

```ini
[importlinter]
root_package = my_project
include_external_packages = True
contract_types=
    forbid_external_packages: importlinter_forbid_external_packages.Contract

[importlinter:contract:external-packages]
name = External packages
type = forbid_external_packages
source_modules =
    my_project.*
```
