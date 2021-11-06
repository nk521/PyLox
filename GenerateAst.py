import os


class GenerateAst:
    def __init__(self):
        self.outputDir = "Expr"
        self.baseName = "Expr"
        self.asList = [
            "Binary : left, operator, right",
            "Grouping : expression",
            "Literal : value",
            "Unary : operator, right"
        ]

    def defineAst(self):
        with open(os.path.join(self.outputDir, f"{self.baseName}.py"), "a") as f:
            f.write(f"class {self.baseName}Visitor:\n")
            for _type in self.asList:
                className = _type.split(":")[0].strip()
                f.write("\n".join(self.defineVisitor(className)))

            f.write(f"\nclass {self.baseName}:\n")
            f.write(f"\tdef accept(visitor: {self.baseName}Visitor):\n")
            f.write("\t\tpass\n")

            for _type in self.asList:
                className = _type.split(":")[0].strip()
                fields = _type.split(":")[1].strip()
                f.write("\n".join(self.defineType(className, fields)))
                f.write("\n")
            f.close()

    def defineType(self, className, fieldsList) -> str:
        stringToReturn = [f"class {className}({self.baseName}):"]
        stringToReturn.append(f"\tdef __init__(self, {fieldsList}):")
        for field in fieldsList.split(", "):
            stringToReturn.append(f"\t\tself.{field} = {field}")
        stringToReturn.append("")
        stringToReturn.append(f"\tdef accept(self, visitor: {self.baseName}Visitor):")
        stringToReturn.append(f"\t\treturn visitor.visit{className}{self.baseName}(self)")
        return stringToReturn

    def defineVisitor(self, className) -> str:
        stringToReturn = []
        stringToReturn.append(
            f"\tdef visit{className}{self.baseName}({self.baseName.lower()}): pass\n")
        return stringToReturn


a = GenerateAst()
a.defineAst()
