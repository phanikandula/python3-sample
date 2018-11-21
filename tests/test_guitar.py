import pytest

from mymusiclib.guitar import OpenStrings
from mymusiclib.scales import ChromaticScale, MinorPentatonicScale, MajorPentatonicScale


def test_open_strings():
    o = OpenStrings()
    print(o.notes())


def test_open_strings_fret1():
    o = OpenStrings()
    print(o.notes(1))


def test_open_strings_fret12():
    o = OpenStrings()
    print(o.notes(11))


@pytest.fixture
def all_frets():
    o = OpenStrings()
    guitar_frets = {}
    for i in range(12):
        guitar_frets[i] = o.notes(i)
    return guitar_frets


@pytest.fixture()
def all_minor_scales():
    minor_scales = {}
    for ch in ChromaticScale.scale:
        minor_scales[ch] = MinorPentatonicScale().key(ch)
    return minor_scales


@pytest.fixture()
def all_major_scales():
    major_scales = {}
    for ch in ChromaticScale.scale:
        major_scales[ch] = MajorPentatonicScale().key(ch)
    return major_scales


def test_minor_pentatonic_with_guitar_open_strings(all_frets, all_minor_scales):
    print('\nAll Minor Pentatonic Scales that can be played with Guitar open strings:')
    for f in all_frets:
        guitar_set = set(all_frets[f])
        for s in all_minor_scales:
            scale_set = set(all_minor_scales[s])
            if scale_set == guitar_set:
                print('Minor scale of {0} Can be played at fret {1} : {2}'.format(s, f, all_minor_scales[s]))


def test_major_pentatonic_with_guitar_open_strings(all_frets, all_major_scales):
    print('\nAll Major Pentatonic Scales that can be played with Guitar open strings:')
    for f in all_frets:
        guitar_set = set(all_frets[f])
        for s in all_major_scales:
            scale_set = set(all_major_scales[s])
            if scale_set == guitar_set:
                print('Major scale of {0} Can be played at fret {1} : {2}'.format(s, f, all_major_scales[s]))
