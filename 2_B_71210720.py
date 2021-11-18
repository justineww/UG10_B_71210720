x=int(input("Masukkan besar RSI:"))
y=str(input("Masukkan kondisi MACD:"))
if x >=70 and y =="death-cross":
    print("RSI lebih dari sama dengan 70 dan MACD Death-cross, saatnya jual")
elif x <=30 and y =="golden-cross":
    print("RSI kurang dari sama dengan 30 dan MACD Golden-cross, saatnya beli")
elif x >=70 and y =="golden-cross":
    print("RSI lebih dari sama dengan 70 dan MACD Golden-cross, Tunggu MACD sampai death-cross")
elif x <=30 and y =="death-cross":
    print("RSI kurang dari sama dengan 30 dan MACD Death-cross, Tunggu MACD sampai golden-cross")
else:
    print("RSI berada di area 31 - 69, Bukan saatnya membeli maupun menjual")