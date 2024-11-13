def buscarPacientes(pacientes,motivoDeAsistencia): 
    legajoBuscar = int(input("Ingrese el legajo que desea buscar, -1 para finalizar"))
    while legajoBuscar != -1 and legajoBuscar < 1000 or legajoBuscar > 9999: 
        legajoBuscar = int(input("Ingrese numero de legajo valido del paciente, -1 para finalizar "))
    
    while legajoBuscar != -1: 
        contador = 0
        urgencia = 0
        consulta = 0
        for i in range(len(pacientes)): 
            if pacientes[i] == legajoBuscar: 
                motivo = motivoDeAsistencia[i]
                if motivo == 1: 
                    consulta += 1
                else: 
                    urgencia += 1

        print("El paciente ", legajoBuscar, "fue atendido un total de ", consulta + urgencia, "veces,", consulta, "veces por consulta y ", urgencia, "veces por urgencia")

        legajoBuscar = int(input("Ingrese el legajo que desea buscar, -1 para finalizar "))
        while legajoBuscar != -1 and legajoBuscar < 1000 or legajoBuscar > 9999: 
            legajoBuscar = int(input("Ingrese numero de legajo valido del paciente, -1 para finalizar "))

def recibirPacientes():
    motivoDeAsistencia = []
    pacientes = [] 

    pacientesUrgencia = []
    pacientesConsulta = []

    legajo = int(input("Ingrese numero de legajo del paciente, -1 para finalizar "))
    while legajo != -1 and legajo < 1000 or legajo > 9999: 
        legajo = int(input("Ingrese numero de legajo valido del paciente, -1 para finalizar "))
         
    while legajo != -1:  
        motivo = int(input("Ingrese motivo de asistencia, consulta (1), urgencia (0)"))
        while motivo != 1 and motivo != 0: 
            motivo = int(input("Ingrese motivo de asistencia, consulta (1), urgencia (0)"))

        if motivo == 1: 
            pacientesConsulta.append(legajo)
        else:
            pacientesUrgencia.append(legajo)

        pacientes.append(legajo)
        motivoDeAsistencia.append(motivo)

        legajo = int(input("Ingrese numero de legajo del paciente, -1 para finalizar "))
        while legajo != -1 and legajo < 1000 or legajo > 9999: 
            legajo = int(input("Ingrese numero de legajo valido del paciente, -1 para finalizar "))
        
    print("Pacientes atendidos por urgencia, en orden de llegada: ", pacientesUrgencia, "\n", "pacientes atendidos por consulta, en orden de llegada: ", pacientesConsulta)
    return(buscarPacientes(pacientes,motivoDeAsistencia))



recibirPacientes()