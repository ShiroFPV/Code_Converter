import os, time, sys
from platform import system

def bin_to_dec(n):
    return int(n, 2)
def hex_to_dec(n):
    return int(n, 16)
def oct_to_dec(n):
    return int(n, 8)
def ascii_to_dec(n):
    return ord(n) if n else 0
def gray_to_dec(n):
    val = int(n, 2)
    mask = val
    while mask:
        mask >>= 1
        val ^= mask
    return val
def bcd_to_dec(n):
    decimal_result = 0
    for i in range(0, len(n), 4):
        bcd_digit = n[i:i+4]
        if not all(c in '01' for c in bcd_digit):
            raise ValueError(f"Invalid BCD digit: {bcd_digit}. Must be 0s and 1s.")
        digit_val = int(bcd_digit, 2)
        if digit_val > 9:
            raise ValueError(f"Invalid BCD digit value: {digit_val}. Must be between 0-9.")
        decimal_result = decimal_result * 10 + digit_val
    return decimal_result
def to_bin(n):
    return bin(n)[2:].upper()
def to_hex(n):
    return hex(n)[2:].upper()
def to_oct(n):
    return oct(n)[2:].upper()
def to_ascii(n):
    return chr(n) if 32 <= n <= 126 else "?"
def to_gray(n):
    return bin(n ^ (n >> 1))[2:].upper()
def to_bcd(n):
    if n < 0:
        return "?"
    return ''.join(format(int(d), '04b') for d in str(n))
def clear_screen():
    os.system('cls' if system() == 'Windows' else 'clear')
def convert_number(n, fmt):
    return (
        str(n) if fmt == 1 else
        to_bin(n) if fmt == 2 else
        to_hex(n) if fmt == 3 else
        to_oct(n) if fmt == 4 else
        to_ascii(n) if fmt == 5 else
        to_gray(n) if fmt == 6 else
        to_bcd(n)
    )
def main():
    while True:
        i = read("Eingabeformat", ["Dezimal", "Binär", "Hexadezimal", "Oktal", "ASCII", "Gray", "BCD"])
        o = read("Ausgabeformat", ["Dezimal", "Binär", "Hexadezimal", "Oktal", "ASCII", "Gray", "BCD"])
        n = read_input_value(i)
        calculate_and_display(n, i, o)
        if not ask_restart():
            break
def read(prompt, options):
    clear_screen()
    while True:
        print(f"Wähle {prompt}:")
        for j, opt in enumerate(options, 1):
            print(f"{j}. {opt}")
        try:
            c = int(input("Nummer: "))
            if 1 <= c <= len(options):
                return c
        except ValueError:
            pass
        print("Ungültige Eingabe! Bitte geben Sie eine gültige Nummer ein.")
        time.sleep(1)
        clear_screen()
def read_input_value(input_format_choice):
    clear_screen()
    while True:
        if input_format_choice == 5:
            user_input = input("Geben Sie den Text ein: ")
        else:
            user_input = input("Geben Sie die Zahl(en) ein (getrennt mit Leerzeichen): ")

        try:
            if input_format_choice == 1:
                [int(x) for x in user_input.split()]
            elif input_format_choice == 2:
                [int(x, 2) for x in user_input.split()]
            elif input_format_choice == 3:
                [int(x, 16) for x in user_input.split()]
                user_input = user_input.upper()
            elif input_format_choice == 4:
                [int(x, 8) for x in user_input.split()]
            elif input_format_choice == 5:
                if not all(32 <= ord(c) <= 126 for c in user_input):
                    raise ValueError("Ungültige ASCII-Zeichen. Nur druckbare ASCII-Zeichen (32-126) sind erlaubt.")
            elif input_format_choice == 6:
                [int(x, 2) for x in user_input.split()]
            elif input_format_choice == 7:
                parts = user_input.split()
                for part in parts:
                    bcd_to_dec(part)
            return user_input
        except ValueError as e:
            print(f"Ungültige Eingabe! Fehler: {e}")
            time.sleep(2)
            clear_screen()
        except Exception as e:
            print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")
            time.sleep(2)
            clear_screen()
def calculate_and_display(input_value, input_format_choice, output_format_choice):
    clear_screen()
    try:
        decimal_numbers = []
        if input_format_choice == 5:
            decimal_numbers = [ascii_to_dec(char) for char in input_value]
        else:
            parts = input_value.strip().split()
            for part in parts:
                if input_format_choice == 1:
                    decimal_numbers.append(int(part))
                elif input_format_choice == 2:
                    decimal_numbers.append(bin_to_dec(part))
                elif input_format_choice == 3:
                    decimal_numbers.append(hex_to_dec(part))
                elif input_format_choice == 4:
                    decimal_numbers.append(oct_to_dec(part))
                elif input_format_choice == 6:
                    decimal_numbers.append(gray_to_dec(part))
                elif input_format_choice == 7:
                    decimal_numbers.append(bcd_to_dec(part))

        if input_format_choice == output_format_choice:
            print("Eingabe- und Ausgabeformate dürfen nicht gleich sein!")
        elif output_format_choice == 5:
            print("Resultat (ASCII):", ''.join(to_ascii(num) for num in decimal_numbers))
        else:
            converted_results = [convert_number(num, output_format_choice) for num in decimal_numbers]
            print("Resultat:", ' '.join(converted_results))
        time.sleep(3)
    except ValueError as e:
        print(f"Fehler bei der Konvertierung: {e}")
        time.sleep(2)
    except Exception as e:
        print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")
        time.sleep(2)
def ask_restart():
    while True:
        print("\nNeue Umwandlung?\n1. Ja\n2. Nein")
        try:
            choice = int(input("Nummer: "))
            clear_screen()
            if choice == 1:
                return True
            elif choice == 2:
                print("Beende das Programm...")
                time.sleep(1)
                clear_screen()
                sys.exit(0)
            else:
                print("Ungültige Eingabe! Bitte geben Sie '1' oder '2' ein.")
        except ValueError:
            print("Ungültige Eingabe! Bitte geben Sie eine Nummer ein.")
        time.sleep(1)
        clear_screen()
if __name__ == "__main__":
    main()