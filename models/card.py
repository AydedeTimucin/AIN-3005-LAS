from models.user import User

class Card:
    def __init__(self, pin_code: str, owner: User):
        self.pin_code = pin_code
        self.owner = owner

    def verify_pin(self, input_pin: str) -> bool:
        return self.pin_code == input_pin