#I.S inputkan Jumlah uang
#F.S outputkan pecahan uang yang di dapat

jumlahuang = int(input("Masukkan Jumlah Uang anda dengan kelipatan Rp.25 : "))

rp1000 = jumlahuang // 1000
sisa1 = jumlahuang % 1000
#sisa1 adalah sisa uang dari div 1000

rp500 = sisa1 // 500
sisa2 = sisa1 % 500
#sisa2 adalah sisa uang dari div 500

rp100 = sisa2 // 100
sisa3 = sisa2 % 100
#sisa3 adalah sisa uang dari div 100

rp50 = sisa3 // 50
rp25 = sisa3 % 50

print("uang senilai : ",jumlahuang,"setara dengan", rp1000, "buah pecahan Rp.1000 ditambah", rp500,"buah pecahan Rp.500 ditambah", rp100,"buah pecahan Rp.500 ditambah", rp50,"buah pecahan Rp.50 ditambah", rp25,"buah pecahan Rp.25")