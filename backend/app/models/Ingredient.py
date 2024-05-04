from ..database import db


class Ingredient(db.Model):
    __bind_key__ = "ingredients"
    __tablename__ = "ingredients"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    isHarmful = db.Column(db.Boolean, nullable=False)
    harmfulSkin = db.Column(db.String(255), nullable=False)

    def __init__(self, name, isHarmful, harmfulSkin):
        self.name = name
        self.isHarmful = isHarmful
        self.harmfulSkin = harmfulSkin

    def json(self):
        return {"id": self.id, "name": self.name, "isHarmful": self.isHarmful, "harmfulSkin": self.harmfulSkin}
