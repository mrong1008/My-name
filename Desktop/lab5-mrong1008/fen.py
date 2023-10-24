def empty_board():
    result = ""
    for i in range(9):
        if i == 8: #last row
            result += "   a  b  c  d  e  f  g  h"
            break
        else:
            result += str(8-i)
        for j in range(8):
            result += "  ."
        result += "\n"
    return result

def fen_number(fen):
    result = ""
    for i in range(int(fen)):
        result += "  ."
    return result

def fen_line(s): #"rnq1kbnr"
    result = ""
    for i in range(len(s)):
        if s[i] in ['1','2','3','4','5','6','7','8']:
            result += fen_number(s[i])
        else:
            result += "  "+s[i]
    return result

def fen_board(s): #"rnlqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
    result = ""
    use_s = s.split('/')
    for i in range(len(use_s)):
        result += str(8-i) + fen_line(use_s[i]) + "\n"
    result += "   a  b  c  d  e  f  g  h"
    return result
print(fen_board("rn1qkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"))