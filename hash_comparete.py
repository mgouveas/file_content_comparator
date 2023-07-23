import hashlib

file_a = 'a.txt'
file_b = 'b.txt'

type_hash = 'ripemd160'

hash_a = hashlib.new(type_hash)
hash_a.update(open(file_a, 'rb').read())

hash_b = hashlib.new('ripemd160')
hash_b.update(open(file_b, 'rb').read())

if hash_a.digest() != hash_b.digest():
    print('Os arquivos são diferentes')
    print(hash_a.hexdigest())
    print(hash_b.hexdigest())

else:
    print('Os arquivos são iguais')
    print(hash_a.hexdigest())
    print(hash_b.hexdigest())
