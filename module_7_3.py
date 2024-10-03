import io
from pprint import pprint
class WordsFinder:
    def __init__(self,*file_names):
        self.file_names = file_names
    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                string = []
                for file_txt in file:
                    file_txt = file_txt.lower()
                    delet = [',', '.', '=', '!', '?', ';', ':', ' - ']
                    for punct in delet:
                        file_txt = file_txt.replace(punct,' ')
                    string.extend(file_txt.split())
                all_words[file_name] = string
            return all_words
    def find(self, word):
        dictionary_1 = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                dictionary_1[name] = words.index(word.lower()) + 1
        return dictionary_1
    def count(self, word):
        dictionary_2 = {}
        for name, words in self.get_all_words().items():
            numbers = words.count(word.lower())
            dictionary_2[name] = numbers
        return dictionary_2
#finder2 = WordsFinder('test_file.txt')
#print(finder2.get_all_words())  # Все слова
#print(finder2.find('TEXT'))  # 3 слово по счёту
#print(finder2.count('teXT'))  # 4 слова teXT в тексте всего

finder1 = WordsFinder('Mother Goose - Monday’s Child.txt',)
print(finder1.get_all_words())
print(finder1.find('Child'))
print(finder1.count('Child'))