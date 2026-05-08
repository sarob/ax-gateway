from pathlib import Path

DEMO_HTML = Path(__file__).resolve().parents[1] / "ax_cli" / "static" / "demo.html"


def test_agent_row_type_prefers_gateway_asset_type_before_template() -> None:
    source = DEMO_HTML.read_text()

    assert "function publicAgentTypeLabel(agent)" in source
    assert "function publicAgentTypeMeta(label)" in source
    assert 'normalized.includes("on-demand")' in source

    public_type_pos = source.index("const publicType = publicAgentTypeMeta")
    template_pos = source.index('if (template === "ollama")')
    assert public_type_pos < template_pos


def test_agent_row_type_falls_back_to_intake_model_before_template() -> None:
    source = DEMO_HTML.read_text()

    launch_on_send_pos = source.index('intake === "launch_on_send"')
    live_listener_pos = source.index('intake === "live_listener"')
    template_pos = source.index('if (template === "ollama")')

    assert launch_on_send_pos < template_pos
    assert live_listener_pos < template_pos
