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
    ONESTAR = 1
    TWOSTAR = 2
    THREESTAR = 3
    FOURSTAR = 4
    FIVESTAR = 5


@unique
class DoorsLoops(Enum):
    TEST = 'TEST'

@unique
class OrderStatus(Enum):
    TEST = 'TEST'
    PAIDFOR = 'PAIDFOR'
    DECORATION = 'DECORATION'
    INPROGRESS = 'INPROGRESS'
    DONE = 'DONE'

@unique
class OrderComplexity(Enum):
    JUNIOR = 'JUNIOR'
    MIDDLE = 'MIDDLE'
    SENIOR = 'SENIOR'

