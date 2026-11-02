from diagnostics_tool.checks import (
    PythonVersionCheck,
    OperatingSystemCheck,
)


def test_python_version_check():
    check = PythonVersionCheck()
    result = check.run()

    assert result["check"] == "Python Version"
    assert result["status"] == "PASS"
    assert "Python" in result["details"]


def test_operating_system_check():
    check = OperatingSystemCheck()
    result = check.run()

    assert result["check"] == "Operating System"
    assert result["status"] == "PASS"
    assert result["details"] != ""


def test_environment_check_name():
    check = PythonVersionCheck()

    assert check.name == "Python Version"