"""Representations of authors, author lists, and author queries."""

from dataclasses import dataclass, field
from search.domain.base import Query


@dataclass
class Author:
    """An author query part, for use in an :class:`.AuthorQuery`."""

    forename: str = field(default_factory=str)
    surname: str = field(default_factory=str)
    fullname: str = field(default_factory=str)

    # TODO: gawd this is ugly.
    def __str__(self) -> str:
        """Print the author name."""
        if self.fullname and self.surname:
            if self.forename:
                name = f'{self.forename}[f] {self.surname}[s]'
            else:
                name = f'{self.surname}[s]'
            name = f'{name} OR {self.fullname}'
        elif self.fullname:
            name = self.fullname
        else:
            if self.forename:
                name = f'{self.forename}[f] {self.surname}[s]'
            else:
                name = f'{self.surname}[s]'
        return name


class AuthorList(list):
    """A list of author query parts, for use in an :class:`AuthorQuery`."""

    def __str__(self) -> str:
        """Print a comma-delimited list of authors."""
        if len(self) == 0:
            return ''
        if len(self) > 1:
            return ' AND '.join([f"({str(au)})" for au in self])
        return str(self[0])


@dataclass
class AuthorQuery(Query):
    """Represents a query by author name."""

    authors: AuthorList = field(default_factory=AuthorList)