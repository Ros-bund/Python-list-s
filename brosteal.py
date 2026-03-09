import sys

def ochistit_kod_bratstva():
    # Chitaem pervuyu stroku, gde hranitsya kolichestvo
    pervaya_stroka = sys.stdin.readline()
    if not pervaya_stroka:
        return
    
    # Izvlekaem chislo n, ubiraya reshetku
    n_strok = int(pervaya_stroka.strip('#').strip())

    for _ in range(n_strok):
        tekushaya_stroka = sys.stdin.readline()
        if not tekushaya_stroka:
            break
        
        # Udalyam simvol perenosa, chtoby ne meshal
        strok_bez_perenosa = tekushaya_stroka.rstrip('\n\r')
        
        # Ishem gde nachinaetsya virusniy kommentariy
        poziciya_kommentariya = strok_bez_perenosa.find('#')
        
        if poziciya_kommentariya != -1:
            # Otrezaem vse lishnee
            rezultat = strok_bez_perenosa[:poziciya_kommentariya]
        else:
            # Esli reshetki net, ostavlyaem kak est
            rezultat = strok_bez_perenosa
            
        # Pechataem rezultat bez probelov v konce
        print(rezultat.rstrip())

if __name__ == "__main__":
    ochistit_kod_bratstva()