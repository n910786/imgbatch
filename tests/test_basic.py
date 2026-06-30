"""Basic smoke tests."""

import subprocess
import imgbatch


def test_version_attribute():
    assert imgbatch.__version__ == "0.1.0"


def test_cli_version():
    result = subprocess.run(
        ["python", "-m", "imgbatch.cli", "--version"],
        capture_output=True, text=True,
    )
    assert result.returncode == 0
