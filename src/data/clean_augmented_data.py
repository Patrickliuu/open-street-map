with open('clean_data.json', mode='r', encoding='utf-8') as read_file:
    content = read_file.read()
    print(content)

    patterns = [
        ('Bern/Berne', 'Bern'),
        ('Graub\\u00fcnden/Grischun/Grigioni', 'Graubünden'),
        ('Valais/Wallis', 'Wallis'),
        ('Fribourg/Freiburg', 'Freiburg'),
        ('Ticino', 'Tessin'),
        ('Vaud', 'Waadt'),
        ('Neuch\\u00e2tel', 'Neuenburg'),
        ('Gen\\u00e8ve', 'Genf'),
    ]

    for pattern in patterns:
        if pattern[0] not in content:
            print(f"WARNING: {pattern[0]} is invalid.")
        content = content.replace(pattern[0], pattern[1])

with open('clean_data.json', mode='w', encoding='utf-8') as write_file:
    write_file.write(content)
