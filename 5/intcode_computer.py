from intcode_instructions import INSTRUCTION_SET

class ComputerState:
    def __init__(self):
        self.ip = None  # instruction pointer
        self.memory = []
        self.halt = None


class Computer:

    def __init__(self):
        self.state = ComputerState()

    def run(self, program):
        self.state.memory.extend(program)
        self.state.ip = 0
        self.state.halt = False

        while not self._program_completed():
            instruction = self._next_instruction()
            instruction.compute()

    def _parse_opcode(self):
        curr_word = self.state.memory[self.state.ip]
        curr_word = str(curr_word).zfill(5)
        opcode = int(curr_word[-2:])

        return opcode

    def _next_instruction(self):
        opcode = self._parse_opcode()

        try:
            instruction = INSTRUCTION_SET[opcode](self.state)
        except KeyError:
            raise Exception(f'Unknown Opcode {opcode} at address {self.state.ip}')

        return instruction


    def _program_completed(self):
        return self.state.halt or self.state.ip >= len(self.state.memory)
