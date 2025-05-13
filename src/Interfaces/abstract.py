from abc import ABCMeta, abstractmethod


class MyAbstract(metaclass=ABCMeta):
    pass

class PaymentMethod(MyAbstract):
      @abstractmethod
      def pay(self):
          pass