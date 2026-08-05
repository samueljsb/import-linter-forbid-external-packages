from __future__ import annotations

from importlinter.domain import imports

import importlinter_forbid_external_packages


def test_filter_stdlib_modules() -> None:
    modules = [
        imports.Module('pytest'),
        imports.Module('unittest.mock'),
        imports.Module('os.environ'),
        imports.Module('os'),
    ]

    importlinter_forbid_external_packages.filter_stdlib_modules(modules)

    assert modules == [
        imports.Module('pytest'),
    ]
