from typing import cast, final
from unittest import TestCase
from TestUtils import TestChecker
from AST import (
    ArrayCell,
    ArrayLiteral,
    ArrayType,
    Assign,
    BinaryOp,
    Block,
    BlockMember,
    BoolType,
    BooleanLiteral,
    Break,
    ConstDecl,
    Continue,
    Decl,
    FieldAccess,
    FloatLiteral,
    FloatType,
    ForBasic,
    ForEach,
    ForStep,
    FuncCall,
    FuncDecl,
    Id,
    If,
    IntLiteral,
    IntType,
    MethCall,
    MethodDecl,
    ParamDecl,
    Program,
    Return,
    StringLiteral,
    StringType,
    StructType,
    UnaryOp,
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

    def test_if_with_boolean_condition(self):
        input_ast = Program(
            [
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block(
                        [If(BooleanLiteral(True), Block([]), None)],
                    ),
                )
            ]
        )
        expect = ""
        self.assertTrue(TestChecker.test(input_ast, expect, 417))

    def test_if_with_non_boolean_condition(self):
        input_ast = Program(
            [
                FuncDecl(
                    "main", [], VoidType(), Block([If(IntLiteral(1), Block([]), None)])
                )
            ]
        )
        expect = "Type Mismatch: If(IntLiteral(1),Block([]))\n"
        self.assertTrue(TestChecker.test(input_ast, expect, 418))

    def test_for_basic_with_int_condition(self):
        input_ast = Program(
            [
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block([ForBasic(IntLiteral(1), Block([]))]),
                )
            ]
        )
        expect = "Type Mismatch: For(IntLiteral(1),Block([]))\n"
        self.assertTrue(TestChecker.test(input_ast, expect, 419))

    def test_for_basic_success(self):
        input_ast = Program(
            [
                VarDecl("i", IntType(), IntLiteral(0)),
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block(
                        [
                            ForBasic(
                                BinaryOp("<", Id("i"), IntLiteral(10)),
                                Block(
                                    [
                                        Assign(
                                            Id("i"),
                                            BinaryOp("+", Id("i"), IntLiteral(1)),
                                        )
                                    ]
                                ),
                            )
                        ]
                    ),
                ),
            ]
        )
        expect = ""
        self.assertTrue(TestChecker.test(input_ast, expect, 420))

    def test_for_step_success(self):
        input_ast = Program(
            [
                VarDecl("i", IntType(), IntLiteral(0)),
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block(
                        [
                            ForStep(
                                Assign(Id("i"), IntLiteral(0)),
                                BinaryOp("<", Id("i"), IntLiteral(5)),
                                Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))),
                                Block([FuncCall("putIntLn", [Id("i")])]),
                            )
                        ]
                    ),
                ),
            ]
        )
        expect = ""
        self.assertTrue(TestChecker.test(input_ast, expect, 421))

    def test_for_step_type_mismatch_in_condition(self):
        input_ast = Program(
            [
                VarDecl("i", IntType(), IntLiteral(0)),
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block(
                        [
                            ForStep(
                                Assign(Id("i"), IntLiteral(0)),
                                IntLiteral(123),
                                Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))),
                                Block([]),
                            )
                        ]
                    ),
                ),
            ]
        )
        expect = "Type Mismatch: For(Assign(Id(i),IntLiteral(0)),IntLiteral(123),Assign(Id(i),BinaryOp(Id(i),+,IntLiteral(1))),Block([]))\n"
        self.assertTrue(TestChecker.test(input_ast, expect, 422))

    def test_foreach_success(self):
        input_ast = Program(
            [
                VarDecl(
                    "arr",
                    ArrayType([IntLiteral(3)], IntType()),
                    ArrayLiteral(
                        [IntLiteral(3)],
                        IntType(),
                        [IntLiteral(1), IntLiteral(2), IntLiteral(3)],
                    ),
                ),
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block(
                        [
                            ForEach(
                                Id("i"),
                                Id("val"),
                                Id("arr"),
                                Block([FuncCall("putIntLn", [Id("val")])]),
                            )
                        ]
                    ),
                ),
            ]
        )
        expect = ""
        self.assertTrue(TestChecker.test(input_ast, expect, 423))

    def test_foreach_type_mismatch_non_array(self):
        input_ast = Program(
            [
                VarDecl("notArr", IntType(), IntLiteral(10)),
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block(
                        [
                            ForEach(
                                Id("i"),
                                Id("v"),
                                Id("notArr"),
                                Block([FuncCall("putIntLn", [Id("v")])]),
                            )
                        ]
                    ),
                ),
            ]
        )
        expect = "Type Mismatch: ForEach(Id(i),Id(v),Id(notArr),Block([FuncCall(putIntLn,[Id(v)])]))\n"
        self.assertTrue(TestChecker.test(input_ast, expect, 424))

    def test_break_continue_in_loop(self):
        input_ast = Program(
            [
                VarDecl("i", IntType(), IntLiteral(0)),
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block(
                        [
                            ForBasic(
                                BinaryOp("<", Id("i"), IntLiteral(10)),
                                Block([Continue(), Break()]),
                            )
                        ]
                    ),
                ),
            ]
        )
        expect = ""
        self.assertTrue(TestChecker.test(input_ast, expect, 425))

    def test_unary_op_success(self):
        input_ast = Program(
            [
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block(
                        [
                            VarDecl("a", IntType(), IntLiteral(5)),
                            VarDecl("b", FloatType(), UnaryOp("-", FloatLiteral(3.14))),
                            VarDecl(
                                "c", BoolType(), UnaryOp("!", BooleanLiteral(True))
                            ),
                        ]
                    ),
                )
            ]
        )
        expect = ""
        self.assertTrue(TestChecker.test(input_ast, expect, 426))

    def test_unary_op_type_mismatch(self):
        input_ast = Program(
            [
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block(
                        [
                            VarDecl("s", StringType(), StringLiteral("abc")),
                            VarDecl("x", IntType(), UnaryOp("-", Id("s"))),
                        ]
                    ),
                )
            ]
        )
        expect = "Type Mismatch: UnaryOp(-,Id(s))\n"
        self.assertTrue(TestChecker.test(input_ast, expect, 427))

    def test_method_call_success(self):
        input_ast = Program(
            [
                VarDecl(
                    "c",
                    StructType(
                        "Counter",
                        [],
                        [
                            MethodDecl(
                                "self",
                                StructType("Counter", [], []),
                                FuncDecl("reset", [], VoidType(), Block([])),
                            )
                        ],
                    ),
                    None,
                ),
                FuncDecl(
                    "main", [], VoidType(), Block([MethCall(Id("c"), "reset", [])])
                ),
            ],
        )
        expect = ""
        self.assertTrue(TestChecker.test(input_ast, expect, 428))

    def test_arraycell_valid_access(self):
        input_ast = Program(
            [
                VarDecl(
                    "a",
                    ArrayType([IntLiteral(2), IntLiteral(3)], IntType()),
                    ArrayLiteral(
                        [IntLiteral(2), IntLiteral(3)],
                        IntType(),
                        [
                            [IntLiteral(1), IntLiteral(2), IntLiteral(3)],
                            [IntLiteral(4), IntLiteral(5), IntLiteral(6)],
                        ],
                    ),
                ),
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block(
                        [
                            VarDecl(
                                "x",
                                IntType(),
                                ArrayCell(Id("a"), [IntLiteral(1), IntLiteral(2)]),
                            )
                        ]
                    ),
                ),
            ]
        )
        expect = ""
        self.assertTrue(TestChecker.test(input_ast, expect, 429))

    def test_arraycell_too_many_indices(self):
        input_ast = Program(
            [
                VarDecl(
                    "a",
                    ArrayType([IntLiteral(2)], IntType()),
                    ArrayLiteral(
                        [IntLiteral(2)], IntType(), [IntLiteral(1), IntLiteral(2)]
                    ),
                ),
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block(
                        [
                            VarDecl(
                                "x",
                                IntType(),
                                ArrayCell(Id("a"), [IntLiteral(0), IntLiteral(1)]),
                            )
                        ]
                    ),
                ),
            ]
        )
        expect = "Type Mismatch: ArrayCell(Id(a),[IntLiteral(0),IntLiteral(1)])\n"
        self.assertTrue(TestChecker.test(input_ast, expect, 430))

    def test_arraycell_index_not_int(self):
        input_ast = Program(
            [
                VarDecl(
                    "a",
                    ArrayType([IntLiteral(2)], IntType()),
                    ArrayLiteral(
                        [IntLiteral(2)], IntType(), [IntLiteral(1), IntLiteral(2)]
                    ),
                ),
                VarDecl("s", StringType(), StringLiteral("abc")),
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block([VarDecl("x", IntType(), ArrayCell(Id("a"), [Id("s")]))]),
                ),
            ]
        )
        expect = "Type Mismatch: ArrayCell(Id(a),[Id(s)])\n"
        self.assertTrue(TestChecker.test(input_ast, expect, 431))

    def test_field_access_success(self):
        input_ast = Program(
            [
                VarDecl(
                    "p",
                    StructType(
                        "Person", [("name", StringType()), ("age", IntType())], []
                    ),
                    None,
                ),
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block([VarDecl("n", StringType(), FieldAccess(Id("p"), "name"))]),
                ),
            ]
        )
        expect = ""
        self.assertTrue(TestChecker.test(input_ast, expect, 432))

    def test_field_access_invalid_field(self):
        input_ast = Program(
            [
                VarDecl(
                    "p",
                    StructType(
                        "Person", [("name", StringType()), ("age", IntType())], []
                    ),
                    None,
                ),
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block(
                        [VarDecl("addr", StringType(), FieldAccess(Id("p"), "address"))]
                    ),
                ),
            ]
        )
        expect = "Undeclared Field: address\n"
        self.assertTrue(TestChecker.test(input_ast, expect, 433))

    def test_field_access_assign_success(self):
        input_ast = Program(
            [
                VarDecl(
                    "p",
                    StructType(
                        "Person", [("name", StringType()), ("age", IntType())], []
                    ),
                    None,
                ),
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block([Assign(FieldAccess(Id("p"), "age"), IntLiteral(30))]),
                ),
            ]
        )
        expect = ""
        self.assertTrue(TestChecker.test(input_ast, expect, 434))

    def test_field_access_func_call(self):
        input_ast = Program(
            [
                VarDecl(
                    "p",
                    StructType(
                        "Person", [("name", StringType()), ("age", IntType())], []
                    ),
                    None,
                ),
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block([FuncCall("putIntLn", [FieldAccess(Id("p"), "age")])]),
                ),
            ]
        )
        expect = ""
        self.assertTrue(TestChecker.test(input_ast, expect, 435))

    def test_field_access_binary_op(self):
        input_ast = Program(
            [
                VarDecl(
                    "p",
                    StructType("Point", [("x", FloatType()), ("y", FloatType())], []),
                    None,
                ),
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block(
                        [
                            VarDecl(
                                "dist",
                                FloatType(),
                                BinaryOp(
                                    "+",
                                    FieldAccess(Id("p"), "x"),
                                    FieldAccess(Id("p"), "y"),
                                ),
                            )
                        ]
                    ),
                ),
            ]
        )
        expect = ""
        self.assertTrue(TestChecker.test(input_ast, expect, 436))
