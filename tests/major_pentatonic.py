import pytest

from mymusiclib.scales import MajorPentatonicScale, ChromaticScale


@pytest.fixture()
def c_major_pentatonic():
    return MajorPentatonicScale().key("C")


def test_major_scale_has_seven_intervals(c_major_pentatonic):
    assert len(c_major_pentatonic) == 5


def test_c_major_scale(c_major_pentatonic):
    assert ['C', 'D', 'E', 'G', 'A'] == c_major_pentatonic


def test_print_all_major_pentatonic():
    print('\nAll Major Pentatonic Scales:')
    for ch in ChromaticScale.scale:
        print('{0} - {1}'.format(ch, MajorPentatonicScale().key(ch)))


def test_major_pentatonic_with_guitar_open_strings():
    print('\nAll Major Pentatonic Scales that can be played with Guitar open strings:')
    guitar_open_strings = ['E', 'A', 'D', 'G', 'B', 'E']
    for ch in ChromaticScale.scale:
        scale = MajorPentatonicScale().key(ch)
        if set(scale) == set(guitar_open_strings):
            print('{0} - {1}'.format(ch, MajorPentatonicScale().key(ch)))


def test_major_pentatonic_with_no_sharps():
    print('\nAll Major Pentatonic Scales that have no sharps:')
    for ch in ChromaticScale.scale:
        scale = MajorPentatonicScale().key(ch)
        if len([ch for ch in scale if not ch.endswith("#")]) == 5:
            print('{0} - {1}'.format(ch, MajorPentatonicScale().key(ch)))


def test_major_pentatonic_with_only_sharps():
    print('\nAll Major Pentatonic Scales that have only sharps:')
    for ch in ChromaticScale.scale:
        scale = MajorPentatonicScale().key(ch)
        if len([ch for ch in scale if ch.endswith("#")]) == 5:
            print('{0} - {1}'.format(ch, MajorPentatonicScale().key(ch)))
