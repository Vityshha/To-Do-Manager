from enum import Enum, unique


@unique
class LevelWorker(Enum):
    JUNIOR = 'JUNIOR'
    MIDDLE = 'MIDDLE'
    SENIOR = 'SENIOR'

@unique
class RoleUser(Enum):
    ADMIN = 'ADMIN'
    WORKER = 'WORKER'
    CLIENT = 'CLIENT'
    MANAGER = 'MANAGER'

@unique
class RatingOrder(Enum):
    TEST = 'TEST'

@unique
class DoorsLoops(Enum):
    TEST = 'TEST'

@unique
class OrderStatus(Enum):
    TEST = 'TEST'

@unique
class OrderComplexity(Enum):
    JUNIOR = 'JUNIOR'
    MIDDLE = 'MIDDLE'
    SENIOR = 'SENIOR'

