import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    # Basic identifiers tests (101-110)
    
    def test_lowercase_identifier(self):
        """Test identifiers with lowercase letters"""
        self.assertTrue(TestLexer.checkLexeme("abc", "abc,<EOF>", 101))
    
    def test_uppercase_identifier(self):
        """Test identifiers with uppercase letters"""
        self.assertTrue(TestLexer.checkLexeme("ABC", "ABC,<EOF>", 102))
    
    def test_mixed_case_identifier(self):
        """Test identifiers with mixed case letters"""
        self.assertTrue(TestLexer.checkLexeme("aBcDeF", "aBcDeF,<EOF>", 103))
    
    def test_identifier_with_digit(self):
        """Test identifiers with digits"""
        self.assertTrue(TestLexer.checkLexeme("abc123", "abc123,<EOF>", 104))
    
    def test_identifier_with_underscore(self):
        """Test identifiers with underscore"""
        self.assertTrue(TestLexer.checkLexeme("_abc", "_abc,<EOF>", 105))
    
    def test_identifier_underscore_digit(self):
        """Test identifiers with underscore and digit"""
        self.assertTrue(TestLexer.checkLexeme("_abc123", "_abc123,<EOF>", 106))
    
    def test_multiple_identifiers(self):
        """Test multiple identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc def ghi", "abc,def,ghi,<EOF>", 107))
    
    def test_identifier_with_keyword(self):
        """Test identifier with keyword as substring"""
        self.assertTrue(TestLexer.checkLexeme("variable", "variable,<EOF>", 108))
    
    def test_identifier_starting_with_keyword(self):
        """Test identifier starting with keyword"""
        self.assertTrue(TestLexer.checkLexeme("ifelse", "ifelse,<EOF>", 109))
    
    def test_long_identifier(self):
        """Test long identifier"""
        self.assertTrue(TestLexer.checkLexeme("thisIsAVeryLongIdentifier", "thisIsAVeryLongIdentifier,<EOF>", 110))
    
    # Keywords tests (111-120)
    def test_keyword_var(self):
        """Test keyword var"""
        self.assertTrue(TestLexer.checkLexeme("var", "var,<EOF>", 111))
    
    def test_keyword_func(self):
        """Test keyword func"""
        self.assertTrue(TestLexer.checkLexeme("func", "func,<EOF>", 112))
    
    def test_keyword_if(self):
        """Test keyword if"""
        self.assertTrue(TestLexer.checkLexeme("if", "if,<EOF>", 113))
    
    def test_keyword_else(self):
        """Test keyword else"""
        self.assertTrue(TestLexer.checkLexeme("else", "else,<EOF>", 114))
    
    def test_keyword_for(self):
        """Test keyword for"""
        self.assertTrue(TestLexer.checkLexeme("for", "for,<EOF>", 115))
    
    def test_keyword_return(self):
        """Test keyword return"""
        self.assertTrue(TestLexer.checkLexeme("return", "return,<EOF>", 116))
    
    def test_keyword_break(self):
        """Test keyword break"""
        self.assertTrue(TestLexer.checkLexeme("break", "break,<EOF>", 117))
    
    def test_keyword_continue(self):
        """Test keyword continue"""
        self.assertTrue(TestLexer.checkLexeme("continue", "continue,<EOF>", 118))
    
    def test_keyword_int(self):
        """Test keyword int"""
        self.assertTrue(TestLexer.checkLexeme("int", "int,<EOF>", 119))
    
    def test_keyword_float(self):
        """Test keyword float"""
        self.assertTrue(TestLexer.checkLexeme("float", "float,<EOF>", 120))
    
    # Operators tests (121-135)
    def test_arithmetic_operators(self):
        """Test arithmetic operators"""
        self.assertTrue(TestLexer.checkLexeme("+ - * / %", "+,-,*,/,%,<EOF>", 121))
    
    def test_relational_operators(self):
        """Test relational operators"""
        self.assertTrue(TestLexer.checkLexeme("> < >= <= == !=", ">,<,>=,<=,==,!=,<EOF>", 122))
    
    def test_logical_operators(self):
        """Test logical operators"""
        self.assertTrue(TestLexer.checkLexeme("&& || !", "&&,||,!,<EOF>", 123))
    
    def test_assignment_operators(self):
        """Test assignment operators"""
        self.assertTrue(TestLexer.checkLexeme("= += -= *= /=", "=,+=,-=,*=,/=,<EOF>", 124))
    
    def test_increment_operator(self):
        """Test increment operator"""
        self.assertTrue(TestLexer.checkLexeme("++", "++,<EOF>", 125))
    
    def test_decrement_operator(self):
        """Test decrement operator"""
        self.assertTrue(TestLexer.checkLexeme("--", "--,<EOF>", 126))
    
    def test_plus_operator(self):
        """Test plus operator in context"""
        self.assertTrue(TestLexer.checkLexeme("a + b", "a,+,b,<EOF>", 127))
    
    def test_minus_operator(self):
        """Test minus operator in context"""
        self.assertTrue(TestLexer.checkLexeme("a - b", "a,-,b,<EOF>", 128))
    
    def test_multiply_operator(self):
        """Test multiply operator in context"""
        self.assertTrue(TestLexer.checkLexeme("a * b", "a,*,b,<EOF>", 129))
    
    def test_divide_operator(self):
        """Test divide operator in context"""
        self.assertTrue(TestLexer.checkLexeme("a / b", "a,/,b,<EOF>", 130))
    
    def test_modulo_operator(self):
        """Test modulo operator in context"""
        self.assertTrue(TestLexer.checkLexeme("a % b", "a,%,b,<EOF>", 131))
    
    def test_and_operator(self):
        """Test logical AND operator in context"""
        self.assertTrue(TestLexer.checkLexeme("a && b", "a,&&,b,<EOF>", 132))
    
    def test_or_operator(self):
        """Test logical OR operator in context"""
        self.assertTrue(TestLexer.checkLexeme("a || b", "a,||,b,<EOF>", 133))
    
    def test_not_operator(self):
        """Test logical NOT operator in context"""
        self.assertTrue(TestLexer.checkLexeme("!a", "!,a,<EOF>", 134))
    
    def test_compound_operators(self):
        """Test compound operators in complex expression"""
        self.assertTrue(TestLexer.checkLexeme("a += b -= c *= d /= e", "a,+=,b,-=,c,*=,d,/=,e,<EOF>", 135))
    
    # Separators tests (136-145)
    def test_parentheses(self):
        """Test parentheses"""
        self.assertTrue(TestLexer.checkLexeme("()", "(,),<EOF>", 136))
    
    def test_brackets(self):
        """Test brackets"""
        self.assertTrue(TestLexer.checkLexeme("[]", "[,],<EOF>", 137))
    
    def test_braces(self):
        """Test braces"""
        self.assertTrue(TestLexer.checkLexeme("{}", "{,},<EOF>", 138))
    
    def test_semicolon(self):
        """Test semicolon"""
        self.assertTrue(TestLexer.checkLexeme(";", ";,<EOF>", 139))
    
    def test_colon(self):
        """Test colon"""
        self.assertTrue(TestLexer.checkLexeme(":", ":,<EOF>", 140))
    
    def test_comma(self):
        """Test comma"""
        self.assertTrue(TestLexer.checkLexeme(",", ",,<EOF>", 141))
    
    def test_dot(self):
        """Test dot"""
        self.assertTrue(TestLexer.checkLexeme(".", ".,<EOF>", 142))
    
    def test_mixed_separators(self):
        """Test mixed separators"""
        self.assertTrue(TestLexer.checkLexeme("func(a, b);", "func,(,a,,,b,),;,<EOF>", 143))
    
    def test_nested_separators(self):
        """Test nested separators"""
        self.assertTrue(TestLexer.checkLexeme("{[()]}", "{,[,(,),],},<EOF>", 144))
    
    def test_separators_with_identifiers(self):
        """Test separators with identifiers"""
        self.assertTrue(TestLexer.checkLexeme("a[i].field", "a,[,i,],.,field,<EOF>", 145))
    
    # Literal tests (146-160)
    def test_integer_literal(self):
        """Test integer literal"""
        self.assertTrue(TestLexer.checkLexeme("123", "123,<EOF>", 146))
    
    def test_multiple_integer_literals(self):
        """Test multiple integer literals"""
        self.assertTrue(TestLexer.checkLexeme("123 456 789", "123,456,789,<EOF>", 147))
    
    def test_zero_literal(self):
        """Test zero literal"""
        self.assertTrue(TestLexer.checkLexeme("0", "0,<EOF>", 148))
    
    def test_float_literal_point(self):
        """Test float literal with decimal point"""
        self.assertTrue(TestLexer.checkLexeme("123.456", "123.456,<EOF>", 149))
    
    def test_float_literal_exponent(self):
        """Test float literal with exponent"""
        self.assertTrue(TestLexer.checkLexeme("1.2e3", "1.2e3,<EOF>", 150))
    
    def test_float_literal_negative_exponent(self):
        """Test float literal with negative exponent"""
        self.assertTrue(TestLexer.checkLexeme("1.2e-3", "1.2e-3,<EOF>", 151))
    
    def test_float_literal_zero_decimal(self):
        """Test float literal with zero decimal part"""
        self.assertTrue(TestLexer.checkLexeme("1.0", "1.0,<EOF>", 152))
    
    def test_float_literal_no_integer_part(self):
        """Test float literal with no integer part"""
        self.assertTrue(TestLexer.checkLexeme(".123", ".123,<EOF>", 153))
    
    def test_string_literal_simple(self):
        """Test simple string literal"""
        self.assertTrue(TestLexer.checkLexeme('"Hello"', '"Hello",<EOF>', 154))
    
    def test_string_literal_with_spaces(self):
        """Test string literal with spaces"""
        self.assertTrue(TestLexer.checkLexeme('"Hello World"', '"Hello World",<EOF>', 155))
    
    def test_string_literal_with_escape(self):
        """Test string literal with escape sequence"""
        self.assertTrue(TestLexer.checkLexeme('"Hello\\nWorld"', '"Hello\\nWorld",<EOF>', 156))
    
    def test_string_literal_with_tab(self):
        """Test string literal with tab escape"""
        self.assertTrue(TestLexer.checkLexeme('"Hello\\tWorld"', '"Hello\\tWorld",<EOF>', 157))
    
    def test_boolean_true(self):
        """Test boolean true literal"""
        self.assertTrue(TestLexer.checkLexeme("true", "true,<EOF>", 158))
    
    def test_boolean_false(self):
        """Test boolean false literal"""
        self.assertTrue(TestLexer.checkLexeme("false", "false,<EOF>", 159))
    
    def test_mixed_literals(self):
        """Test mixed literals"""
        self.assertTrue(TestLexer.checkLexeme('123 4.56 "string" true', '123,4.56,"string",true,<EOF>', 160))

    # Comment tests (161-170)
    def test_single_line_comment(self):
        """Test single line comment"""
        self.assertTrue(TestLexer.checkLexeme("// This is a comment", "<EOF>", 161))
    
    def test_single_line_comment_with_code(self):
        """Test single line comment with code"""
        self.assertTrue(TestLexer.checkLexeme("a = 5; // This is a comment", "a,=,5,;,<EOF>", 162))
    
    def test_multi_line_comment(self):
        """Test multi line comment"""
        self.assertTrue(TestLexer.checkLexeme("/* This is a\nmulti-line comment */", "<EOF>", 163))
    
    def test_multi_line_comment_with_code(self):
        """Test multi line comment with code"""
        self.assertTrue(TestLexer.checkLexeme("a = 5; /* This is a\nmulti-line comment */ b = 6;", "a,=,5,;,b,=,6,;,<EOF>", 164))
    
    # test này chưa true được, vì chưa hỗ trợ xử lý nested comment
    def test_nested_comment(self):
        """Test nested comments"""
        self.assertTrue(TestLexer.checkLexeme("/* outer /* inner */ comment */", "<EOF>", 165)) 
    
    def test_comment_with_special_chars(self):
        """Test comment with special characters"""
        self.assertTrue(TestLexer.checkLexeme("// !@#$%^&*()_+{}|:<>?", "<EOF>", 166))
    
    def test_comment_with_keywords(self):
        """Test comment with keywords"""
        self.assertTrue(TestLexer.checkLexeme("// var func if else for return", "<EOF>", 167))
    
    def test_comment_before_identifier(self):
        """Test comment before identifier"""
        self.assertTrue(TestLexer.checkLexeme("// comment\nabc", "abc,<EOF>", 168))
    
    def test_identifier_before_comment(self):
        """Test identifier before comment"""
        self.assertTrue(TestLexer.checkLexeme("abc // comment", "abc,<EOF>", 169))
    
    def test_multi_line_comment_newline(self):
        """Test multi line comment with additional newline"""
        self.assertTrue(TestLexer.checkLexeme("/* comment */\nabc", "abc,<EOF>", 170))
    
    # Error token tests (171-180)
    def test_error_token_at(self):
        """Test error token @"""
        self.assertTrue(TestLexer.checkLexeme("@", "ErrorToken @", 171))
    
    def test_error_token_dollar(self):
        """Test error token $"""
        self.assertTrue(TestLexer.checkLexeme("$", "ErrorToken $", 172))
    
    def test_error_token_hash(self):
        """Test error token #"""
        self.assertTrue(TestLexer.checkLexeme("#", "ErrorToken #", 173))
    
    def test_error_token_in_identifier(self):
        """Test error token in identifier"""
        self.assertTrue(TestLexer.checkLexeme("abc@def", "abc,ErrorToken @", 174))
    
    def test_error_token_with_valid_tokens(self):
        """Test error token with valid tokens"""
        self.assertTrue(TestLexer.checkLexeme("a = b @ c", "a,=,b,ErrorToken @", 175))
    
    def test_multiple_error_tokens(self):
        """Test multiple error tokens"""
        self.assertTrue(TestLexer.checkLexeme("a $ b @ c", "a,ErrorToken $", 176))
    
    def test_error_token_after_comment(self):
        """Test error token after comment"""
        self.assertTrue(TestLexer.checkLexeme("// comment\n@", "ErrorToken @", 177))
    
    def test_error_token_before_comment(self):
        """Test error token before comment"""
        self.assertTrue(TestLexer.checkLexeme("@ // comment", "ErrorToken @", 178))
    
    def test_error_backtick(self):
        """Test error token backtick"""
        self.assertTrue(TestLexer.checkLexeme("`", "ErrorToken `", 179))
    
    def test_error_tilde(self):
        """Test error token tilde"""
        self.assertTrue(TestLexer.checkLexeme("~", "ErrorToken ~", 180))
    
    # String error tests (181-190)
    def test_unclosed_string(self):
        """Test unclosed string"""
        self.assertTrue(TestLexer.checkLexeme('"Hello', 'Unclosed string: "Hello', 181))
    
    def test_unclosed_string_with_escape(self):
        """Test unclosed string with escape"""
        self.assertTrue(TestLexer.checkLexeme('"Hello\\n', 'Unclosed string: "Hello\\n', 182))
    
    def test_string_with_illegal_escape(self):
        """Test string with illegal escape"""
        self.assertTrue(TestLexer.checkLexeme('"Hello\\k"', 'Illegal Escape In string: "Hello\\k', 183))
    
    def test_string_with_newline(self):
        """Test string with newline"""
        self.assertTrue(TestLexer.checkLexeme('"Hello\nWorld"', 'Unclosed string: "Hello\n', 184))
    
    def test_unclosed_string_eof(self):
        """Test unclosed string at end of file"""
        self.assertTrue(TestLexer.checkLexeme('"', 'Unclosed string: "', 185))
    
    def test_escape_double_quote(self):
        """Test escape double quote in string"""
        self.assertTrue(TestLexer.checkLexeme('"Hello\\""', '"Hello\\"",<EOF>', 186))
    
    def test_escape_backslash(self):
        """Test escape backslash in string"""
        self.assertTrue(TestLexer.checkLexeme('"Hello\\\\"', '"Hello\\\\",<EOF>', 187))
    
    def test_illegal_escape_octal(self):
        """Test illegal escape octal in string"""
        self.assertTrue(TestLexer.checkLexeme('"Hello\\123"', r'Illegal Escape In string: "Hello\123', 188))
    
    def test_unclosed_string_with_valid_tokens(self):
        """Test unclosed string with valid tokens"""
        self.assertTrue(TestLexer.checkLexeme('a = "Hello; b = 5;', 'a,=,Unclosed string: "Hello; b = 5;', 189))
    
    def test_string_with_special_chars(self):
        """Test string with special characters"""
        self.assertTrue(TestLexer.checkLexeme('"!@#$%^&*()_+"', '"!@#$%^&*()_+",<EOF>', 190))
    
    # Complex program tests (191-200)
    def test_simple_program(self):
        """Test simple program"""
        input = """func main() {
    var a int = 5;
}"""
        expect = "func,main,(,),{,var,a,int,=,5,;,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 191))
    
    def test_if_statement(self):
        """Test if statement"""
        input = """if (a > b) {
    return a;
} else {
    return b;
}"""
        expect = "if,(,a,>,b,),{,return,a,;,},else,{,return,b,;,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 192))
    
    def test_for_loop(self):
        """Test for loop"""
        input = """for (var i int = 0; i < 10; i++) {
    print(i);
}"""
        expect = "for,(,var,i,int,=,0,;,i,<,10,;,i,++,),{,print,(,i,),;,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 193))
    
    def test_function_declaration(self):
        """Test function declaration"""
        input = """func add(a int, b int) int {
    return a + b;
}"""
        expect = "func,add,(,a,int,,,b,int,),int,{,return,a,+,b,;,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 194))
    
    def test_complex_expression(self):
        """Test complex expression"""
        input = """var result = (a + b) * c / (d - e) % f;"""
        expect = "var,result,=,(,a,+,b,),*,c,/,(,d,-,e,),%,f,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 195))
    
    def test_nested_blocks(self):
        """Test nested blocks"""
        input = """func main() {
    if (x > 0) {
        if (y > 0) {
            print("Quadrant 1");
        } else {
            print("Quadrant 4");
        }
    } else {
        if (y > 0) {
            print("Quadrant 2");
        } else {
            print("Quadrant 3");
        }
    }
}"""
        expect = "func,main,(,),{,if,(,x,>,0,),{,if,(,y,>,0,),{,print,(,\"Quadrant 1\",),;,},else,{,print,(,\"Quadrant 4\",),;,},},else,{,if,(,y,>,0,),{,print,(,\"Quadrant 2\",),;,},else,{,print,(,\"Quadrant 3\",),;,},},},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 196))
    
    def test_array_access(self):
        """Test array access"""
        input = """var value = arr[i][j];"""
        expect = "var,value,=,arr,[,i,],[,j,],;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 197))
    
    def test_complex_program_with_comments(self):
        """Test complex program with comments"""
        input = """// Factorial function
func factorial(n int) int {
    // Base case
    if (n <= 1) {
        return 1;
    }
    /* Recursive case */
    return n * factorial(n - 1);
}"""
        expect = "func,factorial,(,n,int,),int,{,if,(,n,<=,1,),{,return,1,;,},return,n,*,factorial,(,n,-,1,),;,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 198))
    
    def test_mixed_tokens_in_program(self):
        """Test mixed tokens in program"""
        input = """func gcd(a int, b int) int {
    if (b == 0) {
        return a;
    }
    return gcd(b, a % b);
}"""
        expect = "func,gcd,(,a,int,,,b,int,),int,{,if,(,b,==,0,),{,return,a,;,},return,gcd,(,b,,,a,%,b,),;,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 199))
    
    def test_program_with_error(self):
        """Test program with error"""
        input = """func main() {
    var x = 10;
    var y = 20;
    var z = x @+ y;
}"""
        expect = "func,main,(,),{,var,x,=,10,;,var,y,=,20,;,var,z,=,x,ErrorToken @"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 200))
    
    