from .genre import Genre, GenreSchema
from .director import Director, DirectorSchema
from .movie import Movie, MovieSchema
from .user import User, UserSchema
from .favourites import Favourite, FavouriteSchema

__all__ = [
    "Genre",
    "GenreSchema",
    "Director",
    "DirectorSchema",
    "Movie",
    "MovieSchema",
    "User",
    "UserSchema",
    "Favourite",
    "FavouriteSchema"
]