import collections
from abc import ABC, abstractmethod
from typing import List


class ChromaticScale(ABC):
    scale = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]

    @abstractmethod
    def interval(self) -> List[int]:
        return [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    @staticmethod
    def valid_key(k: str):
        assert k in ChromaticScale.scale

    @abstractmethod
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
