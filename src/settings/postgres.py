from propcache import cached_property
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class PostgresSettings(BaseSettings):
    port: int
    host: str
    username: str = Field(..., validation_alias="user")
    password: str
    db_name: str = Field(..., validation_alias="name")

    @cached_property
    def db_url(self):
        db_url = (
            f"{self.driver}://{self.username}:{self.password}"
            f"@{self.host}{f':{self.port}' if self.port else ''}"
            f"/{self.db_name}"
        )
        return db_url

    model_config = SettingsConfigDict(env_prefix="DATABASE_",)
