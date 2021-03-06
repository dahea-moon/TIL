# 파일명을 변경하지 마시오.
# 아래에 Word 클래스를 작성하시오.


class Word:
    def __init__(self):
        self.wordbook = {}

    def add(self, eng, ko):
        self.wordbook[eng] = ko

    def delete(self, eng):
        try:
            self.wordbook.pop(eng)
            return True
        except KeyError:
            return False

    def print(self):
        for eng, ko in self.wordbook.items():
            print(f'{eng}: {ko}')


# 실행 결과를 확인하기 위한 코드입니다. 수정하지 마시오.
if __name__ == '__main__':
    my_book = Word()
    my_book.add('grape', '포도')
    my_book.add('peach', '복숭아')
    my_book.add('watermelon', '수박')
    my_book.add('mango', '망고')
    my_book.print()
    print(my_book.delete('watermelon'))
    print(my_book.delete('mango'))
    print(my_book.delete('carrot'))
    my_book.print()
