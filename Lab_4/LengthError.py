class LengthError(Exception):
    def __int__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f"Invalid length: {self.message}"
        else:
            return "Invalid length"
