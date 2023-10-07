class NotStartedError(Exception):
    ...


class WorkingOnItError(Exception):
    ...


def WORKING_ON_IT(name):
    raise WorkingOnItError(f"{name}")


def NOT_STARTED(name):
    raise NotStartedError(f"{name}")
