import sys

def poryadok_v_pleyliste():
    # Chitaem kolichestvo pesen n
    vhod_n = sys.stdin.readline()
    if not vhod_n:
        return
    
    n_pesen = int(vhod_n.strip())
    
    # Sozdaem spisok dlya hraneniya nazvaniy
    spisok_nazvaniy = []
    
    # Sobiraem vse pesni v spisok
    for _ in range(n_pesen):
        nazvanie_pesni = sys.stdin.readline().strip()
        if nazvanie_pesni:
            spisok_nazvaniy.append(nazvanie_pesni)
            
    # Sortiruem po alfavitu (v Python eto standart dlya strok)
    otsortirovanniy_spisok = sorted(spisok_nazvaniy)
    
    # Vivodim kazhduyu pesnyu na novoy stroke
    for pesnya in otsortirovanniy_spisok:
        print(pesnya)

if __name__ == "__main__":
    poryadok_v_pleyliste()