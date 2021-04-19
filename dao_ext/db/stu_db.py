from dao.base import BaseDao
from entity import Student


class StudentDao(BaseDao):
    def query(self, where=None, whereargs=None):
        ret = super(StudentDao, self).query('Student', 'id', 'name', 'age', 'sex', where=where, whereargs=whereargs)
        return [Student(item['id'], item['name'], item['age'], item['sex']) for item in ret]


if __name__ == '__main__':
    dao = StudentDao()
    res = dao.query(where='where sex=%s', whereargs=('男',))
    print(res)
