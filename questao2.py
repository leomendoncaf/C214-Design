from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, data):
        pass


class WordCounter:
    def __init__(self):
        self.observers = []
    
    def attach(self, observer):
        self.observers.append(observer)
    
    def detach(self, observer):
        self.observers.remove(observer)
    
    def notify(self, data):
        for observer in self.observers:
            observer.update(data)
    

class WordCountObserver(Observer):
    def __init__(self):
        self.total_count = 0
        self.even_count = 0
        self.uppercase_count = 0
    
    def update(self, data):
        words = data.split()
        self.total_count = len(words)
        self.even_count = sum(len(word) % 2 == 0 for word in words)
        self.uppercase_count = sum(word[0].isupper() for word in words)


def main():
    phrase = input("Digite uma frase: ")

    word_counter = WordCounter()
    word_count_observer = WordCountObserver()
    word_counter.attach(word_count_observer)
    
    word_counter.notify(phrase)
    
    print("Total de palavras:", word_count_observer.total_count)
    print("Palavras com quantidade par de caracteres:", word_count_observer.even_count)
    print("Palavras começadas com maiúsculas:", word_count_observer.uppercase_count)


if __name__ == '__main__':
    main()
