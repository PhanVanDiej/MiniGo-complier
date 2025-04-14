import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):

    def test_lower_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",101))
    def test_wrong_token(self):
        self.assertTrue(TestLexer.checkLexeme("ab?sVN","ab,ErrorToken ?",102))
    def test_keyword_var(self):
        """test keyword var"""
        self.assertTrue(TestLexer.checkLexeme("var abc int ;","var,abc,int,;,<EOF>",103))
    def test_keyword_func(self):
        """test keyword func"""
        self.assertTrue(TestLexer.checkLexeme("""func abc ( ) ""","""func,abc,(,),<EOF>""",104))
    def test_string_literal(self):
        """test string literal"""
        self.assertTrue(TestLexer.checkLexeme('"Hello World"', '"Hello World",<EOF>', 105))

    def test_unclosed_string(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.checkLexeme('"Hello', 'UncloseString: "Hello', 106))

    def test_illegal_escape(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.checkLexeme(
        '"Hello\\mWorld"', 
        'Illegal escape in string: Hello\\mWorld', 
        107))

    def test_number_literals(self):
        """test number literals"""
        self.assertTrue(TestLexer.checkLexeme('123 0x1A 0b101', '123,0x1A,0b101,<EOF>', 108))