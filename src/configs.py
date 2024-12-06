import pydantic_settings


class UserConfig(pydantic_settings.BaseSettings):
    model_config = pydantic_settings.SettingsConfigDict(
        env_prefix="QA_", env_file=".env", frozen=True, extra="ignore"
    )  # frozen - nie będę mogl zmienic atrybutu, extra - ignorujemy dodatkowe zmienne

    username: str = ""
    password: str = ""


# @field_serializer(field:"password",when_user="json")
# def dump_secrect(self, v):
#     return v.get_secrect_value()


class EnvConfig(pydantic_settings.BaseSettings):
    model_config = pydantic_settings.SettingsConfigDict(
        env_prefix="QA_ENV_", env_file=".env", frozen=True, extra="ignore"
    )

    url: str = ""
