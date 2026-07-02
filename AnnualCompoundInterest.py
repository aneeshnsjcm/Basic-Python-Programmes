#Annual Compound Interest
p=input('principal amount : ')
n=input('time period in years :')
r=input('rate of interest pre annum: ')
ta=float(p)*(1+(float(r)/100))**float(n)
i=ta-float(p)
print('Total Interest is ', i)
