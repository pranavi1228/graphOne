from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime


@dataclass
class Source:
    name: str
    url: str


@dataclass
class StartupContent:
    entityName: str
    employeeCount: Optional[int] = None


@dataclass
class StartupEntity:
    schemaVersion: str = "1.0"
    recordType: str = "STARTUP"
    source: Source = None
    content: StartupContent = None
    collectedAt: str = field(
        default_factory=lambda: datetime.utcnow().isoformat()
    )


@dataclass
class ProductContent:
    startupName: str
    pricingModel: str


@dataclass
class ProductEntity:
    schemaVersion: str = "1.0"
    recordType: str = "PRODUCT"
    source: Source = None
    content: ProductContent = None
    collectedAt: str = field(
        default_factory=lambda: datetime.utcnow().isoformat()
    )


@dataclass
class PaperContent:
    title: str
    authors: List[str]
    paper_url: str
    github_url: Optional[str] = None
    github_stars: Optional[int] = None
    published_date: Optional[str] = None


@dataclass
class ResearchPaperEntity:
    schemaVersion: str = "1.0"
    recordType: str = "RESEARCH_PAPER"
    content: PaperContent = None


@dataclass
class JobContent:
    company: str
    date: str
    is_remote: bool
    role_family: str


@dataclass
class JobEntity:
    schemaVersion: str = "1.0"
    recordType: str = "JOB"
    content: JobContent = None