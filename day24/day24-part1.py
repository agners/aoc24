"""Advent of Code 2024 Day 24 part 1"""

from dataclasses import dataclass
from enum import IntEnum

class LogicGateType(IntEnum):
    AND = 0
    OR = 1
    XOR = 2

@dataclass
class Gate:
    left: str
    operand: LogicGateType
    right: str
    output: str

    def __hash__(self):
        return hash((self.left, self.operand, self.right, self.output))

    def __str__(self):
        return f"{self.left} {self.operand.name} {self.right} -> {self.output}"

def calculate_wire(gates_by_output: dict[str, Gate], wires: dict[str, bool], wire: str) -> bool:
    if wire in wires:
        return wires[wire]
    
    gate: Gate = gates_by_output[wire]

    left_value = calculate_wire(gates_by_output, wires, gate.left)
    right_value = calculate_wire(gates_by_output, wires, gate.right)

    if gate.operand == LogicGateType.AND:
        value = left_value and right_value
        wires[wire] = value
        return value
    elif gate.operand == LogicGateType.OR:
        value = left_value or right_value
        wires[wire] = value
        return value
    elif gate.operand == LogicGateType.XOR:
        value = left_value != right_value
        wires[wire] = value
        return value

    raise ValueError(f"Unknown operand {gate.operand}")

with open("test-data2.txt") as f:
    wires: dict[str, bool] = {}
    read_wires: bool = True

    lines = f.readlines()

    gates: set[Gate] = set()
    gates_by_output: dict[str, Gate] = {}
    output_wires: set[str] = set()

    for line in lines:
        line = line.strip()
        if line == "":
            read_wires = False
            continue

        if read_wires:
            name, value = line.split(": ")
            wires[name] = bool(int(value))
            if name.startswith("z"):
                output_wires.add(name)
        else:
            left, gate, right, _, output = line.split(" ")
            if output.startswith("z"):
                output_wires.add(output)
            gate = Gate(left=left, operand=LogicGateType[gate.upper()], right=right, output=output)
            gates.add(gate)
            gates_by_output[output] = gate

    output_value = 0
    for output_wire in sorted(output_wires):
        bit = int(output_wire[1:])
        value = calculate_wire(gates_by_output, wires, output_wire)
        print(f"{output_wire}: {value}")
        wires[output_wire] = value
        if value:
            output_value += 1 << bit 
    print("Decimal value:", output_value)



