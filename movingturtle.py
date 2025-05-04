from turtle import*
shape("turtle")
speed(200)
col = ("red","blue","green","yellow","plum","orange","pink","purple","brown","black")
for random in range(72):
    import random
    color(random.choice(col) )
    circle(100)
    left(5)
done()
