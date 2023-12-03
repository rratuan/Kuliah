program MenuPilihanRekursif;
{I.S.: pengguna memilih salah satu nomor menu}
{F.S.: menampilkan hasil sesuai nomor menu yang dipilih}
uses crt;
//Kamus Global
var
  Pilih,Suku,M,N : integer;

procedure Menu(var Pilih : integer);
{I.S.: pengguna memilih salah satu nomor menu}
{F.S.: menampilkan hasil sesuai nomor menu yang dipilih}
begin
  clrscr; textcolor(15);
  writeln('Menu Pilihan');
  writeln('------------');
  writeln('1. Barisan Fibonacci');
  writeln('2. M Kali N');
  writeln('0. Keluar');
  write('Pilihan Anda? '); readln(Pilih);
  //validasi menu pilihan
  while (Pilih < 0) or (Pilih > 2) do
  begin
    gotoxy(20,6); textcolor(yellow);
    write('Nomor Menu Salah, Ulangi (Tekan Enter)!');
    readln;
    gotoxy(15,6); clreol; textcolor(15); readln(Pilih);
  end;

end; //endprocedure

procedure BanyakSuku(var Suku : integer);
{I.S.: pengguna memasukkan banyaknya suku Fibonacci yang akan ditampilkan
       (Suku)}
{F.S.: menghasilkan banyaknya suku (Suku)}
begin
  write('Banyak Suku : '); readln(Suku);
  //validasi banyak suku
  while (Suku < 1) do
  begin
    gotoxy(1,4); textcolor(yellow);
    write('Banyak suku tidak boleh kurang dari 1, Ulangi (Tekan Enter)!');
    readln;
    gotoxy(1,4); clreol;
    gotoxy(15,3); clreol; textcolor(15); readln(Suku);
  end;
end; //endprocedure

function Fibonacci(Suku : integer):integer;
{I.S. : banyak suku (Suku) sudah terdefinisi}
{F.S. : menghasilkan fungsi rekursif Fibonacci per suku}
begin
  if (Suku = 1) or (Suku = 2)
    then
      Fibonacci := 1
    else
      Fibonacci := Fibonacci(Suku-2) + Fibonacci(Suku-1);
end; //endfunction

procedure TampilFibonacci(Suku : integer);
{I.S.: banyak suku (Suku) sudah terdefinisi }
{F.S.: menampilkan barisan Fibonacci: 1, 1, 2, 3, 5, ..}
var
  i : integer;
begin
  write('Barisan Fibonacci sebanyak ');
  textcolor(yellow); write(Suku);
  textcolor(15); write(' suku : ');
  for i := 1 to Suku do
  begin
    textcolor(yellow); delay(700); write(Fibonacci(i));
    if (i < Suku)
      then
      begin
        textcolor(15); delay(700); write(', ');
      end;
  end; //endfor
end; //endprocedure

procedure IsiMN(var M,N : integer);
{I.S.: pengguna memasukkan harga M dan harga N}
{F.S.: menghasilkan harga M dan harga N}
begin
  write('Masukkan Harga M : '); readln(M);
  write('Masukkan Harga N : '); readln(N);
end; //endprocedure

function Kali(M,N : integer):integer;
{I.S. : harga M dan harga N sudah terdefinisi}
{F.S. : menghasilkan fungsi rekursif M kali N menggunakan operator +}
begin
  if (M = 0) or (N = 0)
    then
      Kali := 0
    else
      if (M = 1)
        then
          Kali := N
        else
        begin
          if (M < 0)
            then
            begin
              M := -M;
              N := -N;
            end;
            Kali := N + Kali(M-1,N);
        end;
end; //endfunction

procedure TampilKali(var M,N : integer);
{I.S.: harga M dan harga N sudah terdefinisi}
{F.S.: menampilkan hasil M kali N}
var
  i : integer;
begin
  write(M:2,' x ',N:2,' = ');
  if (M = 0) or (N = 0) or (M = 1)
    then
    begin
      textcolor(yellow); write(Kali(M,N));
    end
    else
    begin
      if (M < 0)
        then
        begin
          M := -M;
          N := -N;
        end;
      for i := 1 to M do
      begin
        textcolor(yellow); delay(700); write(N);
        if (i < M)
          then
          begin
            textcolor(15); delay(700); write(' + ');
          end;
      end;
      writeln; textcolor(15);
      write('        = ');
      textcolor(yellow); write(Kali(M,N));
    end;
end; //endprocedure

//badan program utama
begin
  Menu(Pilih);
  while (Pilih <> 0) do
  begin
    if (Pilih = 1)
      then
      begin
        clrscr; textcolor(yellow);
        writeln('Barisan Fibonacci');
        writeln('-----------------');
        textcolor(15);
        BanyakSuku(Suku);
        TampilFibonacci(Suku);
        writeln;
        writeln; textcolor(yellow);
        write('Tekan enter untuk kembali ke Menu Pilihan...');
        readln;
      end
      else
        if (Pilih = 2)
          then
          begin
            clrscr; textcolor(yellow);
            writeln('M Kali N Menggunakan Operator +');
            writeln('-------------------------------');
            textcolor(15);
            IsiMN(M,N);
            TampilKali(M,N);
            writeln; writeln; textcolor(yellow);
            write('Tekan enter untuk kembali ke Menu Pilihan...');
            readln;
          end;
    Menu(Pilih);
  end;
end.
