from hangman import *
import unittest


class TestHangman(unittest.TestCase):
    def setUp(self) -> None:
        self.word_bank = Bank()

    def test_pick_topic(self):
        self.assertIn(self.word_bank.pick_topic(), Bank.topic_names)
    
    def test_get_word_from_api(self):
        self.assertTrue(self.word_bank.get_word())

    def test_word_len(self):
        self.word_bank.pick_topic()
        self.assertEqual(self.word_bank.pick_word(),f'Word is {len(self.word_bank.current_word)} letters long.')
    

    def test_not_solve_True(self):
        self.word_bank.pick_topic()
        self.word_bank.pick_word()
        self.word_bank.letters_guessed_counter = 0
        self.word_bank.check_solve()
        self.assertTrue(self.word_bank.not_solved)
    
    def test_guess(self):
        self.bank = Bank()
        self.bank.current_word = 'fish'
        self.player1 = Player(self.word_bank)
        print("enter a guess for your test")
        self.assertEqual(self.player1.guess(), self.player1.answer)
    
    def test_validate_user_input(self):
        self.bank = Bank()
        self.bank.current_word = 'fish'
        self.player1 = Player(self.word_bank)
        self.game = Processes()
        for answ in "abcdefghijklmnopqrstuwxyz":
            self.player1.answer = answ
            self.assertTrue(self.game.validate_user_input(self.player1))
    
    def test_check_answer_update_lives(self):
        self.bank = Bank()
        self.bank.current_word = 'red'
        self.player1 = Player(self.word_bank)
        self.game = Processes()

        for i in self.bank.current_word:
            self.bank.current_word_display.append('_')

        #check if repeated answers return error
        self.player1.answer = "e"
        self.game.check_answer_update_lives(self.bank, self.player1)
        self.player1.answer = "e"
        self.assertEqual(self.game.check_answer_update_lives(self.bank, self.player1), '\nLetter already guessed.')

        #check the lives with wrong answers
        self.bank.current_word = 'fish'
        self.player1.lives = 4        
        self.player1.answer = 'o'
        self.game.check_answer_update_lives(self.bank, self.player1)
        self.assertEqual(self.player1.lives, 3)





        






        



if __name__ == '__main__':
    unittest.main()
