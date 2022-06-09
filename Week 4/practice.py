tax_bracket = int(input("How much money do you make? "))

if tax_bracket >= 15100:

    if tax_bracket < 61300:
        print("15% tax")

    elif tax_bracket > 61300:
        
        if tax_bracket < 123700:
            print("25% tax")

        elif tax_bracket > 123700:

            if tax_bracket < 188450:
                print("28% tax")

            elif tax_bracket > 188450:

                if tax_bracket < 336550:
                    print("33% tax")

                elif tax_bracket > 336550:
                    print("35% tax")


elif tax_bracket < 15100:

    if tax_bracket <= 0:
        print("0% tax")

    elif tax_bracket > 0:
        print("10% tax")