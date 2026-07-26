from aiphad0m.pipeline.orchestrator import Orchestrator


def test_session_plan_contains_safety_and_identity_events() -> None:
    config = {
        "session": {"title": "Test", "duration_seconds": 100},
        "identity": {"initial_state": "observer", "maximum_intensity": 0.75},
        "safety": {"allow_immediate_exit": True, "post_session_reorientation": True},
        "dramaturgy": {
            "beats": [
                "anticipation",
                "first_reveal",
                "scale_expansion",
                "void_or_false_ending",
                "collective_climax",
                "release",
                "afterimage",
            ]
        },
    }
    plan = Orchestrator().build(config)
    kinds = {event.kind for event in plan.events}
    assert "safety:immediate_exit_available" in kinds
    assert "identity:embodied_performer" in kinds
    assert len(plan.events) == 14
