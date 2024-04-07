# Generated first 10,002 fibonacci, the final 10,000 need to be found by calculationnumnbers
Numbers = [0, 1]

lim = 10000

with open('../Storage/10_000_fibo.txt', 'w') as file:
    file.write("0\n1")
    for number in range(lim):
        Newest = Numbers[-1] + Numbers[-2]
        Numbers.append(Newest)
        file.write(f"\n{Newest}")
    
