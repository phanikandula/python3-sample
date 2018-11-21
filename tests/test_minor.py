import pytest

from mymusiclib.scales import MinorScale, ChromaticScale


@pytest.fixture()
def a_minor():
    return MinorScale().key("A")


def test_minor_scale_has_seven_intervals(a_minor):
    assert len(set(a_minor)) == 7  # 7 plus 1 for octave - so use set to remove dup


def test_c_minor_scale(a_minor):
    assert ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'A'] == a_minor


def test_minor_with_no_sharps():
    print('\nAll Major Scales that have no sharps:')
    for ch in ChromaticScale.scale:
        scale = MinorScale().key(ch)
        if len([ch for ch in scale if not ch.endswith("#")]) == 8:
            print('{0} - {1}'.format(ch, scale))
