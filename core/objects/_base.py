
class BaseObject:

    def to_dict(self):
        return {
            key: getattr(self, key)
            for key in self.__dataclass_fields__
        }
