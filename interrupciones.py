import sys
def main():
    try:
        weight = input("¿Cuál es tu peso en kg? ")
        height = input("¿Cuál es tu estatura en metros? ")
        bmi = round(float(weight)/float(height)**2,2)
        val=float(weight)/float(height)**2
        print("Tu índice de masa corporal es " + str(bmi))
        print(f'El IMC es {val:.2f}')
        return 0
    except ValueError as e:
        print(f"ValueError: '{e}'") 
    except KeyboardInterrupt:
        print("\nTerminado por el usuario")
    except:
        print("Unexpected error:", sys.exc_info()[1])
        print(sys.exc_info())
        

if __name__ == '__main__':
    main()