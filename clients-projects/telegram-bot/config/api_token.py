from environs import Env

env = Env()
env.read_env()


BOT_TOKEN: str = env.str("API_TOKEN")
