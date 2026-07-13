class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = 0
        # record = [0] * len(operations)
        record = []
        for i in range(len(operations)):
            if operations[i] == "+":
                record.append(record[len(record) - 2] + record[len(record) - 1])
            elif operations[i] == "C":
                record.pop()
            elif operations[i] == "D":
                record.append(2 * record[len(record) - 1])
            else:
                record.append(int(operations[i]))

        return sum(record)

        