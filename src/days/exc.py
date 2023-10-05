class NotStartedError(Exception):
    ...


class WorkingOnItError(Exception):
    ...


def WORKING_ON_IT(name):
    raise WorkingOnItError(f"{name} Solution under construction!")


def NOT_STARTED(name):
    raise NotStartedError(f"{name} Not implemented yet!")
