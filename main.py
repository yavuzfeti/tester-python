import re
import PyPDF2

def parcala_pdf(pdf_dosya):
    with open(pdf_dosya, "rb") as file:
        pdf = PyPDF2.PdfReader(file)
        sayfa_sayisi = len(pdf.pages)

        sorular = []
        cevaplar = []

        for sayfa_numarasi in range(sayfa_sayisi):
            sayfa = pdf.pages[sayfa_numarasi]
            metin = sayfa.extract_text()

            soru = re.finditer(r'\b\d+\.', metin)
            for match in soru:
                soru_baslangici = match.end()-2

                soru_sonu_match = re.search(r'\bA\)', metin[soru_baslangici:])
                if soru_sonu_match is None:
                    break
                soru_sonu = soru_sonu_match.start() + soru_baslangici

                cevap_baslangici = metin.find("\nA)", soru_sonu)
                if cevap_baslangici == -1:
                    break

                cevap_baslangiclar = re.finditer(r"\n[A-E]\)", metin[cevap_baslangici:])
                cevap_sonlari = []
                for cevap_baslangic_match in cevap_baslangiclar:
                    cevap_baslangic = cevap_baslangic_match.end() + cevap_baslangici
                    cevap_sonlari.append(cevap_baslangic)

                if not cevap_sonlari:
                    break

                cevaplar_birlestirilmis = []
                for i in range(len(cevap_sonlari)):
                    if i == len(cevap_sonlari) - 1:
                        cevap_sonu = None
                    else:
                        cevap_sonu = cevap_sonlari[i + 1]
                    cevap = metin[cevap_sonlari[i]:cevap_sonu].strip()
                    cevaplar_birlestirilmis.append(cevap)

                soru = metin[soru_baslangici:soru_sonu].strip()
                cevap = "\n".join(cevaplar_birlestirilmis)

                sorular.append(soru)
                cevaplar.append(cevap)

    return sorular, cevaplar

# PDF dosyasını parçalama işlemini gerçekleştir
sorular, cevaplar = parcala_pdf("ornek.pdf")

# Sonuçları ekrana yazdır
for i in range(len(sorular)):
    print(f"SORU: {sorular[i]}\n\n\n")
    print(f"CEVAP: {cevaplar[i]}\n\n\n")
