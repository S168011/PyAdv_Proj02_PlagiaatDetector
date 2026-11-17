import libcst as cst

class ArithmeticVisualizer(cst.CSTVisitor):
    def __init__(self):
        self.total = 0

    def visit_Integer(self, node):
        value = int(node.value)
        print(value)
        self.total += value

source_tree = cst.parse_expression("1 + 2 / 4 + 7 * 3")
visitor = ArithmeticVisualizer()

source_tree.visit(visitor)

print(f"Som: {visitor.total}")