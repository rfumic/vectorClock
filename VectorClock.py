class VectorClock:
    # ... your code goes here ...
    def __init__(self):
        self.clocks = {}

    def increment(self, node):
        # self.clocks = [(n[0], n[1] + 1) if n[0] == node else n for n in self.clocks]
        self.clocks[node] = self.clocks.get(node, 0) + 1

    def set(self, node, value):
        # self.clocks = [(node, value) if n[0] == node else n for n in self.clocks]
        self.clocks[node] = value

    def __str__(self):
        return f"{list(self.clocks.items())}"

    def __add__(self, new):
        return 3


if __name__ == "__main__":

    v1 = VectorClock()
    v1.increment("A")  # uvećaj timestamp za node "A"
    v1.increment("B")  # uvećaj timestamp za node "B"

    v2 = VectorClock()
    v2.increment("C")
    v2.set("B", 2)  # postavi timestamp za node "B" na dvojku

    print(v1, v2)  # [('A', 1), ('B', 1)] [('C', 1), ('B', 2)]

    # v3 = v1 + v2
    # print(v3)  # [('A', 1), ('B', 2), ('C', 1)]

    # print("Equal:       v1 == v1 \t", v1 == v1)  # True
    # print("Not equal:   v1 != v2 \t", v1 != v2)  # True
    # print("Before:      v1 < v2 \t", v1 < v2)  # False
    # print("Concurrent:  v1 // v2 \t", v1 // v2)  # True
