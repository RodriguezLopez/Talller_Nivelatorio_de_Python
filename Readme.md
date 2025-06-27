# Sistema de Gestión de Estudiantes

## 📚 Manual de Usuario

¡Bienvenido al Sistema de Gestión de Estudiantes! Este programa, desarrollado en Python, te permite administrar de forma sencilla los registros académicos de los estudiantes de una institución educativa.

### ✨ Características Principales

* **Registro de estudiantes:** Guarda el nombre, identificación, edad y notas de cada estudiante.
* **Consulta:** Busca la información de un estudiante por su número de identificación.
* **Actualización de notas:** Modifica las notas de un estudiante existente.
* **Eliminación:** Borra un registro de estudiante del sistema.
* **Listado general:** Visualiza todos los estudiantes registrados y sus promedios.
* **Validaciones robustas:** El programa valida las entradas de usuario para asegurar la integridad de los datos.

### 🚀 Uso del Programa

Para usar el sistema, sigue estos sencillos pasos:

1.  **Ejecución:**
    Abre una terminal o consola en la carpeta donde se encuentra el archivo `gestion_estudiantes.py` y ejecútalo con el siguiente comando:
    ```bash
    python gestion_estudiantes.py
    ```

2.  **Menú Principal:**
    Al iniciar, el programa te mostrará un menú interactivo con las siguientes opciones:
    ```
    ========================================
          SISTEMA DE GESTIÓN DE ESTUDIANTES
    ========================================
    1. Registrar estudiante
    2. Consultar estudiante
    3. Actualizar notas
    4. Eliminar estudiante
    5. Ver todos los estudiantes
    6. Salir
    ========================================
    ```
    Simplemente ingresa el número de la opción que deseas ejecutar y presiona `Enter`.

### 📝 Guía de Opciones

Aquí te explicamos cada una de las funcionalidades del menú:

#### **1. Registrar estudiante**
* Ingresa el número `1` y presiona `Enter`.
* El programa te pedirá que ingreses la **identificación** (debe ser un número único), el **nombre** y la **edad** del estudiante.
* Luego, te solicitará las **notas**. Debes ingresar al menos 3 notas (valores entre 0.0 y 5.0). Para terminar de ingresar notas al actualizar, presiona `f`.
* El sistema validará que los datos sean correctos y te notificará si el registro fue exitoso.

#### **2. Consultar estudiante**
* Ingresa el número `2` y presiona `Enter`.
* Se te pedirá la **identificación** del estudiante que deseas consultar.
* Si el estudiante existe, verás su nombre, edad, lista de notas y su promedio.
* Si no existe, recibirás un mensaje de error.

#### **3. Actualizar notas**
* Ingresa el número `3` y presiona `Enter`.
* Se te pedirá la **identificación** del estudiante cuyas notas quieres modificar.
* Si se encuentra el estudiante, podrás ingresar una **nueva lista de notas**. Ingresa `f` cuando hayas terminado de agregar notas (recuerda que el mínimo es 3).
* Las notas del estudiante se sobrescribirán con las nuevas.

#### **4. Eliminar estudiante**
* Ingresa el número `4` y presiona `Enter`.
* Ingresa la **identificación** del estudiante que deseas eliminar.
* El registro será borrado permanentemente del sistema.

#### **5. Ver todos los estudiantes**
* Ingresa el número `5` y presiona `Enter`.
* El sistema te mostrará un listado claro con la identificación, nombre y promedio de cada estudiante registrado.
* Si no hay estudiantes, el sistema te lo informará.

#### **6. Salir**
* Ingresa el número `6` para salir del programa de forma segura.

---
**¡Esperamos que este sistema te sea de gran utilidad en tu gestión diaria!**