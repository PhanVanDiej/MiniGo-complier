from unittest import TestCase
from TestUtils import TestChecker
from AST import (
    ArrayLiteral,
    ArrayType,
    Id,
    IntLiteral,
    IntType,
    Program,
    StringLiteral,
    StringType,
    VarDecl,
)


class CheckSuite(TestCase):
    def test_redeclared(self):
        input = """var a int; var b int; var a int; """
        expect = "Redeclared Variable: a\n"
        self.assertTrue(TestChecker.test(input, expect, 400))

    def test_type_mismatch(self):
        input = """var a int = 1.2;"""
        expect = "Type Mismatch: VarDecl(a,IntType,FloatLiteral(1.2))\n"
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test_undeclared_identifier(self):
        input = Program([VarDecl("a", IntType(), Id("b"))])
        expect = "Undeclared Identifier: b\n"
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test_assign_wrong_type(self):
        input = """var a int = 5; var b int = 5.2;"""
        expect = "Type Mismatch: VarDecl(b,IntType,FloatLiteral(5.2))\n"
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_assign_int_type_to_floating_type(self):
        input = """var a = 5; var b float = 5;"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test_assign_string_literial(self):
        input = Program([VarDecl("a", StringType(), StringLiteral("22"))])
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_assign_array_float_literial(self):
        input = Program(
            [
                VarDecl(
                    "a",
                    ArrayType([IntLiteral(3)], IntType()),
                    ArrayLiteral(
                        [IntLiteral(3)],
                        IntType(),
                        [IntLiteral(1), IntLiteral(2), IntLiteral(3)],
                    ),
                )
            ]
        )

        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 406))
