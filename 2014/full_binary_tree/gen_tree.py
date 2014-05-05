with open('stress.in', 'w') as fout:
  fout.write('1\n')
  fout.write('1000\n')
  for i in range(2, 1001):
    fout.write('1 {}\n'.format(i))