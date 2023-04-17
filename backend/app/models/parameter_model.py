from sqlmodel import SQLModel, Relationship, Field
from typing import Optional, List
from uuid import UUID

from app.models.base_model import BaseUUIDModel


class ParameterBase(SQLModel):
    title: str


class Parameter(BaseUUIDModel, ParameterBase, table=True):
    category: Optional["Category"] = Relationship(
        back_populates="parameters", sa_relationship_kwargs={"lazy": "joined"}
    )
    category_id: Optional[UUID] = Field(default=None, foreign_key="Category.id")

    workspace: Optional["Workspace"] = Relationship(
        back_populates="parameters", sa_relationship_kwargs={"lazy": "joined"}
    )
    workspace_id: Optional[UUID] = Field(default=None, foreign_key="Workspace.id")

