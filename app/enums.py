from enum import Enum, unique


@unique
class RoleUser(Enum):
    OWNER = 'OWNER'
    EDITOR = 'EDITOR'
    VIEWER = 'VIEWER'

@unique
class TasksStatus(Enum):
    ACTIVE = 'ACTIVE'
    COMPLETED = 'COMPLETED'
    ARCHIVED = 'ARCHIVED'

