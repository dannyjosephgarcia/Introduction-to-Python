from EndOfLessonFiles.dummy_class_2 import DummyClass2


class DummyClass1:
    def __init__(self, dummy_class_2):
        self.dummy_class_2 = dummy_class_2

    def add_two_numbers(self, integer):
        return integer + self.dummy_class_2.return_integer()


if __name__ == "__main__":
    dummy_class_2 = DummyClass2(3)
    dummy_class_1 = DummyClass1(dummy_class_2=dummy_class_2)
    print(dummy_class_1.add_two_numbers(2))

