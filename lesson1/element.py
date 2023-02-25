class Element:
    def __int__(self):
        pass

    def agg_state(self, temp, scale='C'):
        pass

    @staticmethod
    def convert_to_c(temp, scale='C'):
        return temp


if __name__ == '__main__':
    el = Element()
    el.convert_to_c(12)
    Element.convert_to_c(12)
