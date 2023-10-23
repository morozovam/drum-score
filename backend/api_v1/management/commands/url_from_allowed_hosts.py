def url_from_allowed_hosts(ALLOWED_HOSTS):
    urls = []
    for i in ALLOWED_HOSTS:
        urls.append(f"http://{i}")
        urls.append(f"https://{i}")
    return urls