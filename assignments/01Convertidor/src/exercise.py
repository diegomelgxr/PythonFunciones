# Escribe tus funciones abajo de esta línea
#Opciones
    print('1. pies a cm, 2. pulgadas a cm, 3. yardas a cm')
    opcion = int(input('Introduce una opcion: '))

    #Funciones
    def ft_a_cm(ft):
      a = (ft)*30.48
      return a

    def in_a_cm(inc):
      b = (inc)*2.54
      return b

    def yd_a_cm(yd):
      c = (yd)*91.44
      return c
    cantidad = int(input('Introduce la cantidad: '))
    #Condiciones
    if opcion == 1:
      a = ft_a_cm(cantidad)
      print(a)

    elif opcion == 2:
      b = in_a_cm(cantidad)
      print(b)

    elif opcion == 3:
      c = yd_a_cm(cantidad)
      print(c)

    elif opcion >= 4:
      print('Error')

    elif opcion <= 0:
      print('Error')

def main():
    # Escribe tu código abajo de esta línea
    

if __name__ == '__main__':
    main()
