fh = open('test.txt', 'w')
symbols_written = fh.write('hello!')
print(symbols_written)  # 6
fh.close()

# В этом примере мы открыли файл test.txt для записи и записали туда строку 'hello!' длиной в 6 символов.