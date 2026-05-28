# Integración y consulta avanzada de datos genómicos y fenotípicos clínicos en una infraestructura Beacon FHIR interoperable en un entorno hospitalario

## Descripción

Este repositorio contiene el material desarrollado durante la realización del Trabajo Fin de Máster (TFM) centrado en la integración, transformación y consulta de datos genómicos y fenotípicos clínicos mediante una infraestructura interoperable basada en **Beacon v2**.

El proyecto tiene como objetivo facilitar la interoperabilidad y el acceso estandarizado a datos clínicos y genómicos dentro de un entorno hospitalario, permitiendo consultas avanzadas compatibles con los estándares internacionales de intercambio de información biomédica.

---


## Estructura del repositorio

```bash
.
├── Consultas/
├── beacon2-pi-api/
├── DATOS_NECESARIOS_OMOP_completo.pdf
├── OMOP_mappings.pdf
├── beacon_logs.txt
├── seleccion_individuos.py
└── README.md
```

---

## Contenido del repositorio

### `Consultas/`
Directorio que contiene consultas realizadas durante el desarrollo y validación del sistema.

### `beacon2-pi-api/`
Carpeta que incluye los archivos relacionados con la implementación de **Beacon v2** modificados durante el desarrollo del TFM.

La estructura de directorios se ha mantenido equivalente a la del repositorio oficial de Beacon con el fin de:

- Facilitar la localización de los archivos modificados.
- Mantener la trazabilidad de los cambios realizados.
- Simplificar futuras integraciones o actualizaciones.

### `seleccion_individuos.py`
Script utilizado para la selección de los individuos incluidos en el estudio.

### `DATOS_NECESARIOS_OMOP_completo.pdf`
Documento que recopila las tablas, campos y formatos del modelo **OMOP** necesarias.

### `beacon_logs.txt`
Documento que contiene los logs en los que se especifican los valores invalidos recogidos en la coleccion *individuals*. 

### `OMOP_mappings.pdf`
Documento que contiene los mapeos y equivalencias empleados durante la transformación de datos entre el modelo **OMOP** y los formatos compatibles con **Beacon v2**.

---

## Tecnologías y estándares utilizados

- **Beacon v2**
- **OMOP Common Data Model**
- **Python**
- Integración de datos clínicos y genómicos
- Infraestructuras interoperables hospitalarias

---

## Reproducibilidad

Este repositorio tiene como finalidad facilitar la reproducibilidad del trabajo realizado durante el TFM, proporcionando:

- Scripts utilizados en el procesamiento de datos.
- Documentación técnica.
- Mapeos y transformaciones de datos.
- Modificaciones realizadas sobre la implementación Beacon.

---

## Contexto académico

Trabajo desarrollado como parte de un Trabajo Fin de Máster enfocado en interoperabilidad biomédica, integración de datos clínicos y sistemas de información genómica.



