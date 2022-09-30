from project.exceptions import ItemNotFound


class BaseService:
    def __init__(self, dao):
        self.dao = dao

    def get_one(self, pk):
        """get one item"""
        item = self.dao.get_one(pk)
        if not item:
            raise ItemNotFound(f'Item with pk={pk} not exists.')
        return item

    def get_all(self, page, do_sort=False):
        """get all items"""
        items = self.dao.get_all(page, do_sort)
        if not items:
            raise ItemNotFound
        return items

    def create(self, data):
        """create item"""
        return self.dao.create(data)
