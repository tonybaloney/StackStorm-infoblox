from lib.action import InfobloxBaseAction

__all__ = [
    'GetObjectAction',
]

class GetObjectAction(InfobloxBaseAction):
    def run(self, object_type, fields, **kwargs):
        result = self.connection.get_object(
            object_type,
            return_fields=fields,
            payload=kwargs)
        return result
