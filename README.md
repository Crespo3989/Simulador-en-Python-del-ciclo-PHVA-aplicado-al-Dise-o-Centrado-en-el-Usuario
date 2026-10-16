# Simulador DCU-PHVA

## Descripción

Este programa de consola representa la aplicación del ciclo **PHVA** (*Planificar, Hacer, Verificar y Actuar*) dentro del **Diseño Centrado en el Usuario (DCU)**. La evaluación determina si el sistema cumple los requisitos; si no los cumple, el proceso inicia una nueva iteración.

## Relación entre DCU y PHVA

| Etapa PHVA | Fase o actividad DCU |
|---|---|
| **Planificar** | Comprender el contexto (CECU) e identificar usuarios, tareas, limitaciones y requisitos (ERU). |
| **Hacer** | Proponer y producir soluciones de diseño. |
| **Verificar** | Evaluar la solución (EDR) frente a los requisitos establecidos. |
| **Actuar** | Finalizar si cumple los requisitos o iterar el ciclo para corregir el diseño. |

## Requisitos

- Python 3 instalado.
- No requiere instalar paquetes adicionales.

## Instalación y ejecución

1. Guarda el código del simulador en un archivo llamado `simulador_dcu.py`.
2. Abre una terminal en la carpeta donde guardaste el archivo.
3. Ejecuta:

```bash
python simulador_dcu.py
```

En algunos sistemas, el comando puede ser:

```bash
python3 simulador_dcu.py
```

## Código del simulador

```python
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


if __name__ == "__main__":
    simulador_dcu()
```

## Funcionamiento

- Si se ingresa **`s`**, el sistema confirma el desarrollo exitoso y termina.
- Si se ingresa **`n`**, informa que el diseño debe iterar y vuelve a Planificar.
- Si se ingresa otra respuesta, solicita nuevamente una entrada válida.

## Ejemplo de ejecución

```text
Iniciando proceso DCU (PHVA)...

Planificar: Analizando al usuario y sus requisitos.
Hacer: Produciendo soluciones de diseño.
Verificar: ¿Satisface el sistema los requerimientos? (s/n): n
Actuar: Iterando el ciclo de diseño.

Planificar: Analizando al usuario y sus requisitos.
Hacer: Produciendo soluciones de diseño.
Verificar: ¿Satisface el sistema los requerimientos? (s/n): s
Actuar: Desarrollo exitoso.
Proceso DCU-PHVA finalizado.
```

