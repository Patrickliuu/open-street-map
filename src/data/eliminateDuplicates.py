import pandas as pd

df = pd.read_json('clean_data.json')

initial = (len(df['operator'].unique()))

replacements = [
    ('Post CH AG', 'PostFinance'),
    ('Popstfinance', 'PostFinance'),
    ('Post Finace', 'PostFinance'),
    ('die Post', 'PostFinance'),
    ('La Poste Suisse SA', 'PostFinance'),
    ('post.ch', 'PostFinance'),
    ('Geldautomat Post', 'PostFinance'),
    ('La poste', 'PostFinance'),
    ('Die Schweizerische Post AG', 'PostFinance'),
    ('Posta', 'PostFinance'),

    ('Raiffeisenbanken Möhlin Genossenschaft', 'Raiffeisen'),
    ('Raiffeisenbank Aare-Rhein', 'Raiffeisen'),
    ('Raiffeisenbank Appenzell', 'Raiffeisen'),
    ('Raiffeisenbank Heiden', 'Raiffeisen'),
    ('Raiffeisen Bank', 'Raiffeisen'),
    ('Raiffeisenbank Thewil,', 'Raiffeisen'),
    ('Raiffaisen,', 'Raiffeisen'),
    ('Raiffeisen Rothenburg', 'Raiffeisen'),
    ('Raiffeisenbank Horw', 'Raiffeisen'),
    ('raiffeisen', 'Raiffeisen'),
    ('Raiffeisen ATM', 'Raiffeisen'),
    ('Raffeisen', 'Raiffeisen'),
    ('Raiffeisen Marbach—Rebstein', 'Raiffeisen'),
    ('Raiffeisenbank Berneck-Au', 'Raiffeisen'),
    ('Raiffeisen Bancautomat', 'Raiffeisen'),
    ('Raiffeisen Bankomat', 'Raiffeisen'),
    ('Raiffeisen Bancomat', 'Raiffeisen'),
    ('Raiffeisen AG', 'Raiffeisen'),
    ('Raiffeisenbank Bancomat', 'Raiffeisen'),
    ('Raiffeisen Drive in ', 'Raiffeisen'),
    ('Raiffeisenbank Gäu-Bipperamt', 'Raiffeisen'),
    ('Banca Raiffeisen', 'Raiffeisen'),
    ('Raiffeisenbank Hauptwil', 'Raiffeisen'),
    ('Raiffeisenbank Mittelthurgau', 'Raiffeisen'),
    ('Raiffeisenbank Regio Altnau', 'Raiffeisen'),
    ('Raiffeisen AG', 'Raiffeisen'),
    ('Bank Raiffeisn', 'Raiffeisen'),
    ('Raiffeisenbank Raron-Niederfesteln', 'Raiffeisen'),
    ('Raiffeisenbank Männedorf', 'Raiffeisen'),

    ('CreditSuisee', 'Credit Suisse'),
    ('CreditSuisse', 'Credit Suisse'),
    ('Crédit Suisse', 'Credit Suisse'),
    ('Credit Suisse Group AG', 'Credit Suisse'),

    ('UBS Bankomat', 'UBS'),
    ('ubs', 'UBS'),

    ('Basellandschaftliche Kantonalbank', 'Basler Kantonalbank'),
    ('CLER', 'Bank Cler'),
    ('Banque Celler', 'Bank Cler'),

    ('Banque cantonale de Fribourg', 'Kantonalbank Freiburg'),
    ('Banque Cantonale de Fribourg', 'Kantonalbank Freiburg'),
    ('BCF/FKB', 'Kantonalbank Freiburg'),
    ('FKB', 'Kantonalbank Freiburg'),

    ('BCGe', 'Kantonalbank Genf'),
    ('Banque cantonale de Genf', 'Kantonalbank Genf'),
    ('Banque cantonale de Genf BCG', 'Kantonalbank Genf'),

    ('GKB', 'Graubündner Kantonalbank'),
    ('Graubündner Kanonalbank', 'Graubündner Kantonalbank'),
    ('Graubündner Bank', 'Graubündner Kantonalbank'),
    ('Banca Cantonale', 'Graubündner Kantonalbank'),
    ('Banca Cantunala Grischuna', 'Graubündner Kantonalbank'),
    ('Banca Chantunala Grischuna', 'Graubündner Kantonalbank'),

    ('BCJ', 'Banque Cantonale de Jura'),

    ('Nidwaldner Kantonalbank', 'Kantonalbank Nidwalden'),

    ('Obwaldner Kantonalbank OKB', 'Kantonalbank Obwalden'),
    ('Obwaldner Kantonalbank', 'Kantonalbank Obwalden'),

    ('St.Galler Kantonalbank', 'Sankt Galler Kantonalbank'),
    ('SGKB', 'Sankt Galler Kantonalbank'),
    ('St.Galler Kantonalbank Au', 'Sankt Galler Kantonalbank'),
    ('Kantonalbank SG', 'Sankt Galler Kantonalbank'),

    ('BancaStato', 'Banca dello State'),
    ('Banca Stato', 'Banca dello State'),

    ('TKB', 'Thurgauer Kantonalban'),

    ('UKB', 'Urner Kantonalbank'),

    ('Caisse D’épargne De Nyon', 'Caisse D’Epargne De Nyon'),

    ('Banque cantonale du Valais', 'Walliser Kantonalbank'),
    ('Banque Cantonale du Valais', 'Walliser Kantonalbank'),
    ('Banque Cantonale du Valais (BCVs)', 'Walliser Kantonalbank'),
    ('Banque Cantonal du Valais', 'Walliser Kantonalbank'),
    ('Banque Cantonale Vaudoise', 'Walliser Kantonalbank'),
]

for replacement in replacements:
    df['operator'] = df['operator'].str.replace(replacement[0], replacement[1])

# print((df['operator'].unique()))

n_replacements = len(replacements)
final = (len(df['operator'].unique()))
difference = initial - final

print(df['operator'].unique())
# print(f"Started with {initial} and ended up with {final}. Amount useful replacements: {difference}/{n_replacements}")


df.to_json('clean_data.json', orient='records')
