from __future__ import annotations

import sys

from importlinter.contracts import forbidden
from importlinter.domain import fields
from importlinter.domain import imports


def filter_stdlib_modules(modules: list[imports.Module]) -> None:
    for idx, module in reversed(list(enumerate(modules))):
        package, *_ = module.name.partition('.')
        if package in sys.stdlib_module_names:
            del modules[idx]


class Contract(forbidden.ForbiddenContract):
    # Copy some configuration fields from ForbiddenContract.
    source_modules = fields.SetField(subfield=fields.ModuleExpressionField())
    ignore_imports = fields.SetField(
        subfield=fields.ImportExpressionField(), required=False
    )

    # Explicitly set some configuration values.
    # These cause a 'Incompatible types in assignment' mypy error, which we ignore.
    forbidden_modules = (imports.ModuleExpression('*'),)  # type: ignore[assignment]
    allow_indirect_imports = False  # type: ignore[assignment]
    as_packages = True  # type: ignore[assignment]

    def _check_external_forbidden_modules(
        self, forbidden_modules: list[imports.Module]
    ) -> None:  # pragma: no cover
        super()._check_external_forbidden_modules(forbidden_modules)
        filter_stdlib_modules(forbidden_modules)
