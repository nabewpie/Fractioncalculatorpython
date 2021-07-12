import numpy

def fractioncalc(numer1, denom1, numer2, denom2):
    if denom1 == denom2:
        RESULT = print(numer1 + numer2 ,  "/" , denom1)
    else:
        lcm = numpy.lcm(denom1, denom2)

        print(lcm)
        tomultfract = lcm/denom1
        tomultfract2 = lcm / denom2
        tomultfractdenom1 = tomultfract * denom1
        tomultfractnumer1 = tomultfract * numer1
        tomultfractdenom2 = tomultfract2 * denom2
        tomultfractnumer2 = tomultfract2 * numer2
        resultfract = print(tomultfractnumer1 + tomultfractnumer2 , "/" , tomultfractdenom2)

fractioncalc(int(input("NUMERATOR 1: ")), int(input("DENOMINATOR 1: ")), int(input("NUMERATOR 1: ")), int(input("DENOMINATOR 2: ")))
