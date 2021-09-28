n=input()
card=[0]*9

card_6n9=0

for i in n:
    if(i=='6' or i=='9'):
        card_6n9+=1
    else:
        card[(int(i))]+=1

if (card_6n9 %2==0):
    card_6n9 =card_6n9//2
else:
    card_6n9=card_6n9//2 +1

card[6]=card_6n9

print(max(card))