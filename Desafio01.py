#  Las actividades designadas como Desafíos (o Desafíos de Programación) son retos de programación, mediante los cuales se solicita a los alumnos plantear un script / programa en Python que resuelva uno o más problemas dados, procesar ciertos datos fijos (iguales para todos los alumnos) con esos programas, y luego, simplemente, subir al aula virtual los resultados que haya obtenido para que sean validados. Los alumnos NO DEBEN SUBIR los códigos fuente de sus programas: solo deben subir las respuestas que hayan obtenido al correr sus programas sobre los lotes de datos indicados. Cuando haya vencido el plazo para subir las respuestas, los profesores publicarán los programas cuya estructura se sugiere como solución para el desafío, de forma que los alumnos puedan (por sus propios medios) controlar y comparar contra sus propias soluciones.

# Este primer Desafío es sencillo y lo asumimos como una forma de "entrada en calor" para enfrentar este tipo de evaluaciones. El enunciado del problema (o consigna) a resolver es el siguiente:

# Desarrolle un programa o script Python que permita cargar por teclado un número entero que representa la  cantidad de segundos que pasaron desde un evento dado.  El programa debe convertir esa cantidad de segundos  a la cantidad de horas, minutos y segundos que transcurrieron. Por ejemplo, si la cantidad de segundos  ingresada es 4452 deberá mostrar un mensaje que informe que el tiempo transcurrido fue de 1 hora, 14 minutos  y 12 segundos.

# Su tarea: cuando haya desarrollado el programa pedido, ejecútelo cuatro veces, y compruebe los resultados que obtenga al cargar las siguientes cantidades de segundos:

# Primera ejecución - Cantidad de segundos a ingresar:  7832
# Segunda ejecución - Cantidad de segundos a ingresar:  18993
# Tercera ejecución - Cantidad de segundos a ingresar:  2475
# Cuarta ejecución - Cantidad de segundos a ingresar: 25213
# Cuando haya obtenido los resultados, ingrese en este mismo desafío, y allí se le pedirá que registre los resultados en formato "horas:minutos:segundos". Tomando el mismo ejemplo que se indica en el enunciado del problema, si la cantidad de segundos ingresada es 4452, entonces usted deberá subir un resultado de la forma 1:14:12 sin espacios en blanco, sin comillas, y usando estrictamente el caracter : (dos puntos) para separar una parte de la otra. Cualquier error que cometa en el formato de su respuesta, podrá hacer que la solución subida se considere incorrecta, así que hágalo con mucho cuidado. Si la cantidad de horas o de minutos o de segundos final fue igual a cero, registre un cero en esa posición. Por ejemplo, si usted obtuvo una respuesta de 0 horas, 23 minutos y 0 segundos, entonces registre la siguiente respuesta: 0:23:0 cuando le sea requerida.

# Además, el desafío incluye al final una quinta consigna o pregunta adicional, en la cual se le pedirá hacer un programa que haga el proceso inverso: deberá tomar tres datos, que serán el valor en horas, el valor en minutos y el valor en segundos transcurridos desde un evento dado, y su programa deberá calcular la cantidad total de segundos a partir de esos datos. Por ejemplo, si los datos ingresados fuesen: horas = 4, minutos = 36 y segundos = 8 entonces el resultado a obtener es que la cantidad total de segundos es 16568.

# Es completamente obvio que cualquier alumno puede calcular las respuestas pedidas sin hacer un programa Python, usando en cambio una calculadora o haciendo cuentas con papel y lápiz. También es completamente obvio que un alumno puede simplemente copiarle las respuestas a algún compañero que tenga una idea equivocada de lo que significa la palabra "compañerismo". Los docentes no podemos controlar si están haciendo su trabajo honestamente o no. Hacer su trabajo con honestidad y dedicación es una cuestión de honor hacia ustedes mismos, y de respeto hacia el profesional que serán dentro de algunos años. Y también es completamente obvio que si nunca hacen un esfuerzo por tratar de hacer cada actividad en forma correcta y completa, luego tendrán serios problemas cuando tengan que hacer los parciales (en los que los docentes sí controlamos cada cosa que hacen...)

# Cada alumno tendrá un total de 5(cinco) intentos disponibles hasta subir las respuestas correctas. Cuando haya agotado las cinco posibilidades, o bien si logra registrar las respuestas correctas antes de usar sus cinco intentos, entonces la nota final que le corresponderá por este desafío será la mayor nota que haya obtenido en los intentos que haya usado.

# Cuando haya vencido la fecha final para realizar este desafío, será publicada en el aula virtual la solución de programación sugerida por los profesores (es decir, será publicado el programa Python para resolver el problema).


# TODO  Desarrolle un programa o script Python que permita cargar por teclado un número entero que representa la  cantidad de segundos que pasaron desde un evento dado.  El programa debe convertir esa cantidad de segundos  a la cantidad de horas, minutos y segundos que transcurrieron. Por ejemplo, si la cantidad de segundos  ingresada es 4452 deberá mostrar un mensaje que informe que el tiempo transcurrido fue de 1 hora, 14 minutos  y 12 segundos.

# TODO*  Además, el desafío incluye al final una quinta consigna o pregunta adicional, en la cual se le pedirá hacer un programa que haga el proceso inverso: deberá tomar tres datos, que serán el valor en horas, el valor en minutos y el valor en segundos transcurridos desde un evento dado, y su programa deberá calcular la cantidad total de segundos a partir de esos datos. Por ejemplo, si los datos ingresados fuesen: horas = 4, minutos = 36 y segundos = 8 entonces el resultado a obtener es que la cantidad total de segundos es 16568.


segs = int(input("Ingrese la cantidad de segundos: "))

horas = segs//3600
segs = segs % 3600
minutos = segs // 60
segs = segs % 60


print('La cantidad de horas es: ', horas, '\nLa cantidad de minutos es: ',
      minutos, '\nLa cantidad de segundos es: ', segs)


hours = int(input('Ingrese las horas transcurridas: '))
minutes = int(input('Ingrese los minutos transcurridos: '))
secods = int(input('Ingrese los segundos transcurridos: '))


a = hours * 3600
b = minutes * 60
c = secods

print('La cantidad de segundos transcurridos es: ', a + b + c)
