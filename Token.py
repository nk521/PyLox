import TokenType

class Token:
    def __init__(self, _type: TokenType.TokenType, lexeme: str, literal, line: int):
        self.type = _type
        self.lexeme = lexeme
        self.literal = literal
        self.line = line

    def __str__(self):
        return f"{self.type} {self.lexeme} {self.literal}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.type}, {self.lexeme}, {self.literal}, {self.line})"
