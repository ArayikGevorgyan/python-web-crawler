from dataclasses import dataclass, field

@dataclass
class CrawlResult:
    pages: dict[str, list[str]] = field(default_factory=dict)
    errors: dict[str, str] = field(default_factory=dict)
    fetch_count: int = 0  # distinct URLs initially dispatched
    attempts: int = 0     # includes retries
    stopped: bool = False
