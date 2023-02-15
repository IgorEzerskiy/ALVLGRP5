from datetime import datetime

SMALL_SENTENCE_VALUE = '1231233u13akjhs'


class A:
    def __init__(self, sentence):
        self.sentence = sentence

    def __del__(self):
        print(f"{self} destructed at {datetime.now()}")



    def return_string_reversed(self, some_str):
        return ''.join(reversed(some_str + self.__class__.__name__))

    def make_longer(self):
        self.sentence += 'abc'


class C(A):
    """не треба так"""

    # def __init__(self, sentence):
    #     super().__init__(sentence)

    def make_longer(self):
        super().make_longer()
        self.sentence += 'd'


class Alphabet:
    pass


class B(A):
    def __init__(self, sentence, alphabet_obj):
        if len(sentence) > 15:
            raise ValueError('Sentences with 15+ characters are not allowed')
        super().__init__(sentence)
        self.alphabet_obj = alphabet_obj

    def return_string_reversed(self, some_str):
        return super().return_string_reversed(some_str).upper()

    def some_action_with_other_object(self, some_obj):
        if self.sentence == some_obj.some_property:
            pass


def some_func(param1, *args, **kwargs):
    if hasattr(some_func, 'called') and some_func.called:
        return
    print(args)
    print(kwargs)
    some_func.called = True


if __name__ == '__main__':
    alp = Alphabet()
    b = B('', alp)
    some_func(1, some_str='qwe', some_list=[1, 2, 3, 45])
    some_func('weqeqw', 1, 3)
    c = C('some_sentence')
    c.make_longer()
    print(c.sentence)

    b.make_longer()
    print(b.sentence)

    b.prop1 = 1
    print(b.prop1)
