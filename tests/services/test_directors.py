from unittest.mock import MagicMock

import pytest

from project.dao import DirectorDAO
from project.dao.models import Director
from project.services import DirectorService


@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(None, model=Director)
    director_one = Director(id=1, name='test_director_one')
    director2_two = Director(id=2, name='test_director_two')
    director3_three = Director(id=3, name='test_director_three')
    director_dao.get_one = MagicMock(return_value=director_one)
    director_dao.get_all = MagicMock(return_value=[director_one, director2_two, director3_three])
    director_dao.create = MagicMock(return_value=Director(id=2))

    return director_dao


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(dao=director_dao)

    def test_get_one(self):
        director = self.director_service.get_one(1)
        assert director is not None
        assert director.id is not None

    def test_get_all(self):
        directors = self.director_service.get_all(page=1)
        assert len(directors) > 0

    def test_create(self):
        director_data = {
            'name': 'test_name'
        }
        director = self.director_service.create(director_data)
        assert director.id is not None

