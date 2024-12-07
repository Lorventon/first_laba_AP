from abc import ABC, abstractmethod

filenamexml = "data.xml"
filenamejson = "data.json"


class Handler(ABC):
    @abstractmethod
    def save_to(self, data) -> None:
        pass

    @abstractmethod
    def load_from(self) -> dict:
        pass

    @abstractmethod
    def print_data(self, data):
        pass

    @abstractmethod
    def data_to_dict(self, data):
        pass
