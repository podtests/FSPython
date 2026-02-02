from abc import ABC, abstractmethod

class Car(ABC):

    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def engineSetting(self):
        pass

class BMW(Car):

    def engineSetting(self):
        print('BMW Engine is Set!')

    def playMusic(self):
        print('BMW playing music')


b1 = BMW()
b1.playMusic()