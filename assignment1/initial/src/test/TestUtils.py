import sys,os
from antlr4 import *
from antlr4.error.ErrorListener import ConsoleErrorListener,ErrorListener
current_dir = os.path.dirname(os.path.abspath(__file__))
parser_path = os.path.abspath(os.path.join(current_dir, 'main', 'minigo', 'parser'))
target_path = os.path.abspath(os.path.join(current_dir, '..', 'target', 'main', 'minigo', 'parser'))

# Thêm vào sys.path nếu chưa có
if parser_path not in sys.path:
    sys.path.insert(0, parser_path)
if os.path.isdir(target_path) and target_path not in sys.path:
    sys.path.insert(0, target_path)

# Debug
print(f"Importing from: {parser_path}")
print(f"Target path: {target_path}")

# Import thử
try:
    from MiniGoLexer import MiniGoLexer
    from MiniGoParser import MiniGoParser
    from lexererr import ErrorToken, UncloseString, IllegalEscape
    print("All imports successful!")
except ImportError as e:
    print(f"Import error: {e}")
    print(f"Current sys.path: {sys.path}")
    raise

import difflib

class TestUtil:
    @staticmethod
    def makeSource(inputStr,num):
        filename = "./test/testcases/" + str(num) + ".txt"
        file = open(filename,"w")
        file.write(inputStr)
        file.close()
        return FileStream(filename)


class TestLexer:
    @staticmethod
    def test(inputdir,outputdir,num):
        dest = open(outputdir + "/" + str(num) + ".txt","w")
        lexer = MiniGoLexer(FileStream(inputdir + "/" + str(num) + ".txt"))
        try:
            TestLexer.printLexeme(dest,lexer,"\n")
        except (ErrorToken,UncloseString,IllegalEscape) as err:
            dest.write(err.message+"\n")
        except Exception as err:
            dest.write(str(err)+"\n")
        finally:
            dest.close() 
    @staticmethod
    def checkLexeme(input,expect,num):
        inputfile = TestUtil.makeSource(input,num)
        dest = open("./test/solutions/" + str(num) + ".txt","w")
        lexer = MiniGoLexer(inputfile)
        try:
            TestLexer.printLexeme(dest,lexer,",")
        except (ErrorToken,UncloseString,IllegalEscape) as err:
            dest.write(err.message)
            print(err.message)
        except Exception as err:
            dest.write(str(err)+"\n")
        finally:
            dest.close() 
        dest = open("./test/solutions/" + str(num) + ".txt","r")
        line = dest.read()
        return line == expect

    @staticmethod    
    def printLexeme(dest,lexer,char):
        tok = lexer.nextToken()
        if tok.type != Token.EOF:
            dest.write(tok.text+char)
            TestLexer.printLexeme(dest,lexer,char)
        else:
            dest.write("<EOF>")
class NewErrorListener(ConsoleErrorListener):
    INSTANCE = None
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise SyntaxException("Error on line "+ str(line) + " col " + str(column + 1)+ ": " + offendingSymbol.text)
NewErrorListener.INSTANCE = NewErrorListener()

class SyntaxException(Exception):
    def __init__(self,msg):
        self.message = msg

class TestParser:
    @staticmethod
    def test(inputdir,outputdir,num):
        dest = open(outputdir + "/" + str(num) + ".txt","w")
        lexer = MiniGoLexer(FileStream(inputdir + "/" + str(num) + ".txt"))
        listener = TestParser.createErrorListener()

        tokens = CommonTokenStream(lexer)

        parser = MiniGoParser(tokens)
        parser.removeErrorListeners()
        parser.addErrorListener(listener)
        try:
            parser.program()
            dest.write("successful\n")
        except SyntaxException as f:
            dest.write(f.message + "\n")
        except Exception as e:
            dest.write(str(e))
        finally:
            dest.close()
    @staticmethod
    def createErrorListener():
         return NewErrorListener.INSTANCE

    @staticmethod
    def checkParser(input,expect,num):
        inputfile = TestUtil.makeSource(input,num)
        dest = open("./test/solutions/" + str(num) + ".txt","w")
        lexer = MiniGoLexer(inputfile)
        listener = TestParser.createErrorListener()

        tokens = CommonTokenStream(lexer)

        parser = MiniGoParser(tokens)
        parser.removeErrorListeners()
        parser.addErrorListener(listener)
        try:
            parser.program()
            dest.write("successful")
        except SyntaxException as f:
            dest.write(f.message)
        except Exception as e:
            dest.write(str(e))
        finally:
            dest.close()
        dest = open("./test/solutions/" + str(num) + ".txt","r")
        line = dest.read()
        return line == expect


        
