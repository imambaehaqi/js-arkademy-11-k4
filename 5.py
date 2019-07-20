def evenSum(N):
    if (N < 2):
        return 0

    AngkaSebe = 0
    AngkaA = 2
    hasil = AngkaSebe + AngkaA

    while (AngkaA < N):
        AngkaSel = 4 * AngkaA + AngkaSebe
        
        if (AngkaSel > N):
            break

        AngkaSebe = AngkaA
        AngkaA = AngkaSel
        hasil += AngkaA

    return hasil

def oddSum(N):
    AngkaSebe = 1
    AngkaA = 1
    hasil = 0
    
    while (AngkaA < N):
        if (AngkaA % 2 != 0):
            hasil += AngkaA

        AngkaA += AngkaSebe
        AngkaSebe = AngkaA - AngkaSebe

    return hasil

print(evenSum(1000))
print(oddSum(100))
print(oddSum(1000))