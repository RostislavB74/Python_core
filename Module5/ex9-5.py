print('dec: {:d} hex: {:x} bin: {:b}'.format(
    15, 15, 15))  # dec: 15 hex: f bin: 1111
print('pi: {:0.3}'.format(3.1415))  # pi: 3.14
print('"{}" "{:+}" "{:-}" "{: }"'.format(1, 2, -3, 4))  # "1" "+2" "-3" " 4"
# |left      |**center**|     right|
print("|{:<10}|{:*^10}|{:>10}|".format('left', 'center', 'right'))
