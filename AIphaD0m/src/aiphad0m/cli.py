from __future__ import annotations

import argparse
import json
from pathlib import Path

import yaml

from aiphad0m.pipeline.orchestrator import Orchestrator


def main() -> None:
    parser = argparse.ArgumentParser(description="Build an engine-neutral AIphaD0m session plan.")
    parser.add_argument("--config", default="config/default.yaml", help="Path to YAML configuration.")
    args = parser.parse_args()

    config_path = Path(args.config)
    if not config_path.exists():
        raise SystemExit(f"Configuration not found: {config_path}")

    with config_path.open("r", encoding="utf-8") as handle:
        config = yaml.safe_load(handle)

    plan = Orchestrator().build(config)
    output_dir = Path(config["session"].get("output_directory", "output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "session_plan.json"
    output_path.write_text(json.dumps(plan.to_dict(), indent=2), encoding="utf-8")
    print(f"AIphaD0m session plan written to {output_path}")


if __name__ == "__main__":
    main()
