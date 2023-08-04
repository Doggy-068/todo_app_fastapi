import strawberry
from fastapi import Depends
from sqlalchemy.orm import Session
from strawberry.types import Info
from strawberry.fastapi import GraphQLRouter
from app.database.database import get_db
from app.database.model import Continent, Country, City


@strawberry.type
class CityType:
    id: int
    code: str
    name: str
    country_id: int


@strawberry.type
class CountryType:
    id: int
    code: str
    name: str
    continent_id: int

    @strawberry.field
    async def cities(self, info: Info) -> list[CityType]:
        return info.context['db'].query(City).filter(City.country_id == self.id).all()


@strawberry.type
class ContinentType:
    id: int
    code: str
    name: str

    @strawberry.field
    async def countries(self, info: Info) -> list[CountryType]:
        return info.context['db'].query(Country).filter(Country.continent_id == self.id).all()


@strawberry.type
class Query:
    @strawberry.field
    async def continents(self, info: Info) -> list[ContinentType]:
        return info.context['db'].query(Continent).all()

    @strawberry.field
    async def countries(self, info: Info) -> list[CountryType]:
        return info.context['db'].query(Country).all()

    @strawberry.field
    async def cities(self, info: Info) -> list[CityType]:
        return info.context['db'].query(City).all()


def get_context(db: Session = Depends(get_db)):
    return {'db': db}


router = GraphQLRouter(strawberry.Schema(Query), path='/graphql', context_getter=get_context)
