def remote_control():
        yield "CNN"
        yield "ESPN"
        yield "BBC"

remote=remote_control()
print(next(remote))
print(next(remote))
print(next(remote))