from app import db # we already defined db instance inside app/__init__.py file
from datetime import datetime



################## Publication class ##############################
class Publication(db.Model):
    __tablename__ = 'publication'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), nullable = False)

    def __init__(self, name):
        # self.id = id   # it will be generated automatically
        self.name = name

    def __repr__(self):
        return 'Publisher is {}'.format(self.name)

##############Book ###########################
class Book(db.Model):
    __tablename__ = 'book'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(500), nullable = False, index = True)
    author = db.Column(db.String(350))
    avg_rating = db.Column(db.Float)
    format = db.Column(db.String(50))
    image = db.Column(db.String(100), unique = True)
    num_pages = db.Column(db.Integer)
    #for the following, first import => from datetime import datetime
    pub_date = db.Column(db.DateTime, default = datetime.utcnow())

    #relationship
    pub_id = db.Column(db.Integer, db.ForeignKey('publication.id'))

    def __init__(self, title, author, avg_rating, book_format, image, num_pages, pub_id):

        self.title = title
        self.author = author
        self.avg_rating = avg_rating
        self.format = book_format
        self.image = image
        self.num_pages = num_pages
        self.pub_id = pub_id

    def __repr__(self):
        return '{} by {}'.format(self.title, self.author)
