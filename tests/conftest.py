import os

import pytest


@pytest.fixture(autouse=True)
def _chdir_to_tests_dir(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.chdir(os.path.dirname(__file__))
