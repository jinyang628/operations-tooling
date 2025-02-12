import os
from typing import Optional

from postgrest._async.request_builder import AsyncQueryRequestBuilder
from pydantic import BaseModel
from supabase._async.client import AsyncClient as Client
from supabase._async.client import create_client

from app.utils.boolean_clause import (
    BooleanClause,
    apply_boolean_clause,
)


class DatabaseClient:
    _instance: "DatabaseClient"
    _client: Optional[Client] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    async def _init(self):
        if self._instance is not self:
            raise RuntimeError("_init() should only be called through get_instance()")

        if not self._client:
            self._client = await create_client(
                supabase_url=os.environ["SUPABASE_URL"],
                supabase_key=os.environ["SUPABASE_SERVICE_KEY"],
            )

    @classmethod
    async def get_instance(cls) -> "DatabaseClient":
        if not cls._instance:
            client = cls()
            await client._init()
        return cls._instance

    async def post(self, table_name: str, data: BaseModel):
        if not self._client:
            raise TypeError("Database client is not initialized when executing a POST request")
        return await self._client.table(table_name).insert(data.model_dump()).execute()

    async def get(
        self,
        table_name: str,
        column_names: list[str] = [],
        boolean_clause: Optional[BooleanClause] = None,
    ):
        if not self._client:
            raise TypeError("Database client is not initialized when executing a GET request")

        query = self._client.table(table_name).select(
            ", ".join(column_names) if column_names else "*"
        )
        query: AsyncQueryRequestBuilder = apply_boolean_clause(
            query=query, boolean_clause=boolean_clause
        )
        return await query.execute()
