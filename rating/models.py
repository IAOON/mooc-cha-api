from tortoise import models, fields
from tortoise.contrib.pydantic import pydantic_model_creator

class Ratable(models.Model):
    id = fields.IntField(pk=True)
    name = fields.TextField()
    description = fields.TextField()


class Lecture(Ratable):
    pass


class Rating(models.Model):
    target = fields.ForeignKeyField('rating.Ratable', related_name="ratings")


LecturePydantic = pydantic_model_creator(Lecture, name="Lecture")
