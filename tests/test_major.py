import pytest

from mymusiclib.scales import MajorScale, ChromaticScale


@pytest.fixture()
def c_major():
    return MajorScale().key("C")


def test_major_scale_has_seven_intervals(c_major):
    assert len(set(c_major)) == 7  # 7 plus 1 for octave - so use set to remove dup


def test_c_major_scale(c_major):
    assert ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C'] == c_major


def test_major_with_no_sharps():
    print('\nAll Major Scales that have no sharps:')
    for ch in ChromaticScale.scale:
        scale = MajorScale().key(ch)
        if len([ch for ch in scale if not ch.endswith("#")]) == 8:
            print('{0} - {1}'.format(ch, scale))
