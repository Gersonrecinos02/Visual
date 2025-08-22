# Diagrama de flujo: Año bisiesto

```mermaid
graph TD
    A[Inicio] --> B[Leer anio]
    B --> C{anio % 4 == 0}
    C -- No --> Z1[Mostrar: No es bisiesto] --> F[Fin]
    C -- Si --> D{anio % 100 == 0}
    D -- No --> E[Mostrar: Es bisiesto] --> F
    D -- Si --> G{anio % 400 == 0}
    G -- Si --> H[Mostrar: Es bisiesto] --> F
    G -- No --> I[Mostrar: No es bisiesto] --> F
