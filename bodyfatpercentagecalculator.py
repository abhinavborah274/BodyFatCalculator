import math

def main():
    print("Enter M for Male, F for Female")
    x = input()
    print("Enter weight in kg:")
    a = float(input())
    print("Enter height in cm:")
    b = float(input())
    print("Enter neck circumference in cm:")
    c = float(input())
    print("Enter waist circumference in cm:")
    d = float(input())
    heightlog = float(math.log(b, 10))
    bmi = float(a/((b*b)/(100*100)))
    if (str(x) == "M") or (str(x) == "m"):
        print("Subject is Male.")
        maleterm = float(math.log((d-c), 10))
        bf1 = float((495/(1.0324-(0.19077*maleterm)+(0.15456*heightlog)))-450)
        print("BMI is : ", bmi)
        print("Body Fat Percentage is : ", bf1)
        fm1 = (bf1*a)/100
        lm1 = a - fm1
        print("Fat Mass: ", fm1)
        print("Lean Mass: ", lm1)
    elif (str(x) == "F") or (str(x) == "f"):
        print("Subject is Female.")
        femaleterm = float(math.log((d+c), 10))
        bf2 = float((495/(1.29579-(0.35004*femaleterm)+(0.22100*heightlog)))-450)
        print("BMI is : ", bmi)
        print("Body Fat Percentage is : ", bf2)
        fm2 = (bf2*a)/100
        lm2 = a - fm2
        print("Fat Mass: ", fm2)
        print("Lean Mass: ", lm2)
    else:
        print("Incorrect Input")
    return 0
    
    
if __name__ == '__main__' :
    main()