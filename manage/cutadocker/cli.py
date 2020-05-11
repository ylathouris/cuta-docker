import typer
from typing import List

from .api import API


cli = typer.Typer()


@cli.command("build")
def build(keys: List[str]):
    """
    Build the given cuta images.
    """
    api = API()
    api.build(*keys)


@cli.command("push")
def push(keys: List[str]):
    """
    Push the given cuta images to docker hub.
    """
    api = API()
    api.push(*keys)


@cli.command("update")
def update(keys: List[str]):
    """
    Update (build & push) the given cuta images to docker hub.
    """
    api = API()
    for key in keys:
        api.build(key)
        api.push(key)
