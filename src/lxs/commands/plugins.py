from typing import Annotated

import typer

from lxs import config
from lxs.core import process, ui

app = typer.Typer(help="Manage zsh plugins")


@app.command("list")
def list_plugins() -> None:
    plugins_dir = config.DIR_ZSH_PLUGINS

    if not plugins_dir.exists():
        ui.warn("No plugins installed yet")
        return

    ui.info("Installed plugins:")
    for plugin in plugins_dir.iterdir():
        if plugin.is_dir():
            ui.console.print(f"  - {plugin.name}")


@app.command("update")
def update_plugins(
    name: Annotated[
        str | None,
        typer.Argument(help="Plugin name to update (all if not specified)"),
    ] = None,
) -> None:
    gitmodules = config.PROJECT_ROOT / ".gitmodules"
    if not gitmodules.exists():
        ui.error("No git submodules found")
        return

    if name:
        plugin_path = f"dotfiles/zsh/plugins/{name}"
        ui.step(f"Updating plugin: {name}")
        process.run(
            ["git", "submodule", "update", "--remote", plugin_path],
            cwd=config.PROJECT_ROOT,
        )
    else:
        ui.step("Updating all plugins")
        process.run(
            ["git", "submodule", "update", "--remote"],
            cwd=config.PROJECT_ROOT,
        )

    ui.ok("Plugins updated")
    ui.info("Run 'lxs install shell' to reinstall updated plugins")
