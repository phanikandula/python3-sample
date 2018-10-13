import pytest

from mymusiclib.scales import ChromaticScale


@pytest.fixture()
def scale():
    return ChromaticScale.scale


def test_chromatic_scale_must_have_12_notes(scale):
    assert len(scale) == 12


def test_chromatic_scale_must_have_no_e_sharp(scale):
    assert "E#" not in scale


def test_chromatic_scale_must_have_no_b_sharp(scale):
    assert "B#" not in scale
