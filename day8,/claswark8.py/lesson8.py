target_kill = 50
target_save = 100

kill = int(input(" how many people have you killed ? "))
alive = int(input(" how many people have you save ? "))

print(kill == target_kill and alive == target_save )
print(kill == target_kill or alive == target_save )
print(kill >= target_kill and alive >= target_save )
print(kill >= target_kill or alive >= target_save )