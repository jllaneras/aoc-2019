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

        self.state.ip += self.size


class Mult(Instruction):
    size = 4

    def compute(self):
        param1 = self._get_param(1)
        param2 = self._get_param(2)

        result = param1 * param2

        self._write_result(3, result)

        self.state.ip += self.size


class Halt(Instruction):
    size = 1

    def compute(self):
        self.state.halt = True
        self.state.ip += self.size


class Input(Instruction):
    size = 2

    def compute(self):
        result = input("Introduce input: ")
        self._write_result(1, int(result))
        self.state.last_input = result
        self.state.ip += self.size


class Output(Instruction):
    size = 2

    def compute(self):
        param = self._get_param(1)
        print(param)
        self.state.last_output = param
        self.state.ip += self.size


class JumpIfTrue(Instruction):
    size = 3

    def compute(self):
        param = self._get_param(1)
        if param != 0:
            self.state.ip = self._get_param(2)
        else:
            self.state.ip += self.size


class JumpIfFalse(Instruction):
    size = 3

    def compute(self):
        param = self._get_param(1)
        if param == 0:
            self.state.ip = self._get_param(2)
        else:
            self.state.ip += self.size


class LessThan(Instruction):
    size = 4

    def compute(self):
        param1 = self._get_param(1)
        param2 = self._get_param(2)

        if param1 < param2:
            result = 1
        else:
            result = 0

        self._write_result(3, result)
        self.state.ip += self.size


class Equals(Instruction):
    size = 4

    def compute(self):
        param1 = self._get_param(1)
        param2 = self._get_param(2)

        if param1 == param2:
            result = 1
        else:
            result = 0

        self._write_result(3, result)
        self.state.ip += self.size


INSTRUCTION_SET = {
    99: Halt,
    1: Add,
    2: Mult,
    3: Input,
    4: Output,
    5: JumpIfTrue,
    6: JumpIfFalse,
    7: LessThan,
    8: Equals
}
