expe = {
    'jan': 2200,
    'feb': 2350,
    'mar': 2600,
    'apr': 2130,
    'may': 2190
}


print(expe['feb']-expe['jan'])
print(expe['jan']+expe['feb']+expe['mar'])

print(2600 in expe)

expe['jun'] = 1800

expe['apr'] = expe['apr']-200


print(expe)
