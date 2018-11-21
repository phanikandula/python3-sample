import pytest

from mymusiclib.scales import MinorPentatonicScale, ChromaticScale


@pytest.fixture()
def a_minor_pentatonic():
    return MinorPentatonicScale().key("A")


def test_minor_pentatonic_scale_has_five_intervals(a_minor_pentatonic):
    assert len(a_minor_pentatonic) == 5


def test_a_minor_scale(a_minor_pentatonic):
    assert ['A', 'C', 'D', 'E', 'G'] == a_minor_pentatonic


def test_print_all_minor_pentatonic():
    print('\nAll Minor Pentatonic Scales:')
    for ch in ChromaticScale.scale:
        print('{0} - {1}'.format(ch, MinorPentatonicScale().key(ch)))


def test_minor_pentatonic_with_guitar_open_strings():
    print('\nAll Minor Pentatonic Scales that can be played with Guitar open strings:')
    guitar_open_strings = ['E', 'A', 'D', 'G', 'B', 'E']
    for ch in ChromaticScale.scale:
        scale = MinorPentatonicScale().key(ch)
        if set(scale) == set(guitar_open_strings):
            print('{0} - {1}'.format(ch, scale))


def test_minor_pentatonic_with_no_sharps():
    print('\nAll Minor Pentatonic Scales that have no sharps:')
    for ch in ChromaticScale.scale:
        scale = MinorPentatonicScale().key(ch)
        if len([ch for ch in scale if not ch.endswith("#")]) == 5:
            print('{0} - {1}'.format(ch, scale))


def test_minor_pentatonic_with_only_sharps():
    print('\nAll Major Pentatonic Scales that have only sharps:')
    for ch in ChromaticScale.scale:
        scale = MinorPentatonicScale().key(ch)
        if len([ch for ch in scale if ch.endswith("#")]) == 5:
            print('{0} - {1}'.format(ch, scale))