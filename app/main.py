from enum import Enum
from fastapi import FastAPI, status
from pydantic import BaseModel
from faker import Faker

app = FastAPI()
faker = Faker()


class SexEnum(str, Enum):
    male = "Male"
    female = "Female"


class Person(BaseModel):
    first_name: str
    last_name: str
    birthday: str
    login: str
    password: str


@app.post("/person", status_code=status.HTTP_200_OK)
async def person(
    sex: SexEnum,
    age: int
):
    """Get person data"""

    fake_person = faker.get_person(
        sex=sex,
        age=age
    )

    person = Person(
        first_name=fake_person["first_name"],
        last_name=fake_person["last_name"],
        birthday=fake_person["birthday"],
        login=fake_person["login"],
        password=fake_person["password"]
    )

    return person


@app.post("/persons", status_code=status.HTTP_200_OK)
async def persons(
    sex: SexEnum,
    age: int,
    count: int = 2
):
    """Get persons data"""

    persons = []

    for _ in range(count):
        fake_person = faker.get_person(
            sex=sex,
            age=age
        )

        person = Person(
            first_name=fake_person["first_name"],
            last_name=fake_person["last_name"],
            birthday=fake_person["birthday"],
            login=fake_person["login"],
            password=fake_person["password"]
        )
        persons.append(person)

    return persons
