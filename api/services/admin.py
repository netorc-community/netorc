from typing import List

from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from core import db
from core.addons.exceptions import APIError
from core.db.models import UserRead, UserCreate
from core.db.tables import User
from core.security.user import create_user

router = APIRouter(prefix="/api/admin/v1", tags=["Administration"])


@router.get("/users", response_model=List[UserRead])
def get_users(username: str = None, session: Session = Depends(db.get_session)) -> list:
    """
    Returns a list of user/'s from the db.

    Args:
        username: an optional username filter.
        session: db session dependency.

    Returns:
        Dictionary/s enclosed in a list containing attributes for a user/s.

    Raises:
        APIException: 500 status code.
    """
    try:

        if username is not None:
            with session as _session:
                user = _session.get(User, username)
                if not user:
                    raise APIError(status_code=404, code="tbd", reason="tbd")

                return [user]

        query = select(User)
        with session as _session:
            result = _session.exec(query)
            return [x for x in result]

    except APIError:
        raise

    except Exception as exc:
        raise APIError(status_code=500, code="tbd", reason="tbd") from exc


@router.post("/users", response_model=UserRead)
def post_users(user_create: UserCreate):
    """
    Creates new users.

    Args:
        user_create: UserCreate object.

    Returns:
        db_user: database User object.

    Raises:
        APIException: 500 status code.

    """
    user = User()
    user_data = user_create.dict(exclude_unset=True)
    for k, v in user_data.items():
        setattr(user, k, v)

    try:
        db_user = create_user(user)
        return db_user

    except Exception as exc:
        raise APIError(status_code=500, code="tbd", reason="tbd") from exc


@router.patch("/users")
def patch_users():
    pass


@router.delete("/users")
def delete_users():
    pass
