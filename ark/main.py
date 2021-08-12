
from ark.core.ark import Ark
from ark.core.ark_index import ArkIndex

if __name__ == '__main__':
    db = Ark()
    db.__add__('self')
    index = ArkIndex()
