from pydantic_settings import BaseSettings


class Setting(BaseSettings):
    database_url: str


# BaseSettingsは大文字、小文字の区別なく一致する環境変数をみに行く
setting = Setting()
print(setting.database_url)
