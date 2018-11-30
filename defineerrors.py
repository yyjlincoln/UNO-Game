class RoomDoesnotExistError(Exception):
    # Room does not exist
    pass

class RoomAlreadyExistError(Exception):
    # Room already exists
    pass

class PlayerDoesnotExistError(Exception):
    # Player does not exist
    pass

class PlayerAlreadyExistError(Exception):
    # Room already exists
    pass

class CardDefineError(Exception):
    # CardDefinerror
    pass

class CardInUseError(Exception):
    # This card is already in use.
    pass