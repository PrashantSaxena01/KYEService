from src.utils.helpers import ensure_list


def test_ensure_list_wraps_scalars():
    assert ensure_list("a") == ["a"]
    assert ensure_list(["a", "b"]) == ["a", "b"]
    assert ensure_list(None) == []
