#phrase = input("Set a phrase: ")
#count = len(phrase)
#print(f"Введено {count} символов")

class TestSetPhrase:
    max_count = 15

    def test_check_phrase(self):
        phrase = input("Set a phrase: ")
        max_count = 15
        input_count = len(phrase)
        assert input_count < max_count, f"Фраза более 15 символов. Введено {input_count} символов"