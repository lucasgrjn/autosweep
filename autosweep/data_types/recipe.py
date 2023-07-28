import logging
from typing import Iterable

from autosweep.utils import typing_ext
from autosweep.utils import io
from autosweep.data_types import filereader


class Recipe(filereader.FileWRer):

    def __init__(self, recipe: dict):
        super().__init__()
        self.logger = logging.getLogger(self.__class__.__name__)

        self.recipe = recipe

    @classmethod
    def from_dict(cls, data: dict):
        return cls(recipe=data)

    def __eq__(self, other):
        if isinstance(other, Recipe):
            return self.recipe == other.recipe
        else:
            return False

    @property
    def instruments(self) -> tuple[str]:
        """
        Returns the instruments needed to run this recipe.

        :return: The instrument instance names needed
        :rtype: tuple[str]
        """
        return tuple(self.recipe['instruments'])

    def to_json(self, path: typing_ext.PathLike):
        io.write_json(data=self.recipe, path=path)

    def to_dict(self, **kwargs) -> dict:
        return self.recipe

    def tests(self) -> Iterable[tuple]:
        """
        Used to iterate over tests.

        :yields: tuple[str, dict]
        """
        for test in self.recipe['tests']:
            yield tuple(test)
