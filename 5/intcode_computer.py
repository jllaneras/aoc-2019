class Instruction:
    @property
    def size(self):
        raise NotImplementedError

    def __init__(self, computer_state):
        self.state = computer_state

        curr_word = self.state.memory[self.state.ip]
        curr_word = str(curr_word).zfill(5)
        self.param_modes = curr_word[:-2]

    def compute(self):
        raise NotImplementedError

    def _get_param(self, ip_offset):
        param = self.state.memory[self.state.ip + ip_offset]

        mode = self.param_modes[-ip_offset]

        if mode == '1':
            return param
        elif mode == '0':
            return self.state.memory[param]
        else:
            raise Exception(f'Parameter mode {mode} not supported')

    def _write_result(self, ip_offset, result):
        address = self.state.memory[self.state.ip + ip_offset]
        self.state.memory[address] = result


class Add(Instruction):
    size = 4

    def compute(self):
        param1 = self._get_param(1)
        param2 = self._get_param(2)

        result = param1 + param2

        self._write_result(3, result)


class Mult(Instruction):
    size = 4

    def compute(self):
        param1 = self._get_param(1)
        param2 = self._get_param(2)

        result = param1 * param2

        self._write_result(3, result)


class Halt(Instruction):
    size = 1

    def compute(self):
        self.state.halt = True


class Input(Instruction):
    size = 2

    def compute(self):
        result = input("Introduce input: ")
        self._write_result(1, int(result))


class Output(Instruction):
    size = 2

    def compute(self):
        param = self._get_param(1)
        print(param)


class ComputerState:
    def __init__(self):
        self.ip = None  # instruction pointer
        self.memory = []
        self.halt = None


class Computer:

    INSTRUCTIONS = {
        99: Halt,
        1: Add,
        2: Mult,
        3: Input,
        4: Output
    }

    def __init__(self):
        self.state = ComputerState()

    def run(self, program):
        self.state.memory.extend(program)
        self.state.ip = 0
        self.state.halt = False

        while not self._program_completed():
            instruction = self._next_instruction()
            instruction.compute()
            self.state.ip += instruction.size

    def _parse_opcode(self):
        curr_word = self.state.memory[self.state.ip]
        curr_word = str(curr_word).zfill(5)
        opcode = int(curr_word[-2:])

        return opcode

    def _next_instruction(self):
        opcode = self._parse_opcode()

        try:
            instruction = Computer.INSTRUCTIONS[opcode](self.state)
        except KeyError:
            raise Exception(f'Unknown Opcode {opcode} at address {self.state.ip}')

        return instruction


    def _program_completed(self):
        return self.state.halt or self.state.ip >= len(self.state.memory)
