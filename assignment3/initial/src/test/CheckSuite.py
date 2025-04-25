from typing import final
from unittest import TestCase
from TestUtils import TestChecker
from AST import (
    ArrayLiteral,
    ArrayType,
    Assign,
    BinaryOp,
    Block,
    ConstDecl,
    FloatLiteral,
    FloatType,
    FuncCall,
    FuncDecl,
    Id,
    IntLiteral,
    IntType,
    ParamDecl,
    Program,
    Return,
    StringLiteral,
    StringType,
    VarDecl,
    VoidType,
)


@final
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
        input_ast = Program([VarDecl("a", StringType(), StringLiteral("22"))])
        expect = ""
        self.assertTrue(TestChecker.test(input_ast, expect, 405))

    def test_assign_array_float_literial(self):
        input_ast = Program(
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
        self.assertTrue(TestChecker.test(input_ast, expect, 406))

    def test_const_decl_type_mismatch(self):
        input_ast = Program([ConstDecl("x", IntType(), FloatLiteral(3.14))])
        expect = "Type Mismatch: ConstDecl(x,IntType,FloatLiteral(3.14))\n"
        self.assertTrue(TestChecker.test(input_ast, expect, 407))

    def test_const_decl_correct(self):
        input_ast = Program([ConstDecl("x", FloatType(), FloatLiteral(3.14))])
        expect = ""
        self.assertTrue(TestChecker.test(input_ast, expect, 408))

    def test_assign_type_mismatch(self):
        input_ast = Program(
            [
                VarDecl("a", IntType(), IntLiteral(5)),
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block([Assign(Id("a"), FloatLiteral(2.5))]),
                ),
            ]
        )
        expect = "Type Mismatch: Assign(Id(a),FloatLiteral(2.5))\n"
        self.assertTrue(TestChecker.test(input_ast, expect, 409))

    def test_assign_correct(self):
        input_ast = Program(
            [
                VarDecl("a", IntType(), IntLiteral(1)),
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block(
                        [
                            Assign(Id("a"), IntLiteral(10)),
                            Assign(Id("a"), IntLiteral(20)),
                        ]
                    ),
                ),
            ]
        )
        expect = ""
        self.assertTrue(TestChecker.test(input_ast, expect, 410))

    def test_assign_to_const_should_fail(self):
        input_ast = Program(
            [
                ConstDecl("a", IntType(), IntLiteral(1)),
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block([Assign(Id("a"), IntLiteral(5))]),
                ),
            ]
        )
        expect = "Cannot Assign To Constant: a\n"
        self.assertTrue(TestChecker.test(input_ast, expect, 411))

    def test_func_call_type_mismatch(self):
        input_ast = Program(
            [
                FuncDecl("foo", [], VoidType(), Block([])),
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block([FuncCall("foo", [IntLiteral(1)])]),
                ),
            ]
        )
        expect = "Type Mismatch: FuncCall(foo,[IntLiteral(1)])\n"
        self.assertTrue(TestChecker.test(input_ast, expect, 412))

    def test_built_in_func_call_correct(self):
        input_ast = Program(
            [
                VarDecl("a", IntType(), IntLiteral(42)),
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block([FuncCall("putInt", [Id("a")])]),
                ),
            ]
        )
        expect = ""
        self.assertTrue(TestChecker.test(input_ast, expect, 413))

    def test_func_call_user_defined_with_body(self):
        input_ast = Program(
            [
                FuncDecl(
                    "add",
                    [ParamDecl("a", IntType()), ParamDecl("b", IntType())],
                    IntType(),
                    Block(
                        [
                            VarDecl(
                                "result", IntType(), BinaryOp("+", Id("a"), Id("b"))
                            ),
                            Return(Id("result")),
                        ]
                    ),
                ),
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block(
                        [
                            VarDecl("x", IntType(), IntLiteral(10)),
                            VarDecl("y", IntType(), IntLiteral(20)),
                            VarDecl(
                                "z", IntType(), FuncCall("add", [Id("x"), Id("y")])
                            ),
                            FuncCall("putInt", [Id("z")]),
                        ]
                    ),
                ),
            ]
        )
        expect = ""
        self.assertTrue(TestChecker.test(input_ast, expect, 414))

    def test_return_void_with_value(self):
        input_ast = Program(
            [
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block([Return(IntLiteral(5))]),
                )
            ]
        )
        expect = "Type Mismatch: Return(IntLiteral(5))\n"
        self.assertTrue(TestChecker.test(input_ast, expect, 415))

    def test_return_correct(self):
        input_ast = Program(
            [FuncDecl("foo", [], FloatType(), Block([Return(IntLiteral(10))]))]
        )
        expect = ""
        self.assertTrue(TestChecker.test(input_ast, expect, 416))
