# from pydantic import BaseModel, SecretStr
# from dotenv import load_dotenv
# class Settings(BaseModel):
#     bot_token : SecretStr
    
    
#     class Config:
#         env_file = '.env'
#         env_file_encoding = 'utf-8'

# load_dotenv()
# config = Settings()

# bot_token = config.bot_token.get_secret_value()