def arkaFood(harga, voucher, jarak, pajak):
    voucher_dict = {
        "ARKAFOOD5": {
            "min": 50000,
            "percent_disc": 50/100,
            "max_disc": 50000
        },
        "DITRAKTIRDEMY": {
            "min": 25000,
            "percent_disc": 60/100,
            "max_disc": 30000
        }
    }
    
    #Diskon
    disc_amount = 0
    if voucher != "False":
        if voucher in voucher_dict:
            if harga >= voucher_dict[voucher].get("min"):
                disc_amount = harga * voucher_dict[voucher].get("percent_disc")
                if disc_amount > voucher_dict[voucher].get("max_disc"):
                    disc_amount = voucher_dict[voucher].get("max_disc")
    
    #Menghitung pajak dari harga asli
    tax_amount = 0
    if pajak != "False":
        percent_tax = 5/100
        tax_amount = harga * percent_tax
    
    #Menghitung Ongkos Kirim
    jarak_bawah = 1.5
    ongkir = 5000 #Dasar Tarif
    if jarak > jarak_bawah:
        per_kilo = 3000
        ongkir += (jarak - jarak_bawah * 1.0) * per_kilo
    
    return harga - disc_amount + tax_amount + ongkir 

print(arkaFood(75000,"ARKAFOOD5",5.5,"False"))