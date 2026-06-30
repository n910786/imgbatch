"""Basic smoke tests."""

import subprocess


def test_version():
    result = subprocess.run(["imgbatch", "--version"], capture_output=True, text=True)
    assert result.returncode == 0
    assert "imgbatch" in result.stdout
