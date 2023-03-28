from environs import Env

env = Env()
env.read_env()

DEBUG= env.bool("DEBUG")
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")
SECRET_KEY = env.list("SECRET_KEY")
