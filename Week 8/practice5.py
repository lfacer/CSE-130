def compute_tax(income):
    ''' 05.6: Compute the tax burden based on income. '''
    brackets = [
        #   min       max  fixed  rate 
        (     0,    15100,     0, 0.10),
        ( 15100,    61300,  1510, 0.15),
        ( 61300,   123700,  8440, 0.25),
        (123700,   188450, 24040, 0.28),
        (188450,   336500, 42170, 0.33),
        (336500, 99999999, 91043, 0.35)
    ]

    for bracket in brackets:
        if bracket[0] <= income and bracket[1] >= income:
            assert bracket[0] < bracket[1]
            assert bracket[2] < income
            tax = bracket[2] + bracket[3] * (income - bracket[0])
            assert type(tax) == float
            assert tax <= income
            return tax
    assert False
    return 0.0