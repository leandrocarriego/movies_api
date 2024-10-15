from fastapi import APIRouter


router = APIRouter()


@router.get("/")
def index():
    return {"Hello": "People service"}


@router.get("/people")
def get_all_people():
    return {"endpoint": "get_all_people"}


@router.get("/people/{person_id}")
def get_person(person_id: int):
    return {"endpoint": "get_person", "id": person_id}


@router.get("/people/name/{first_name}")
def get_person_by_first_name(first_name: str):
    return {"endpoint": "get_person_by_first_name", "first_name": first_name}


@router.post("/people")
def create_person():
    return {"endpoint": "create_person"}


@router.put("/people/{person_id}")
def update_person(person_id: int):
    return {"endpoint": "update_person", "id": person_id}


@router.delete("/people/{person_id}")
def delete_person(person_id: int):
    return {"endpoint": "delete_person", "id": person_id}
