import sys
input = sys.stdin.readline

def calc_formula(formula):
    number = float(formula[0])
    for n in formula:
        if n == '@':
            number *= 3
        if n == '%':
            number += 5
        if n == '#':
            number -= 7
        else:
            continue
    return number

T = int(input())
for _ in range(T):
    mars_formula = list(input().split())
    print(f'{calc_formula(mars_formula):.2f}')