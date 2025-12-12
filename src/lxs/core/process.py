import shutil
import subprocess
from pathlib import Path

from lxs.core import ui


def run(
    cmd: list[str],
    check: bool = True,
    capture: bool = False,
    cwd: Path | None = None,
) -> subprocess.CompletedProcess[str]:
    ui.info(f"Running: {' '.join(cmd)}")
    result = subprocess.run(
        cmd,
        check=check,
        capture_output=capture,
        text=True,
        cwd=cwd,
    )
    return result


def run_quiet(cmd: list[str], cwd: Path | None = None) -> bool:
    try:
        subprocess.run(
            cmd,
            check=True,
            capture_output=True,
            text=True,
            cwd=cwd,
        )
        return True
    except subprocess.CalledProcessError:
        return False


def is_installed(cmd: str) -> bool:
    return shutil.which(cmd) is not None


def run_shell(script: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        script,
        shell=True,
        check=check,
        capture_output=False,
        text=True,
    )
