import abc


class Tributavel(abc.ABC):
    @abc.abstractmethod
    def valor_imposto(self):
        pass
