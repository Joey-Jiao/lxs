import typer

from lxs.commands import dotfiles, install, plugins

app = typer.Typer(
    name="lxs",
    help="Linux Setup CLI Tool",
    no_args_is_help=True,
)

app.add_typer(install.app, name="install")
app.add_typer(plugins.app, name="plugins")
app.add_typer(dotfiles.app, name="dotfiles")

if __name__ == "__main__":
    app()
