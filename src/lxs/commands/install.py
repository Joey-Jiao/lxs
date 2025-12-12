from typing import Annotated

import typer

from lxs import config, modules
from lxs.core import distro, ui

app = typer.Typer(help="Install system modules")


@app.callback(invoke_without_command=True)
def install(
    ctx: typer.Context,
    module_names: Annotated[
        list[str] | None,
        typer.Argument(help="Modules to install"),
    ] = None,
    all_modules: Annotated[
        bool,
        typer.Option("--all", "-a", help="Install all modules"),
    ] = False,
    list_only: Annotated[
        bool,
        typer.Option("--list", "-l", help="List available modules"),
    ] = False,
) -> None:
    if list_only:
        ui.info("Available modules:")
        for name in modules.list_modules():
            ui.console.print(f"  - {name}")
        return

    if all_modules:
        module_names = modules.list_modules()
    elif not module_names:
        ui.error("No modules specified. Use --all or provide module names.")
        ui.info(f"Available: {', '.join(modules.list_modules())}")
        raise typer.Exit(1)

    for name in module_names:
        if name not in modules.MODULES:
            ui.error(f"Unknown module: {name}")
            ui.info(f"Available: {', '.join(modules.list_modules())}")
            raise typer.Exit(1)

    ui.section("Linux Setup")
    distro.detect()

    for name in module_names:
        modules.run_module(name)

    ui.section("Setup Complete")
    ui.ok("All requested modules have been installed")
    ui.info("You may need to re-login for some changes to take effect")
