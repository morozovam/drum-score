import environ

env = environ.Env()
env.prefix = "DRUMSCORE_"


def get_url_from_allowed_hosts():
    ALLOWED_HOSTS = env.tuple("ALLOWED_HOSTS", default=["0.0.0.0"])
    urls = []
    for i in ALLOWED_HOSTS:
        urls.append(f"http://{i}")
        urls.append(f"https://{i}")
    return urls
