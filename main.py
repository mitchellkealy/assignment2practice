# and gate
def and_gate(input1, input2):
  gate1 = input1 and input2
  return bool(gate1)

# not and gate
def nand_gate(input1, input2):
  gate1 = not(input1 and input2)
  return bool(gate1)

# gate for the function
def mitchells_gate(input1, input2, input3, input4):
    gate1 = and_gate(input1, input2)
    gate2 = and_gate(input3, input4)
    gate3 = nand_gate(gate1, gate2)
    return bool(gate3)

# header
print("A\t B\t C\t D\t OUTPUT")
print("T\t T\t T\t T\t", mitchells_gate(True, True, True, True))

