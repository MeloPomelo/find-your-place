from uuid import UUID
from typing import List, Optional

from app.models.workspace_model import WorkspaceBase
from app.models.image_media_model import ImageMedia
from app.schemas.image_media_schema import ImageMediaRead
from app.schemas.comment_schema import CommentRead
from app.schemas.dictionary_schema import DictionaryRead
from app.schemas.response_schemas import PostResponseBase


class WorkspaceCreate(WorkspaceBase):
    # images: Optional[List[PostResponseBase[ImageMedia]]] = []
    images_id: Optional[List[UUID]] = []
    pass


class WorkspaceUpdate(WorkspaceBase):
    pass


class WorkspaceRead(WorkspaceBase):
    id: UUID
    images:  Optional[List[ImageMediaRead]] = []
    comments: Optional[List[CommentRead]] = []
    parameters: Optional[List[DictionaryRead]] = []