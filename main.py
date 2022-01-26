# or gate
def or_gate(input1, input2):
    gate1 = input1 or input2
    return bool(gate1)


# gate for the function
def mitchells_gate(input1, input2, input3, input4):
    gate1 = or_gate(input1, input2)
    gate2 = or_gate(input3, input4)
    gate3 = or_gate(gate1, gate2)
    return bool(gate3)


#header
print("A\t B\t C\t D\t OUTPUT")
print("F\t F\t F\t F\t", mitchells_gate(False, False, False, False))
