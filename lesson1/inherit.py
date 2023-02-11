from abc import abstractmethod


class Vehicle:
    color = 'red'
    doors_count = 5

    def start_engine(self):
        pass

    def accelerate(self):
        pass

    # def accelerate(self, param1: str):
    #     pass
    #
    # def accelerate(self, param1: int):
    #     pass

    def break_(self):
        pass

    def turn(self, angle):
        pass


class DieselCar(Vehicle):
    def start_engine(self):
        pass  # start with starter pedal


class ElectroCar(Vehicle):
    acc_type = 'LiIon'

    def start_engine(self):
        pass

    def accelerate(self):
        pass


class HybridCar(ElectroCar):
    pass


class MusicPlayer:
    pass


class MobilePhone:
    pass


class SmartPhone(MusicPlayer, MobilePhone):
    pass


class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C, Vehicle, ElectroCar):
    pass


class AbstractConnector:
    def connect(self):
        raise NotImplementedError

    def send_request(self):
        raise NotImplementedError

    def process_request(self):
        raise NotImplementedError

    def close_connection(self):
        raise NotImplementedError


class CosmosDBConnector(AbstractConnector):
    pass


if __name__ == '__main__':
    d = D()
    # d.some_method()
