import itertools

symbols = "SENDMORY"
nums = list(range(10))

for combo in itertools.permutations(nums, len(symbols)):
    assign = {symbols[i]: combo[i] for i in range(len(symbols))}

    # Leading digits cannot be zero
    if assign['S'] == 0 or assign['M'] == 0:
        continue

    # Form numbers using place values
    val_send = assign['S']*1000 + assign['E']*100 + assign['N']*10 + assign['D']
    val_more = assign['M']*1000 + assign['O']*100 + assign['R']*10 + assign['E']
    val_money = assign['M']*10000 + assign['O']*1000 + assign['N']*100 + assign['E']*10 + assign['Y']

    # Check equation
    if val_send + val_more == val_money:
        print("Valid Assignment:")
        for k in sorted(assign):
            print(k, "=", assign[k])

        print("\nResult:")
        print(f"{val_send} + {val_more} = {val_money}")
        break