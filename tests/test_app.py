import pytest
from app import main

def test_app_runs_without_error(monkeypatch):
    """
    Test that the application runs without raising an exception.
    """
    monkeypatch.setattr("streamlit.title", lambda x: None)
    monkeypatch.setattr("streamlit.write", lambda x: None)
    monkeypatch.setattr("streamlit.error", lambda x: None)
    assert main() is None
