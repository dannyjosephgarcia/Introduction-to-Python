class DummyClass2:
    def __init__(self, integer):
        self.integer = integer

    def return_integer(self):
        return self.integer


if __name__ == "__main__":
    dummy = DummyClass2(3)
    print(dummy.return_integer())