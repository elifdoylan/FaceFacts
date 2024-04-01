from ..database import db


class Ingredient(db.Model):
    __bind_key__ = "ingredients"
    __tablename__ = "ingredients"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    isHarmful = db.Column(db.Boolean, nullable=False)

    def __init__(self, name, isHarmful):
        self.name = name
        self.isHarmful = isHarmful

    def json(self):
        return {"id": self.id, "name": self.name, "isHarmful": self.isHarmful}
