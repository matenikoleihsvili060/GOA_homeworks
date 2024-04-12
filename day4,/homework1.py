
"""day4:
1) module1 quiz-ის ჩათვლით

2) შექმენით რამოდენიმე ცვლადი(თქვენი სახელი, თქვენი გვარი, თქვენი ასაკი, ასევე გამოითვალეთ რამდენი წლის იქნებით 10 წლის       შემდეგ და ერთ გრძელ წინადადებაში დაპრინტეთ
Image

გაიხსენეთ turtle, დახაზეთ 3 სახლი, ეზოთი, მზედა ვარსკვლავები ( რაც უფრო მეტს იშრომებთ, უფრო დაგიფასდებათ )"""


from turtle import* 

penup()
goto(-670,0)
pendown()

width(4)

color("green")
begin_fill()
forward(1360)
end_fill()

penup()
goto(500,0)
pendown()

color("maroon")

left(90)
forward(200)
right(90)
forward(150)
right(90)
forward(200)

penup()
goto(550,0)
pendown()

color("red")
begin_fill()
left(180)
forward(70)
right(90)
forward(50)
right(90)
forward(70)
end_fill()

penup()
goto(510,170)
pendown()

color("red")
begin_fill()
forward(30)
left(90)
forward(40)
left(90)
forward(30)
left(90)
forward(40)
end_fill()

penup()
goto(600,170)
pendown()

color("red")
begin_fill()
left(90)
forward(30)
left(90)
forward(40)
left(90)
forward(30)
left(90)
forward(40)
end_fill()

penup()
goto(650,200)
pendown()

color("maroon")
begin_fill()
right(45)
forward(110)
left(92)
forward(110)
end_fill()

penup()
goto(480,0)
pendown()

right(47)
right(90)

color("maroon")
forward(200)
left(90)
forward(150)
left(90)
forward(200)

penup()
goto(380,0)
pendown()

color("blue")
begin_fill()
right(180)
forward(70)
right(90)
forward(50)
right(90)
forward(70)
end_fill()
 
penup()
goto(340,170)
pendown() 

color("blue")
begin_fill()
forward(30)
left(90)
forward(40)
left(90)
forward(30)
left(90)
forward(40)

penup()
goto(430,170)
pendown()

left(90)
forward(30)
left(90)
forward(40)
left(90)
forward(30)
left(90)
forward(40)
end_fill()

penup()
goto(480,200)
pendown()

color("blue")
begin_fill()
right(45)
forward(110)
left(92)
forward(110)
end_fill()

penup()
goto(310,0)
pendown()

right(47)
right(90)

color("maroon")

forward(200)
left(90)
forward(150)
left(90)
forward(200)

penup()
goto(210,0)
pendown()

color("aqua")
begin_fill()
left(180)
forward(70)
right(90)
forward(50)
right(90)
forward(70)
end_fill()

penup()
goto(170,170)
pendown()

color("aqua")
begin_fill()
forward(30)
left(90)
forward(40)
left(90)
forward(30)
left(90)
forward(40)

penup()
goto(260,170)
pendown()

left(90)
forward(30)
left(90)
forward(40)
left(90)
forward(30)
left(90)
forward(40)
end_fill()

penup()
goto(310,200)
pendown()

color("aqua")
begin_fill()
right(45)
forward(110)
left(92)
forward(110)
end_fill()

penup()
goto(-150,0)
pendown()

color("silver")
left(20)
forward(600)

penup()
goto(-350,0)
pendown()

forward(600)

penup()
goto(-250,-30)
pendown()

forward(100)

penup()
goto(-350,-260)
pendown()

forward(100)

penup()
goto(-353,0)
pendown()

color("green")
begin_fill()
forward(700)
right(60)
forward(350)
right(90)
forward(700)
end_fill()

left(180)

penup()
goto(-147,0)
pendown()

color("green")
begin_fill()
right(30)
forward(700)
left(93)
forward(1400)
left(90)
forward(1210)
end_fill()

color("brown")
penup()
goto(100,0)
pendown()

begin_fill()
left(20)
forward(120)

penup()
goto(100,0)
pendown()

left(90)
forward(30)

penup()
goto(70,0)
pendown()

right(90)
forward(120)
right(90)
forward(30)

end_fill()

exitonclick()