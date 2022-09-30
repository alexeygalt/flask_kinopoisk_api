from .movie import MovieDAO
from .director import DirectorDAO
from .genre import GenreDAO
from .user import UserDAO
from .favourite import FavouriteDAO

__all__ = [
    "GenreDAO",
    "MovieDAO",
    "DirectorDAO",
    "UserDAO"
]
