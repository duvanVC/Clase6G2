class Mascota:

    def __init__(self):
        self.__nombre = " "
        self.__historia = ""
        self.__tipo = " "
        self.__peso = " "
        self.__fecha_ingreso = " "
        self.__medicamento = {}

    def verNombre(self):
        return self.__nombre

    def verHistoria(self):
        return self.__historia

    def verTipo(self):
        return self.__tipo

    def verPeso(self):
        return self.__peso

    def verFecha(self):
        return self.__fecha_ingreso

    def ver_Medicamento(self):
        return self.__medicamento

    def asignarNombre(self, n):
        self.__nombre = n

    def asignarHistoria(self, nh):
        self.__historia = nh

    def asignarTipo(self, t):
        self.__tipo = t

    def asignarPeso(self, p):
        self.__peso = p

    def asignarFecha(self, f):
        self.__fecha_ingreso = f

    def asignarMedicamento(self, n):
        self.__medicamento[n.verNombre()] = n.verDosis()


class sistemaV:
    def __init__(self):
        self.__lista_felinos = {}
        self.__lista_caninos = {}

    def verificarExiste(self, historia):
        if historia in self.__lista_felinos:
            return True
        if historia in self.__lista_caninos:
            return True
        # solo luego de haber recorrido todo el ciclo se retorna False
        return False

    def verNumeroMascotas(self):
        return len(self.__lista_felinos) + len(self.__lista_caninos)

    def ingresarFelino(self, mascota):
        self.__lista_felinos[mascota.verHistoria()] = mascota

    def ingresarCanino(self, mascota):
        self.__lista_caninos[mascota.verHistoria()] = mascota

    def verFechaIngreso(self, historia):
        # busco la mascota y devuelvo el atributo solicitado
        # return self.__lista_caninos.get(historia)
        if historia in self.__lista_caninos:
            return self.__lista_caninos[historia].verFecha()
        if historia in self.__lista_felinos:
            return self.__lista_felinos[historia].verFecha()
        return None
        # for masc in self.__lista_caninos:
        #     if historia == masc:
        #         return masc.verFecha()
        # for masc in self.__lista_felinos:
        #     if historia == masc:
        #         return masc.verFecha()
        # return None

    def verMedicamento(self, historia):
        # busco la mascota y devuelvo el atributo solicitado
        if historia in self.__lista_caninos:
            return self.__lista_caninos[historia].verMedicamento()
        if historia in self.__lista_caninos:
            return self.__lista_felinos[historia].verMedicamento()
        return None

    def eliminarMascota(self, historia):
        if historia in self.__lista_caninos:
            del self.__lista_caninos[historia]
            return True
        if historia in self.__lista_caninos:
            del self.__lista_felinos[historia]
            return True
        return False
        # for masc in self.__lista_caninos:
        #     if historia == masc.verHistoria():
        #         # del self.__lista_mascotas[masc]
        #         self.__lista_caninos.remove(masc)  # opcion con el pop
        #         return True  # eliminado con exito
        # for masc in self.__lista_felinos:
        #     if historia == masc.verHistoria():
        #         # del self.__lista_mascotas[masc]
        #         self.__lista_felinos.remove(masc)  # opcion con el pop
        #         return True
        # return False


class Medicamento:
    def __init__(self):
        self.__nombre = ""
        self.__dosis = 0

    def verNombre(self):
        return self.__nombre

    def verDosis(self):
        return self.__dosis

    def asignarNombre(self, med):
        self.__nombre = med

    def asignarDosis(self, med):
        self.__dosis = med
