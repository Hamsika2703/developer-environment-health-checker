class DiagnosticError(Exception):
    """Base exception for diagnostic errors."""


class CheckError(DiagnosticError):
    """Raised when a system check fails unexpectedly."""


class ReportError(DiagnosticError):
    """Raised when a diagnostic report cannot be saved."""


class InvalidInputError(DiagnosticError):
    """Raised when user input is invalid."""