"""Representations of authors, author lists, and author queries."""
from search.domain import Query, Property, Base # type: ignore


class Author(Base):
    """Represents an author."""

    forename = Property('forename', str)
    surname = Property('forensurnameame', str)

    def __str__(self):
        """Prints the author name."""
        if self.forename:
            return f'{self.forename} {self.surname}'
        return self.surname


class AuthorList(list):
    """Represents a list of authors."""

    def __str__(self):
        """Prints comma-delimited list of authors."""
        return ', '.join([str(au) for au in self])


class AuthorQuery(Query):
    """Represents an author query."""

    authors = Property('authors', AuthorList)