class RoomDoesnotExistError(Exception):
    # Room does not exist
    pass

class CardDefineError(Exception):
    # CardDefinerror
    pass


class CardInUseError(Exception):
    # This card is already in use.
    pass