class Validator():

    def validateString(self, string):
        return isinstance(string, str)

    def validateStringLength(self, string, length):
        if not(self.validateString(string)):
            return False

        return len(string) <= length

    def validateBool(self, value):
        return isinstance(value, bool)
