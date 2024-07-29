from datetime import datetime, UTC
from typing import Annotated

from sqlalchemy import text
from sqlalchemy.orm import mapped_column

intpk = Annotated[int, mapped_column(primary_key=True, index=True)]  # Integer Primary Key type

created_at = Annotated[datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]
updated_at = Annotated[datetime, mapped_column(
    server_default=text("TIMEZONE('utc', now())"),
    onupdate=datetime.now(UTC)
)]

str_256 = Annotated[str, 256]
str_128 = Annotated[str, 128]
str_64 = Annotated[str, 64]
str_8 = Annotated[str, 8]
