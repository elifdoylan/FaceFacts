from ..database import db


class Blog(db.Model):
    __bind_key__ = "blogs"
    __tablename__ = "blogs"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(255), nullable=False)

    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def json(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "author": self.author,
        }
