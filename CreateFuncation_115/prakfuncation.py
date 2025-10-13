# NO 1
def convert_temperature(value, unit):
    if unit.upper() == 'C':
        return (value * 9/5) + 32 
    elif unit.upper() == 'F':
        return (value - 32) * 5/9
    else:
        raise ValueError("Unit harus 'c' atau 'f'")
    
print("========= KONVERSI SUHU =========")
try:
    input_suhu = float(input("Masukkan nilai suhu: "))
    unit = input("Masukkan satuan suhu ('c' untuk celsius atau 'F' untuk Fahrenhit): ")
    konversi = convert_temperature(input_suhu, unit)
    if unit.upper() == 'C':
        print(f"{input_suhu}°C = {konversi:.2f}°F")
    elif unit.upper() == 'F':
        print(f"{input_suhu}°F = {konversi:.2f}°C")
    else:
        print("Satuan tidak dikenal.")
except ValueError as e:
    print("Terjadi kesalahan:", e)

# NO 2
luas_lingkaran = lambda jejari: 3.14159 * jejari ** 2

print("\n========= HITUNG LUAS LINGKARAN =========")
try:
    jejari = float(input("Masukkan jari-jari lingkaran: "))
    result = luas_lingkaran(jejari)
    print(f"Luas lingkaran dengan jari-jari {jejari} adalah {result:.2f}")
except ValueError:
    print("Input harus berupa angka!")