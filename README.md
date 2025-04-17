Tkinter + PostgreSQL aplikace – „Škola a databáze“
Popis
Tato desktopová aplikace vytvořená pomocí Tkinteru slouží k jednoduché správě učitelů ve školní databázi. Umožňuje:
Vytvoření tabulky teacher v databázi PostgreSQL
Přidávání nových učitelů (jméno, věk, adresa)
Vyhledávání učitelů podle ID
Zobrazení všech záznamů v databázi

Jak to funguje
Aplikace se připojuje k databázi PostgreSQL pomocí knihovny psycopg2 a využívá connection pool.
Po spuštění vytvoří tabulku teacher, pokud ještě neexistuje.
Uživatelské rozhraní umožňuje vložit jméno, věk a adresu učitele a přidat ho do databáze.
Pomocí ID lze vyhledat konkrétního učitele.
Všechny záznamy se zobrazují v Listboxu se svislým posuvníkem.

Požadavky
Python 3.x
Knihovny:
tkinter (součástí standardní knihovny Pythonu)
psycopg2
Nastavení databáze
Před spuštěním aplikace je potřeba mít spuštěný PostgreSQL server a vytvořenou databázi, např. student.
