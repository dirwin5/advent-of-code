from time import time
from dataclasses import dataclass

RULES_DICT = {}

PARTS_LIST = []

@dataclass
class Part:
    x: int
    m: int
    a: int
    s: int

    def __post_init__(self):
        self.total = sum([self.x, self.m, self.a, self.s])


def main():
    input_list = open('input.txt', 'r').read().splitlines()
    # input_list = open('test.txt', 'r').read().splitlines()

    workflows = True
    for line in input_list:
        if line == '':
            workflows = False
            continue
        if workflows:
            name = line.split('{')[0]
            workflow = line.split('{')[1][:-1].split(',')
            RULES_DICT[name] = workflow
        else:
            line = line[1:-1]
            part_attributes = line.split(',')
            x = int(part_attributes[0].split('=')[1])
            m = int(part_attributes[1].split('=')[1])
            a = int(part_attributes[2].split('=')[1])
            s = int(part_attributes[3].split('=')[1])
            PARTS_LIST.append(Part(x, m, a, s))

    accepted_parts = []
    rejected_parts = []
    # test rules for each part
    for part in PARTS_LIST:
        workflow_name = 'in'
        while workflow_name not in ['A', 'R']:
            workflow = RULES_DICT[workflow_name]
            for rule in workflow:
                if len(rule.split(':')) == 1:
                    workflow_name = rule
                    break
                condition = rule.split(':')[0]
                condition_parameter = condition[0]
                condition_operator = condition[1]
                condition_value = int(condition[2:])
                if condition_operator == '>':
                    if getattr(part, condition_parameter) > condition_value:
                        workflow_name = rule.split(':')[1]
                        break
                elif condition_operator == '<':
                    if getattr(part, condition_parameter) < condition_value:
                        workflow_name = rule.split(':')[1]
                        break

        # check of part was accepted or rejected
        if workflow_name == 'A':
            accepted_parts.append(part)
        else:
            rejected_parts.append(part)

    # get total of accepted parts
    total = 0
    for part in accepted_parts:
        total += part.total

    print(f'Total: {total}')


if __name__ == '__main__':
    start_time = time()
    main()
    print('\nProcess complete')
    print(f"Process time: {round(time() - start_time, 2)} seconds.")