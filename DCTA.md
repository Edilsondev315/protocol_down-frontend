# 🚨 Directiva de contexto técnico y arquitectura - PROTOCOL_DOWN

Hola IA. Vas a ser mi asistente de programación para desarrollar un módulo específico dentro de un proyecto universitario colaborativo llamado **PROTOCOL_DOWN**.

Para garantizar que el código que generes encaje perfectamente con el trabajo de los demás programadores sin romper nada, **DEBES SEGUIR ESTAS REGLAS OBLIGATORIAS**:

---

## 1. Regla fundamental de trabajo (Arquitectura modular)

- **Un único archivo por persona:** No compartimos código fuente ni editamos los archivos de los demás compañeros.
- **Desacoplamiento total:** Todo el código que generes debe estar encapsulado en **clases o funciones exportables** dentro de mi archivo.
- **Prohibido código global ejecutable:** No coloques bucles while ni inicializaciones globales fuera de clases o funciones.
- **Bloque de ejecución individual:** Si generas código de prueba para ejecutar mi archivo de forma aislada, DEBES colocarlo estrictamente dentro del siguiente bloque:

```python
if __name__ == "__main__":
    # Código de prueba independiente aquí
    pass
```

---

## 2. Estándares técnicos del proyecto

- **Lenguaje y librería:** Python 3 + Pygame puro, sin motores gráficos externos.
- **Resolución base de pantalla:** 800 x 600 píxeles a 60 FPS fijos.
- **Nombres de variables de coordenadas:** Utilizar estrictamente x e y, en minúsculas, como flotantes o enteros, para posiciones en el espacio.
- **Estructura de datos compartida:** Toda información intercambiada entre mi archivo y el servidor o demás módulos debe usar diccionarios de Python o JSON con las siguientes claves estándar:

  - **jugador_id:** Identificador del cliente, por ejemplo: "P1".
  - **x, y:** Posición actual en el mapa.
  - **salud:** Valor numérico entre 0 y 100.
  - **dano_boss:** Daño acumulado por el jugador.

---

## 3. ¿Cómo se conectará todo al final? (Visión del proyecto)

Al final del desarrollo, un archivo principal orquestador, main.py, importará las clases que tú y yo creemos en este script, junto con las de los demás integrantes, para hacerlas funcionar en conjunto:

```text
               [ server_main.py ] (Servidor Sockets LAN)
                           ▲
                           │ (JSON Red)
                           ▼
                     [ main.py ]  <-- (Orquestador Central)
                /          │          \
               ▼           ▼           ▼
      [ engine_camera.py ] [ cli_module.py ] [ ui_windows.py ] [ hud_display.py ]
```

---

## 4. Instrucción final

Confírmame que has entendido estas reglas, la arquitectura del proyecto y las restricciones de código antes de comenzar a generar cualquier script.