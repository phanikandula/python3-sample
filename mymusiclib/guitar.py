from mymusiclib.scales import ChromaticScale

class OpenStrings:
    string6 = ChromaticScale().key("E")
    string5 = ChromaticScale().key("A")
    string4 = ChromaticScale().key("D")
    string3 = ChromaticScale().key("G")
    string2 = ChromaticScale().key("B")

    def notes(self, fret=0):
        assert -1 < fret < 13
        return [OpenStrings.string6[fret],
                OpenStrings.string5[fret],
                OpenStrings.string4[fret],
                OpenStrings.string3[fret],
                OpenStrings.string2[fret]]