import importlib
import os


def get_setting(name: str, default=None):
    try:
        config = importlib.import_module("config")
    except ModuleNotFoundError as exc:
        if exc.name != "config":
            raise
        value = os.environ.get(name, default)
        if value is None:
            raise RuntimeError(
                f"config.py is not present. Add {name} to local.settings.json "
                "under Values, or create config.py with that setting."
            )
        return value

    return getattr(config, name, os.environ.get(name, default))
