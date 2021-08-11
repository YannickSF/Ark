
from core.ark import Ark
from core.ark_index import ArkIndex
from core.objects import Column
from core.nosql import Query


if __name__ == '__main__':
    db = Ark()
    db.__add__('self')
    index = ArkIndex()
