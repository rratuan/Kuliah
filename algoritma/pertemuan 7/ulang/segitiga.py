n = int(input('N : '))

# pyramid
# preview
#     *     => i(1) = 1 ---- spasi = 4
#    ***    => i(2) = 3 ---- spasi = 3
#   *****   => i(3) = 5 ---- spasi = 2
#  *******  => i(4) = 7 ---- spasi = 1
# ********* => i(5) = 9 ---- spasi = 0
# spasi = n-i
# rumus = 2*i-1

for i in range(1,n+1):
    segitiga = ' '*(n-i) + '*'*(2*i-1)
    print(segitiga)