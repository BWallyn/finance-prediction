"""finance-prediction file for ensuring the package is executable
as `finance-prediction` and `python -m finance_prediction`
"""
import sys
from pathlib import Path

from kedro.framework.cli.utils import find_run_command
from kedro.framework.project import configure_project


def main(*args, **kwargs):
    package_name = Path(__file__).parent.name
    configure_project(package_name)

    interactive = hasattr(sys, 'ps1')
    kwargs["standalone_mode"] = not interactive

    run = find_run_command(package_name)
    run(*args, **kwargs)


if __name__ == "__main__":
    main()
