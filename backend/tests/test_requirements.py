import pytest
from fastapi import HTTPException
from unittest.mock import AsyncMock, Mock

from app.models.Requirements import Requirements
from app.schemas.requirement_schema import RequirementCreate, RequirementUpdate

from app.services.requirement_sevice import (
    add_new_requirements,
    get_all_requiments,
    update_requirement
)


@pytest.fixture
def mock_db(monkeypatch):
    """Mock AsyncSession with AsyncMock."""
    db = Mock()

    db.execute = AsyncMock()
    db.add = Mock()
    db.commit = AsyncMock()
    db.refresh = AsyncMock()

    return db


# ---------------------------------------------------------
# TEST: get_all_requirements()
# ---------------------------------------------------------
@pytest.mark.asyncio
async def test_get_all_requirements_success(mock_db):
    
    fake_requirement = Requirements(req_name="Brake System")

    class FakeScalar:
        def all(self):
            return [fake_requirement]

    class FakeResult:
        def scalars(self):
            return FakeScalar()

    mock_db.execute.return_value = FakeResult()

    result = await get_all_requiments(mock_db)

    assert len(result) == 1
    assert result[0].req_name == "Brake System"


@pytest.mark.asyncio
async def test_get_all_requirements_empty(mock_db):

    class FakeScalar:
        def all(self):
            return []

    class FakeResult:
        def scalars(self):
            return FakeScalar()
    mock_db.execute.return_value = FakeResult()

    with pytest.raises(HTTPException):
        await get_all_requiments(mock_db)


# ---------------------------------------------------------
# TEST: add_new_requirements()
# ---------------------------------------------------------
@pytest.mark.asyncio
async def test_add_new_requirement_success(mock_db):

    new_req = RequirementCreate(req_name="Engine Control")

    class FakeResult:
        def scalar_one_or_none(self):
            return None

    mock_db.execute.return_value = FakeResult()

    result = await add_new_requirements(mock_db, new_req)

    assert isinstance(result, Requirements)
    assert result.req_name == "Engine Control"


@pytest.mark.asyncio
async def test_add_new_requirement_exists(mock_db):

    new_req = RequirementCreate(req_name="Engine Control")

    class FakeResult:
        def scalar_one_or_none(self):
            return Requirements(req_name="Engine Control")

    mock_db.execute.return_value = FakeResult()

    with pytest.raises(HTTPException) as exc:
        await add_new_requirements(mock_db, new_req)

    assert exc.value.status_code == 422


# ---------------------------------------------------------
# TEST: update_requirement()
# ---------------------------------------------------------
@pytest.mark.asyncio
async def test_update_requirement_success(mock_db):

    update_data = RequirementUpdate(req_name="Suspension")
    requirement_id = 1
    existing_req = Requirements(req_name="Suspension")

    class FakeResult:
        def scalar_one_or_none(self):
            return existing_req

    mock_db.execute.return_value = FakeResult()

    result = await update_requirement(mock_db, requirement_id, update_data)

    assert result.req_name == "Suspension"


@pytest.mark.asyncio
async def test_update_requirement_not_found(mock_db):

    update_data = RequirementUpdate(req_name="NotFound")
    requirement_id = 999
    class FakeResult:
        def scalar_one_or_none(self):
            return None

    mock_db.execute.return_value = FakeResult()

    with pytest.raises(HTTPException):
        await update_requirement(mock_db, requirement_id, update_data) 
