"""Locating, loading and walking a model's BUML source. Requires `besser`,
i.e. the `.venv-puml` interpreter -- only import this from scripts that
already need it.
"""
from __future__ import annotations

import importlib.util
import sys
import uuid
from pathlib import Path

from besser.BUML.metamodel.project import Project
from besser.BUML.metamodel.structural import DomainModel

OLD_GLOB = "*_BUML_model.py"
NEW_GLOB = "*_buml.py"


def find_buml_file(model_dir: Path) -> Path | None:
    """The model's BUML source file -- older models use `*_BUML_model.py`,
    newer ones `*_buml.py`."""
    matches = list(model_dir.glob(OLD_GLOB)) or list(model_dir.glob(NEW_GLOB))
    return matches[0] if matches else None


def load_domain_model(file_path: Path) -> DomainModel:
    """Executes the BUML source under a unique throwaway module name (so
    models loaded in the same worker process never collide) and returns its
    DomainModel -- either a top-level one, or the first model of a Project."""
    module_name = f"buml_model_{uuid.uuid4().hex}"
    spec = importlib.util.spec_from_file_location(module_name, str(file_path))
    if spec is None or spec.loader is None:
        raise ValueError(f"Could not load Python module from path: {file_path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    try:
        spec.loader.exec_module(module)
    finally:
        sys.modules.pop(module_name, None)
    for value in vars(module).values():
        if isinstance(value, DomainModel):
            return value
    for value in vars(module).values():
        if isinstance(value, Project) and value.models:
            return value.models[0]
    raise ValueError(f"No DomainModel found in {file_path}")


def type_name(value) -> str:
    return value.name if hasattr(value, "name") else str(value)


def ordered_ends(association):
    """Deterministic (end1, end2): association.ends is a set, so list order
    varies between runs under hash randomization."""
    ends = list(getattr(association, "ends", []))
    if len(ends) != 2:
        return None

    def end_key(end):
        multiplicity = getattr(end, "multiplicity", None)
        return (
            type_name(getattr(end, "type", "")),
            str(getattr(end, "name", "")),
            str(getattr(multiplicity, "min", "")),
            str(getattr(multiplicity, "max", "")),
            bool(getattr(end, "is_navigable", False)),
            bool(getattr(end, "is_composite", False)),
            bool(getattr(end, "is_aggregation", False)),
        )

    ordered = sorted(ends, key=end_key)
    return ordered[0], ordered[1]
