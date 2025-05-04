import random
hp=100

while hp>0:
    damage=random.randint(1,20)
    print("おのざきは"+str(damage)+"のダメージを受けた！")
    hp=hp-damage
print("おのざきはしんだ")
print("残りHP:",hp)