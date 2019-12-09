

def fuel(mass):
    if mass < 0:
        return 0
    return (mass // 3)-2


if __name__ == '__main__':
    fuel_sum = 0
    with open('day1.txt', 'rt') as f_obj:
        for line in f_obj:
            try:
                fuel_sum += fuel(int(line))
            except ValueError:
                continue
    print(fuel_sum)

