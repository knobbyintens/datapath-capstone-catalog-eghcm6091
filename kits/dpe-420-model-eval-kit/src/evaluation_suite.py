"""Reference implementation for the Model Evaluation & Benchmarking starter kit.

Released as part of the DPE-420 course package.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Iterator


@dataclass(frozen=True)
class EvaluationSuiteConfig:
    window_seconds: int = 3600
    batch_size: int = 128
    checkpoint_dir: str = "./checkpoints"


class EvaluationSuiteRunner:
    """Small reference runner used by the DPE-420 lab sessions."""

    def __init__(self, config: EvaluationSuiteConfig | None = None) -> None:
        self.config = config or EvaluationSuiteConfig()

    def transform(self, rows: Iterable[dict]) -> Iterator[dict]:
        for row in rows:
            enriched = dict(row)
            enriched["course"] = "DPE-420"
            enriched["window_seconds"] = self.config.window_seconds
            yield enriched

    def run(self, rows: Iterable[dict]) -> list[dict]:
        return list(self.transform(rows))
