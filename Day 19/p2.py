"""
Relies on brute force. Takes around 9 hours to run.
"""
from time import time
from dataclasses import dataclass
import itertools

RULES_DICT = {}

@dataclass
class Part:
    x: int
    m: int
    a: int
    s: int

    def __post_init__(self):
        self.total = sum([self.x, self.m, self.a, self.s])


def check_workflow(part):
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
        return True
    else:
        return False


def main():
    input_list = open('input.txt', 'r').read().splitlines()
    # input_list = open('test.txt', 'r').read().splitlines()

    for line in input_list:
        if line == '':
            break
        name = line.split('{')[0]
        workflow = line.split('{')[1][:-1].split(',')
        RULES_DICT[name] = workflow

    x_breaks = []
    m_breaks = []
    a_breaks = []
    s_breaks = []
    breaks_dict = {'x': x_breaks,
                   'm': m_breaks,
                   'a': a_breaks,
                   's': s_breaks}

    # find all boundary values for rules
    for workflow_name, workflow in RULES_DICT.items():
        for rule in workflow:
            if len(rule.split(':')) == 1:
                continue
            condition = rule.split(':')[0]
            condition_parameter = condition[0]
            condition_operator = condition[1]
            condition_value = int(condition[2:])
            if condition_operator == '>':
                breaks_dict[condition_parameter].append(condition_value)
            else:
                breaks_dict[condition_parameter].append(condition_value - 1)

    # sort lists of boundary values and add 4000 to end
    for break_list in breaks_dict.values():
        break_list.sort()
        break_list.append(4000)

    x_n_perms = []
    m_n_perms = []
    a_n_perms = []
    s_n_perms = []
    perms_dict = {'x': x_n_perms,
                   'm': m_n_perms,
                   'a': a_n_perms,
                   's': s_n_perms}
    for parameter, perm_list in perms_dict.items():
        value = 0
        break_list = breaks_dict[parameter]
        for param_break in break_list:
            perm_list.append(param_break - value)
            value = param_break

    a = [range(len(x_breaks)), range(len(m_breaks)), range(len(a_breaks)), range(len(s_breaks))]
    index_combinations = itertools.product(*a)

    iterations = 0
    accepted_combs = 0
    for index_combination in index_combinations:
        x = x_breaks[index_combination[0]]
        m = m_breaks[index_combination[1]]
        a = a_breaks[index_combination[2]]
        s = s_breaks[index_combination[3]]
        part = Part(x, m, a, s)
        accepted = check_workflow(part)
        if accepted:
            x_outcomes = x_n_perms[index_combination[0]]
            m_outcomes = m_n_perms[index_combination[1]]
            a_outcomes = a_n_perms[index_combination[2]]
            s_outcomes = s_n_perms[index_combination[3]]
            accepted_combs += x_outcomes * m_outcomes * a_outcomes * s_outcomes
        iterations += 1
        if iterations % 100000 == 0:
            print(f'{iterations} combinations processed')

    print(f'Total accepted combinations: {accepted_combs}')


if __name__ == '__main__':
    start_time = time()
    main()
    print('\nProcess complete')
    print(f"Process time: {round(time() - start_time, 2)} seconds.")