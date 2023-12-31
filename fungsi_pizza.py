#Fungsi pemilihan pizza dengan parameter crust, size, dan extra
def pizza(crust, size, extra):
    #Harga awal
    harga = 0

    #pilihan statement di varian crust pan pizza
    if crust == 'pan pizza' and size == 'personal':#Kondisi apakah benar pesanan pan pizza dengan ukuran personal
        harga += 43637                             #Menambahkan harga pesanan(harga akan otomatis diperbarui) 
        if extra == 'yes':                         #Jika pesanan ingin extra keju
            harga += 13636                         #Maka harga pesanan akan ditambah lagi sesuai harga tersebut
    elif crust == 'pan pizza' and size == 'regular':#Kondisi apakah benar pesanan pan pizza dengan ukuran regular
        harga += 100910                             #Menambahkan harga pesanan(harga akan otomatis diperbarui) 
        if extra == 'yes':                          #Jika pesanan ingin extra keju
            harga += 16364                          #Maka harga pesanan akan ditambah lagi sesuai harga tersebut
    elif crust == 'pan pizza' and size == 'large':#Kondisi apakah benar pesanan pan pizza dengan ukuran large
        harga += 132727                           #Menambahkan harga pesanan(harga akan otomatis diperbarui)
        if extra == 'yes':                        #Jika pesanan ingin extra keju
            harga += 19091                        #Maka harga pesanan akan ditambah lagi sesuai harga tersebut
    #pilihan statement di varian stuffed crust cheese
    elif crust == 'stuffed crust cheese' and size == 'personal':#Kondisi apakah benar pesanan stuffed crust cheese dengan ukuran personal
        harga += 55455                                          #Menambahkan harga pesanan(harga akan otomatis diperbarui)   
        if extra == 'yes':                                      #Jika pesanan ingin extra keju
            harga += 13636                                      #Maka harga pesanan akan ditambah lagi sesuai harga tersebut
    elif crust == 'stuffed crust cheese' and size == 'regular':#Kondisi apakah benar pesanan stuffed crust cheese dengan ukuran regular
        harga += 120910                                        #Menambahkan harga pesanan(harga akan otomatis diperbarui)
        if extra == 'yes':                                     #Jika pesanan ingin extra keju
            harga += 16364                                     #Maka harga pesanan akan ditambah lagi sesuai harga tersebut
    elif crust == 'stuffed crust cheese' and size == 'large':#Kondisi apakah benar pesanan stuffed crust cheese dengan ukuran large
        harga += 160000                                      #Menambahkan harga pesanan(harga akan otomatis diperbarui)
        if extra == 'yes':                                   #Jika pesanan ingin extra keju
            harga += 19091                                   #Maka harga pesanan akan ditambah lagi sesuai harga tersebut
    #pilihan statement di varian stuffed crust sausage
    elif crust == 'stuffed crust sausage' and size == 'personal':#Kondisi apakah benar pesanan stuffed crust sausage dengan ukuran personal
        harga += 52728                                           #Menambahkan harga pesanan(harga akan otomatis diperbarui)
        if extra == 'yes':                                       #Jika pesanan ingin extra sausage
            harga += 13636                                       #Maka harga pesanan akan ditambah lagi sesuai harga tersebut
    elif crust == 'stuffed crust sausage' and size == 'regular':#Kondisi apakah benar pesanan stuffed crust sausage dengan ukuran regular
        harga += 117273                                         #Menambahkan harga pesanan(harga akan otomatis diperbarui)
        if extra == 'yes':                                      #Jika pesanan ingin extra sausage
            harga += 16364                                      #Maka harga pesanan akan ditambah lagi sesuai harga tersebut
    elif crust == 'stuffed crust sausage' and size == 'large':#Kondisi apakah benar pesanan stuffed crust sausage dengan ukuran large
        harga += 155455                                       #Menambahkan harga pesanan(harga akan otomatis diperbarui)
        if extra == 'yes':                                    #Jika pesanan ingin extra sausage
            harga += 19091                                    #Maka harga pesanan akan ditambah lagi sesuai harga tersebut
    #pilihan statement di varian cheesy bite
    elif crust == 'cheesy bite' and size == 'personal':#Kondisi apakah benar pesanan cheesy bite dengan ukuran personal
        harga += 57273                                 #Menambahkan harga pesanan(harga akan otomatis diperbarui)
        if extra == 'yes':                             #jika pesanan ingin extra cheesy bite
            harga += 13636                             #Maka harga pesanan akan ditambah lagi sesuai harga tersebut
    elif crust == 'cheesy bite' and size == 'regular':#Kondisi apakah benar pesanan cheesy bite dengan ukuran reguler
        harga += 123637                               #Menambahkan harga pesanan(harga akan otomatis diperbarui)
        if extra == 'yes':                            #jika pesanan ingin extra cheesy bite
            harga += 16364                            #Maka harga pesanan akan ditambah lagi sesuai harga tersebut
    elif crust == 'cheesy bite' and size == 'large':#Kondisi apakah benar pesanan cheesy bite dengan ukuran large
        harga += 164546                             #Menambahkan harga pesanan(harga akan otomatis diperbarui)
        if extra == 'yes':                          #jika pesanan ingin extra cheesy bite
            harga += 19091                          #Maka harga pesanan akan ditambah lagi sesuai harga tersebut
    #pilihan statement di varian crown crust
    elif crust == 'crown crust' and size == 'personal':#Kondisi apakah benar pesanan crown crust dengan ukuran personal
        harga += 55455                                 #Menambahkan harga pesanan(harga akan otomatis diperbarui)
        if extra == 'yes':                             #Jika pesanan ingin extra keju
            harga += 13636                             #Maka harga pesanan akan ditambah lagi sesuai harga tersebut
    elif crust == 'crown crust' and size == 'regular':#Kondisi apakah benar pesanan crown crust dengan ukuran regular
        harga += 120910                               #Menambahkan harga pesanan(harga akan otomatis diperbarui)
        if extra == 'yes':                            #Jika pesanan ingin extra keju
            harga += 16364                            #Maka harga pesanan akan ditambah lagi sesuai harga tersebut
    elif crust == 'crown crust' and size == 'large':#Kondisi apakah benar pesanan crown crust dengan ukuran regular
        harga += 160000                             #Menambahkan harga pesanan(harga akan otomatis diperbarui)
        if extra == 'yes':                          #Jika pesanan ingin extra keju
            harga += 19091                          #Maka harga pesanan akan ditambah lagi sesuai harga tersebut
    # Mengembalikan harga pesanan
    return harga
