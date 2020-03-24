import random
import string

class Robot(object):
    list_names = []

    def __init__(self):
        self.reset()

    def reset(self):
        self.name = self.generate_name()
        while self.name in self.list_names:
            self.name = self.generate_name()
        self.list_names.append(self.name)

    @staticmethod
    def generate_name():
        name = ''.join(random.choices(string.ascii_uppercase, k=2))
        name += ''.join(random.choices(string.digits, k=3))
        return name
