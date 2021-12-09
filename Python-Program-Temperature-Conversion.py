print("""pilihan derajat suhu
1. Celcius
2. Reamur
3. Fahrenheit
4. Kelvin""")
print('----------------------')
suhu_saat_ini = int(input("Masukan suhu saat ini: "))
perhitungan = int(input("suhu pada derajat [1..4]: "))

if perhitungan == 1:
  fahrenheit = (9 / 5) * suhu_saat_ini + 32
  reamur = (4 / 5) * suhu_saat_ini
  kelvin = suhu_saat_ini + 273
  print(float(suhu_saat_ini) ,"C =", reamur, "R")
  print(float(suhu_saat_ini) ,"C =", fahrenheit, "F")
  print(float(suhu_saat_ini) ,"C =", kelvin, "K")

elif perhitungan == 2:
  celcius = (5 / 4) * suhu_saat_ini
  fahrenheit = (9 / 4) * suhu_saat_ini + 32
  kelvin = (5 / 4) * suhu_saat_ini + 273
  print(float(suhu_saat_ini) ,"R =", celcius, "C")
  print(float(suhu_saat_ini) ,"R =", fahrenheit, "F")
  print(float(suhu_saat_ini) ,"R =", kelvin, "K")

elif perhitungan == 3:
  celcius = (5 / 9) * (suhu_saat_ini - 32)
  reamur = (4 / 9) * (suhu_saat_ini - 32)
  kelvin = (5 / 9) * (suhu_saat_ini - 32) + 273
  print(float(suhu_saat_ini) ,"F =", celcius, "C")
  print(float(suhu_saat_ini) ,"C =", reamur, "R")
  print(float(suhu_saat_ini) ,"F =", kelvin, "K")

elif perhitungan == 4:
  celcius = suhu_saat_ini - 273
  fahrenheit = (9 / 5) * (suhu_saat_ini - 273) + 32
  reamur = (4 / 5) * (suhu_saat_ini - 273)
  print(float(suhu_saat_ini) ,"K =", float(celcius), "C")
  print(float(suhu_saat_ini) ,"K =", float(fahrenheit), "F")
  print(float(suhu_saat_ini) ,"C =", float(reamur), "R")
