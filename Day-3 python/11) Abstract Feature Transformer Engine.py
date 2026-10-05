from abc import ABC, abstractmethod
class BaseDataTransformer(ABC):
    @abstractmethod
    def transform(self, data):
        pass
class NormalizerTransformer(BaseDataTransformer):
    def transform(self, data):
        maximum = max(data)
        return [round(x / maximum, 2) for x in data]
class StandardizerTransformer(BaseDataTransformer):
    def transform(self, data):
        mean = sum(data) / len(data)
        variance = sum((x - mean) ** 2 for x in data) / len(data)
        std = variance ** 0.5
        return [round((x - mean) / std, 2) for x in data]
normal = NormalizerTransformer()
standard = StandardizerTransformer()
print("Normalized :", normal.transform([10, 20, 50, 100]))
print("Standardized:", standard.transform([10, 20, 30, 40, 50]))