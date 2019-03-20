import collections
from abc import ABC, abstractmethod
from typing import List



class Note:
    pass


class ChromaticScale(ABC):
    scale = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]

    def interval(self) -> List[int]:
        return [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    @staticmethod
    def valid_key(k: str):
        assert k in ChromaticScale.scale

    def key(self, root: str) -> List[str]:
        ChromaticScale.valid_key(root)
        index = ChromaticScale.scale.index(root)
        d = collections.deque(ChromaticScale.scale)
        d.rotate(len(ChromaticScale.scale) - index)
        return list(d)


class MajorScale(ChromaticScale):

    def key(self, root: str) -> List[str]:
        chromatic_scale = super(MajorScale, self).key(root)
        chromatic_scale.append(root)
        result = [root]
        index = 0
        for step in self.interval():
            index += step
            result.append(chromatic_scale[index])
        return result

    def interval(self) -> List[int]:
        return [2, 2, 1, 2, 2, 2, 1]


class MajorPentatonicScale(MajorScale):

    def key(self, root: str) -> List[str]:
        major_scale = super(MajorPentatonicScale, self).key(root)
        result = []
        for step in self.pattern():
            result.append(major_scale[step-1])
        return result

    def pattern(self) -> List[int]:
        return [1, 2, 3, 5, 6]

xyz

class MinorScale(ChromaticScale):

    def key(self, root: str) -> List[str]:
        chromatic_scale = super(MinorScale, self).key(root)
        chromatic_scale.append(root)
        result = [root]
        index = 0
        for step in self.interval():
            index += step
            result.append(chromatic_scale[index])
        return result

    def interval(self) -> List[int]:
        return [2, 1, 2, 2, 1, 2, 2]


class MinorPentatonicScale(MinorScale):

    def key(self, root: str) -> List[str]:
        major_scale = super(MinorPentatonicScale, self).key(root)
        result = []
        for step in self.pattern():
            result.append(major_scale[step-1])
        return result

    def pattern(self) -> List[int]:
        return [1, 3, 4, 5, 7]
