from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise, HTTPNotFoundError

from rating.models import Lecture, LecturePydantic


app = FastAPI()

@app.get("/hello")
async def sample_server():
    lecture = Lecture(name="Hello", description="World")
    await lecture.save()
    return {"message": "world"}


@app.get("/lectures/{lecture_id}", response_model=LecturePydantic, responses={404: {"model": HTTPNotFoundError}})
async def get_lecture(lecture_id: int):
    return await LecturePydantic.from_queryset_single(Lecture.get(id=lecture_id))


register_tortoise(
    app,
    db_url='postgres://mooc_cha_user:@localhost/mooc_cha',
    modules={'models': ['rating.models']},
    generate_schemas=True,
    add_exception_handlers=True,
)

