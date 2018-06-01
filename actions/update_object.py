from lib.action import InfobloxBaseAction

__all__ = [
    'UpdateObjectAction',
]

class CreateObjectAction(InfobloxBaseAction):
    def run(self, ref, **kwargs):
        result = self.connection.update_object(ref=ref, kwargs)
        return result
