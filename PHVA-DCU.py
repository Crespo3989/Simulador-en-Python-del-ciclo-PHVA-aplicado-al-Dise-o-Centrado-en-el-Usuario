def simulador_dcu():
    print("Iniciando proceso DCU (PHVA)...")

    satisfactorio = False

    while not satisfactorio:
        print("\nPlanificar: Analizando al usuario y sus requisitos.")
        print("Hacer: Produciendo soluciones de diseño.")

        evaluacion = input(
            "Verificar: ¿Satisface el sistema los requerimientos? (s/n): "
        ).strip().lower()

        if evaluacion == "s":
            print("Actuar: Desarrollo exitoso.")
            satisfactorio = True
        elif evaluacion == "n":
            print("Actuar: Iterando el ciclo de diseño.")
        else:
            print("Respuesta no válida. Escriba 's' o 'n' para evaluar nuevamente.")

    print("Proceso DCU-PHVA finalizado.")


simulador_dcu()