import sys,os
from antlr4 import *
from antlr4.error.ErrorListener import ConsoleErrorListener,ErrorListener
if not './main/minigo/parser/' in sys.path:
    sys.path.append('./main/minigo/parser/')
if os.path.isdir('../target/main/minigo/parser') and not '../target/main/minigo/parser/' in sys.path:
    sys.path.append('../target/main/minigo/parser/')
from MiniGoLexer import MiniGoLexer
from MiniGoParser import MiniGoParser
from lexererr import *
import difflib

class TestUtil:
    @staticmethod
    # Hàm này tạo một file input và trả về FileStream của file này để lexer có thể đọc
    def makeSource(inputStr,num):
        # Tạo 1 file input trong folder test/testcases
        filename = "./test/testcases/" + str(num) + ".txt" 
        file = open(filename,"w")
        file.write(inputStr)
        file.close()
        # Trả về FileStream của file này để lexer có thể đọc
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
        # Tạo 1 file input trong folder test/testcases và trả về FileStream của file này để lexer có thể đọc
        inputfile = TestUtil.makeSource(input,num)
        # Tạo 1 file output trong folder test/solutions và mở file trong chế độ ghi
        dest = open("./test/solutions/" + str(num) + ".txt","w")
        # Khởi tạo MiniGoLexer với FileStream của file input
        # Lexer sẽ đọc nội dung từ input và chuẩn bị phân tích từ vựng
        lexer = MiniGoLexer(inputfile)
        try:
            # Gọi hàm printLexeme để phân tích từ vựng và ghi kết quả vào file dest
            # Tham số char=',' để phân tách các token bằng dấu phẩy
            TestLexer.printLexeme(dest,lexer,",")
        except (ErrorToken,UncloseString,IllegalEscape) as err:
            # Bắt các ngoại lệ từ vựng như ErrorToken, UncloseString, IllegalEscape
            # và ghi thông báo lỗi vào file kết quả
            dest.write(err.message)
        except Exception as err:
            # Bắt các ngoại lệ khác và ghi thông báo lỗi vào file kết quả
            dest.write(str(err)+"\n")
        finally:
            # Đảm bảo file kết quả được đóng dù có lỗi hay không
            dest.close() 
        # Mở file kết quả trong chế độ đọc
        dest = open("./test/solutions/" + str(num) + ".txt","r")
        # Đọc nội dung của file kết quả
        line = dest.read()
        # So sánh nội dung của file kết quả với nội dung mong đợi
        return line == expect

    @staticmethod
    def printLexeme(dest,lexer,char):
        # Lấy token tiếp theo từ lexer
        # nextToken() đọc token từ input và tiến con trỏ tới vị trí tiếp theo
        tok = lexer.nextToken()
        # Kiểm tra nếu token không phải là EOF (End Of File)
        if tok.type != Token.EOF:
            # Ghi text của token vào file kết quả, theo sau là ký tự phân tách (thường là dấu phẩy)
            dest.write(tok.text+char)
            # Gọi đệ quy để xử lý token tiếp theo
            # Đây là cách để duyệt qua tất cả các token trong input
            TestLexer.printLexeme(dest,lexer,char)
        else:
            # Nếu gặp token EOF, ghi "<EOF>" vào file kết quả
            # Đây là dấu hiệu kết thúc của quá trình phân tích từ vựng  
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


        
