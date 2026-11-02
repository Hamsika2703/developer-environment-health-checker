import sys
import platform
import shutil
import importlib.util
import socket
import psutil

# 1. Python Version Check
class PythonVersionCheck:

    name = "Python Version"

    def run(self):
        version = platform.python_version()

        major = sys.version_info.major
        minor = sys.version_info.minor

        status = "PASS" if (major, minor) >= (3, 8) else "FAIL"

        return {
            "check": self.name,
            "status": status,
            "details": f"Python {version} installed"
        }


# 2. Operating System Check
class OperatingSystemCheck:

    name = "Operating System"

    def run(self):
        os_name = platform.system()
        version = platform.version()
        machine = platform.machine()

        return {
            "check": self.name,
            "status": "PASS",
            "details": f"{os_name} {version}, machine: {machine}"
        }


# 3. Git Installation Check
class GitInstallationCheck:

    name = "Git Installation"

    def run(self):
        git_path = shutil.which("git")

        if git_path:
            return {
                "check": self.name,
                "status": "PASS",
                "details": f"Git installed at {git_path}"
            }

        return {
            "check": self.name,
            "status": "WARN",
            "details": "Git is not installed or not available in PATH"
        }


# 4. VS Code Installation Check
class VSCodeInstallationCheck:

    name = "VS Code Installation"

    def run(self):
        code_path = shutil.which("code")

        if code_path:
            return {
                "check": self.name,
                "status": "PASS",
                "details": f"VS Code found at {code_path}"
            }

        return {
            "check": self.name,
            "status": "WARN",
            "details": "VS Code command is not available in PATH"
        }


# 5. Required Python Packages Check
class RequiredPackagesCheck:

    name = "Required Python Packages"

    def run(self):
        required_packages = ["pytest"]

        missing = []

        for package in required_packages:
            if importlib.util.find_spec(package) is None:
                missing.append(package)

        if missing:
            return {
                "check": self.name,
                "status": "WARN",
                "details": f"Missing packages: {', '.join(missing)}"
            }

        return {
            "check": self.name,
            "status": "PASS",
            "details": "All required Python packages are installed"
        }


# 6. Internet Connectivity Check
class InternetConnectivityCheck:

    name = "Internet Connectivity"

    def run(self):
        try:
            connection = socket.create_connection(
                ("1.1.1.1", 53),
                timeout=3
            )

            connection.close()

            return {
                "check": self.name,
                "status": "PASS",
                "details": "Internet connection is available"
            }

        except OSError:
            return {
                "check": self.name,
                "status": "WARN",
                "details": "Internet connection is unavailable"
            }
            # 7. RAM Check
class RAMCheck:
    name = "RAM Check"

    def run(self):
        try:
            psutil = importlib.import_module("psutil")

            memory = psutil.virtual_memory()
            total_ram = memory.total / (1024 ** 3)
            available_ram = memory.available / (1024 ** 3)

            return {
                "check": self.name,
                "status": "PASS",
                "details": (
                    f"Total RAM: {total_ram:.2f} GB, "
                    f"Available RAM: {available_ram:.2f} GB"
                )
            }

        except ImportError:
            return {
                "check": self.name,
                "status": "WARN",
                "details": "psutil package is not installed"
            }


# 8. Disk Space Check
class DiskSpaceCheck:
    name = "Disk Space Check"

    def run(self):
        try:
            psutil = importlib.import_module("psutil")

            disk = psutil.disk_usage("/")
            total_space = disk.total / (1024 ** 3)
            free_space = disk.free / (1024 ** 3)

            return {
                "check": self.name,
                "status": "PASS",
                "details": (
                    f"Total Disk: {total_space:.2f} GB, "
                    f"Free Disk: {free_space:.2f} GB"
                )
            }

        except ImportError:
            return {
                "check": self.name,
                "status": "WARN",
                "details": "psutil package is not installed"
            }