import libcst as cst

class MultiplicationOperandVisualizer(cst.CSTVisitor):
    def visit_BinaryOperation(self, node: cst.BinaryOperation):
        if isinstance(node.operator, cst.Multiply):
            print(node.left.value)
            print(node.right.value)

class ArithmeticVisualizer(cst.CSTVisitor):
    def __init__(self):
        self.total = 0

    def visit_Integer(self, node):
        value = int(node.value)
        print(value)
        self.total += value

source_tree = cst.parse_expression("1 + 2 / 4 + 7 * 3")
visitor01 = ArithmeticVisualizer()
visitor02 = MultiplicationOperandVisualizer()

source_tree.visit(visitor01)
print()
source_tree.visit(visitor02)

print(f"Som: {visitor01.total}")