name = str(input("その子の名前を入力してください。"))  #全て１０点満点です.
face = int(input("顔の可愛さを入力してください。"))
stlye = int(input("スタイルの良さを入力してください。") )
oppaisize = int(input("おっぱいの大きさを入力してください。"))
personality = int(input("性格の良さを入力してください。"))
total = face + stlye + oppaisize + personality
if total >= 35:
    print("総合スコアは", total, "点です。", name, "は最高の女の子です。")
elif total >=30 and total < 35:
    print("総合スコアは", total, "点です。", name, "は良い女の子です。")
elif total >= 25 and total < 30:
    print("総合スコアは", total, "点です。", name, "はそこそこの女の子です。")
elif total >= 20 and total < 25:
    print("総合スコアは", total, "点です。", name, "は普通の女の子です。")
elif total >= 15 and total < 20:
    print("総合スコアは",total,"点です。",name,"は付き合うには少ししゃばい女の子です。")
else:
    print("総合スコアは",total,"点です。",name,"は付き合うには到底無理な女の子です。何なら付き合ったらいじられるでしょう。")
