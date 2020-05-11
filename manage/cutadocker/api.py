
import dataclasses
import itertools
import functools
import pathlib
import sys

import docker
import structlog


logger = structlog.get_logger(__name__)


ROOT = pathlib.Path(__file__).parent.parent.parent
IMAGES = {
    "aws-python": ROOT.joinpath("aws", "python", "base"),
    "aws-python3.8": ROOT.joinpath("aws", "python", "3.8"),
    "aws-python3.7": ROOT.joinpath("aws", "python", "3.7"),
    "aws-python3.6": ROOT.joinpath("aws", "python", "3.6"),
    "aws-python2.7": ROOT.joinpath("aws", "python", "2.7"),
}


class API:

    def __init__(self, repo="ylathouris/cuta"):
        self.repo = repo

    @functools.cached_property
    def images(self):
        return IMAGES.copy()

    @property
    def docker(self):
        return docker.from_env()

    def build(self, *keys):
        keys = keys or self.images.keys()
        for key in keys:
            self._build(key)

    def _build(self, key):
        path = str(self.images.get(key))
        tag = f"{self.repo}:{key}"
        logger.info("Building image", tag=tag, path=path)
        for item in self.docker.api.build(path=path, tag=tag, rm=True, decode=True):
            output = item.get("stream", "").rstrip()
            output = output or item.get("aux", {}).get("ID")
            if output:
                logger.info(output)

    def push(self, *keys):
        keys = keys or self.images.keys()
        for key in keys:
            self._push(key)

    def _push(self, key):
        report = {}
        for item in self.docker.api.push(self.repo, tag=key, stream=True, decode=True):
            uid = item.get("id", "")
            status = item.get("status", "")
            progress = item.get("progress")
            lines = []
            if not uid:
                continue

            report[uid] = (status, progress)
            for uid, (status, progress) in report.items():
                msg = f"{uid}: {status}"
                msg = f"{msg}: {progress}" if progress else msg
                logger.info(msg)

            clear_lines(len(report))


def clear_lines(count=1):
    [sys.stdout.write("\x1b[1A\x1b[2K") for _ in range(count)]
