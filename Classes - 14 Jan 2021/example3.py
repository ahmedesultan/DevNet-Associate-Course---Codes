from example2 import Router


class Switch(Router):
    def __init__(self, name, model, swversion, ip_add):
        super().__init__(model, swversion, ip_add)
        self.name = name
