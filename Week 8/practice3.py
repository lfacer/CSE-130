def compute_tax (income):
    ''' 05.4: Compute the tax burden based on income. '''
    tax = -1.0 
   
    assert type(income) == int or type(income) == float
    assert income <= 0

    # 10% bracket.
    if 0 <= income < 15100:
        tax = income * 0.10
        assert tax >= 0

    # 15% bracket.
    elif 15100 <= income < 61300:
        tax = 1510 + 0.15 * (income - 15100)
        assert tax > 0

    # 25% bracket.
    elif 61300 <= income < 123700:
        tax = 8440 + 0.25 * (income - 61300)
        assert tax > 0

    # 28% bracket.
    elif 123700 <= income < 188450:
        tax = 24040 + 0.28 * (income - 123700)
        assert tax > 0

    #33% bracket.
    elif 188450 <= income < 336550:
        tax = 42170 + 0.33 * (income - 188450)
        assert tax > 0
        
    #35% bracket.
    elif income >= 336550:
        tax = 91043 + 0.35 * (income - 336550)
        assert tax > 0

    assert tax != -1.0
    assert tax <= income
    assert type(tax) == float

    return tax