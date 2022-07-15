import docker


def get_client():
    """Retrieve the docker client for this environment."""
    client = docker.from_env()
    bk = client.login(username='healthyrahul', password='Rahul@5893')
    print(bk)
    import pdb; pdb.set_trace()
    return client


print(get_client())
