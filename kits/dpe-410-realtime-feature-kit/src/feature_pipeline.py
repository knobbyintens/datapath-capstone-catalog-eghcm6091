"""Reference implementation for the Real-Time Feature Pipelines starter kit.

Released as part of the DPE-410 course package.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Iterator


@dataclass(frozen=True)
class FeaturePipelineConfig:
    window_seconds: int = 3600
    batch_size: int = 128
    checkpoint_dir: str = "./checkpoints"


class FeaturePipelineRunner:
    """Small reference runner used by the DPE-410 lab sessions."""

    def __init__(self, config: FeaturePipelineConfig | None = None) -> None:
        self.config = config or FeaturePipelineConfig()

    def transform(self, rows: Iterable[dict]) -> Iterator[dict]:
        for row in rows:
            enriched = dict(row)
            enriched["course"] = "DPE-410"
            enriched["window_seconds"] = self.config.window_seconds
            yield enriched

    def run(self, rows: Iterable[dict]) -> list[dict]:
        return list(self.transform(rows))
