"""Tests for the main module."""

from ai_3d_print.main import hello_world


def test_hello_world():
    """Test the hello_world function."""
    result = hello_world()
    assert result == "Hello, AI 3D Print!"
    assert isinstance(result, str)
