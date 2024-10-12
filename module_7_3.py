class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file in self.file_names:
            with open(file, encoding='utf-8') as f:
                text = f.read()
                text = text.lower()
                for i in ',.=!?:;-':
                    text = text.replace(i, '')
                words = text.split()
                all_words[file] = words
        return all_words

    def find(self, word):
        result = {}
        for name, words in self.get_all_words().items():
            result[name] = words.index(word.lower()) + 1
        return result

    def count(self, word):
        result = {}
        for name, words in self.get_all_words().items():
            result[name] = words.count(word.lower())
        return result


finder2 = WordsFinder('test.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
