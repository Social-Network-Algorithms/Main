from typing import List, Dict
from src.dao.global_word_frequency.setter.global_word_frequency_setter import GlobalWordFrequencySetter

class MongoGlobalWordFrequencySetter(GlobalWordFrequencySetter):
    def __init__(self):
        self.user_word_frequency_collection = None

    def set_global_word_frequency_collection(self, global_word_frequency_collection: str) -> None:
        self.global_word_frequency_collection = global_word_frequency_collection

    def store_global_word_frequency_vector(self, global_word_freq_vc: Dict):
        doc = {"global_word_frequency_vector": global_word_freq_vc}
        self.user_word_frequency_collection.replace(doc)

