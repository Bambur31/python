from abc import ABC, abstractmethod


class Clother(ABC):

    @abstractmethod
    def coat(self, size):
        pass

    @abstractmethod
    def suit(self, len_ght):
        pass


class Coat(Clother):
    def coat(self, size):
        v_1 = (size / 6.5) + 0.5
        return float(v_1)

    def suit(self, len_ght):
        pass


class Suit(Clother):
    def suit(self, h):
        v_2 = (h * 2) + 0.5
        return float(v_2)

    def coat(self, size):
        pass


n_1 = Coat()
s_1 = n_1.coat(80)
print(f"Расход ткани на пальто: {s_1}")
n_2 = Suit()
s_2 = n_2.suit(1.8)
print(f"Расход ткани на костюм: {s_2}")
print(f"Суммарный расход: {s_1 + s_2}")
