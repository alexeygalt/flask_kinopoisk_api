from .movies import movie_ns
from .directors import director_ns
from .genres import genre_ns
from .auth import auth_ns
from .users import user_ns
from .favourites import favourite_ns


__all__ = [
    "movie_ns",
    "director_ns",
    "genre_ns",
    "user_ns",
    "auth_ns",
    "favourite_ns"
]
