import pytest

from project.dao import DirectorDAO

from project.dao.models import Director


class TestDirectorsDAO:

    @pytest.fixture
    def directors_dao(self, db):
        return DirectorDAO(db.session, model=Director)

    @pytest.fixture
    def director_1(self, db):
        d = Director(id=1, name="Гай")
        db.session.add(d)
        db.session.commit()
        return d

    @pytest.fixture
    def director_2(self, db):
        d = Director(name="Риччи")
        db.session.add(d)
        db.session.commit()
        return d

    def test_get_one(self, director_1, directors_dao):
        assert directors_dao.get_one(director_1.id) == director_1

    def test_get_all(self, director_1, director_2, directors_dao):
        assert directors_dao.get_all() == [director_1, director_2]

    def test_create(self, directors_dao, director_2):
        data = {

            "name": "Test"
        }
        new_director = directors_dao.create(data)
        assert new_director.id is not None
        assert new_director.name == "Test"


