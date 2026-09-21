# 🚀 Guía Definitiva de Git y Trabajo Colaborativo (Para Principiantes)

¡Bienvenido! Si nunca has usado Git o sientes que la consola da miedo, esta guía está hecha exactamente para ti. Aquí aprenderás qué es Git, cómo trabajar en equipo sin borrar el código de tus compañeros y cómo dominar el flujo con ramas y Pull Requests (PR).

---

## 🧭 Índice Rápido
1. [¿Qué es Git y GitHub? (La analogía)](file:///home/Edilson/Documentos/projects/protocol-down-game/GUIA_GIT_COLABORATIVO.md#1-qué-es-git-y-github-la-analogía)
2. [Los 5 Conceptos Clave que Debes Entender](file:///home/Edilson/Documentos/projects/protocol-down-game/GUIA_GIT_COLABORATIVO.md#2-los-5-conceptos-clave)
3. [Configuración Inicial (Se hace una sola vez)](file:///home/Edilson/Documentos/projects/protocol-down-game/GUIA_GIT_COLABORATIVO.md#3-configuración-inicial-una-sola-vez)
4. [El Ciclo de Vida de los Archivos en Git](file:///home/Edilson/Documentos/projects/protocol-down-game/GUIA_GIT_COLABORATIVO.md#4-el-ciclo-de-los-cambios)
5. [Paso a Paso: El Flujo de Trabajo Colaborativo Diario](file:///home/Edilson/Documentos/projects/protocol-down-game/GUIA_GIT_COLABORATIVO.md#5-el-flujo-de-trabajo-colaborativo-paso-a-paso)
6. [¿Cómo Abrir y Revisar un Pull Request (PR)?](file:///home/Edilson/Documentos/projects/protocol-down-game/GUIA_GIT_COLABORATIVO.md#6-pull-requests-pr-trabajo-en-equipo)
7. [Qué Hacer Si Hay Conflictos (¡Sin entrar en pánico!)](file:///home/Edilson/Documentos/projects/protocol-down-game/GUIA_GIT_COLABORATIVO.md#7-cómo-resolver-conflictos-sin-miedo)
8. [Buenas Prácticas y Reglas de Oro](file:///home/Edilson/Documentos/projects/protocol-down-game/GUIA_GIT_COLABORATIVO.md#8-reglas-de-oro-del-equipo)
9. [Chuleta / Tabla de Comandos Rápidos](file:///home/Edilson/Documentos/projects/protocol-down-game/GUIA_GIT_COLABORATIVO.md#9-tabla-de-comandos-esenciales)

---

## 1. ¿Qué es Git y GitHub? (La analogía)

* **Git**: Es una **máquina del tiempo** y un sistema de guardado inteligente instalado en tu computadora. En lugar de tener carpetas llamadas `proyecto_final`, `proyecto_final_ahora_si`, `proyecto_final_este_es_el_bueno.zip`, Git guarda un historial exacto de cada cambio que haces.
* **GitHub / GitLab**: Es la **nube central** (como un Google Drive de programadores). Permite que todos los integrantes del equipo descarguen el código, suban sus avances y revisen el trabajo mutuo.

> **Regla mental:**
> * Tu computadora = *Entorno Local* (nadie más lo ve hasta que tú lo compartes).
> * GitHub = *Entorno Remoto* (el punto de encuentro de todo el equipo).

---

## 2. Los 5 Conceptos Clave

1. **Repositorio (Repo)**: Es la carpeta del proyecto rastreada por Git. Contiene todos los archivos y todo el historial de cambios.
2. **Commit**: Es un **punto de control (checkpoint)** o una foto instantánea de tu código con un mensaje explicativo (ej. *"Añade pantalla de inicio del juego"*).
3. **Rama (Branch)**: Una copia paralela del código para trabajar en una función específica sin romper lo que ya funciona. La rama principal se llama comúnmente `main`.
4. **Pull Request (PR)**: Una solicitud en GitHub para decirle a tu equipo: *"Terminé esta tarea en mi rama, por favor revísenla y si está bien, incorpórenla a la rama principal (`main`)"*.
5. **Merge**: La acción de fusionar dos ramas (por ejemplo, unir tu rama con `main` tras aprobar el PR).

---

## 3. Configuración Inicial (Una sola vez)

Antes de hacer nada, dile a Git quién eres para que tus compañeros sepan quién hizo cada cambio:

```bash
git config --global user.name "Tu Nombre o Alias"
git config --global user.email "tu_correo@ejemplo.com"
```

Para verificar que quedó bien guardado:
```bash
git config --global --list
```

---

## 4. El Ciclo de los Cambios

Cuando modificas archivos, Git los clasifica en 3 áreas:

```text
[ Working Directory ]  ---> (git add) --->  [ Staging Area ]  ---> (git commit) --->  [ Historial Git ]
(Archivos modificados)                      (Caja de envío)                           (Paquete guardado)
```

1. **Directorio de trabajo (Working Directory)**: Modificas tus scripts, imágenes o estilos. Git sabe que cambiaron, pero aún no están preparados.
2. **Área de preparación (Staging Area)**: Usas `git add` para poner en una "caja" los archivos que quieres incluir en el próximo punto de guardado.
3. **Historial (Commit)**: Sellas la caja con `git commit -m "mensaje"` y queda registrada permanentemente en el historial.

---

## 5. El Flujo de Trabajo Colaborativo Paso a Paso

Sigue esta rutina **siempre que vayas a trabajar en una nueva tarea o corrección**.

### 🔹 Paso 1: Partir de la última versión de `main`
Antes de crear cualquier cosa nueva, asegúrate de tener lo último que hicieron tus compañeros:

```bash
# 1. Cambia a la rama principal
git checkout main

# 2. Descarga los cambios más recientes de GitHub
git pull origin main
```

---

### 🔹 Paso 2: Crear tu propia rama
**¡NUNCA programes directamente sobre `main`!** Crea una rama específica para tu tarea:

```bash
# Crea y salta a la nueva rama
git checkout -b feature/nombre-de-tu-tarea
```

> **Convención de nombres de rama:**
> * `feature/login-multijugador` (nueva funcionalidad)
> * `bugfix/colision-enemigo` (corregir un error)
> * `docs/actualizar-readme` (documentación)

---

### 🔹 Paso 3: Trabaja en tu código
Abre tu editor de código (VS Code, Antigravity, etc.) y escribe tu código, crea assets, prueba que funcione en tu máquina.

Para ver qué archivos has cambiado en cualquier momento:
```bash
git status
```

---

### 🔹 Paso 4: Guardar tus cambios (Add + Commit)
Cuando hayas avanzado una parte importante y funcione:

```bash
# 1. Añade los archivos modificados a la zona de preparación
git add .

# 2. Guarda el commit con un mensaje claro y descriptivo
git commit -m "feat: implementa movimiento de personajes con teclado"
```

> **Consejos para mensajes de commit claros:**
> * `feat: ...` para nuevas características.
> * `fix: ...` para arreglar errores.
> * `style: ...` para mejoras visuales o CSS.
> * `docs: ...` para cambios de texto o documentación.

---

### 🔹 Paso 5: Subir tu rama a GitHub
Tus commits están ahora en tu computadora. Para enviarlos a GitHub:

```bash
git push -u origin feature/nombre-de-tu-tarea
```
*(El `-u origin nombre-de-rama` solo es necesario la primera vez que subes esa rama. Las siguientes veces basta con `git push`).*

---

## 6. Pull Requests (PR): Trabajo en Equipo

Una vez que subiste tu rama a GitHub:

1. Ve a la página del repositorio en **GitHub**.
2. Verás un cartel amarillo que dice: **"Compare & pull request"**. Haz clic en él.
3. **Título claro**: Explica brevemente qué hiciste (ej. *"Añadir sistema de autenticación de jugadores"*).
4. **Descripción**:
   - ¿Qué problema resuelve o qué agrega?
   - ¿Cómo pueden probarlo tus compañeros?
5. Elige la rama base (normalmente `base: main` <- `compare: feature/tu-tarea`).
6. Haz clic en **Create Pull Request**.
7. **Revisión en equipo**:
   - Uno o más compañeros revisan el código en la pestaña *"Files changed"*.
   - Si hay sugerencias, comentan allí mismo.
   - Si todo está en orden, dan clic en **"Approve"** y finalmente en **"Merge pull request"**.
8. ¡Felicidades! Tu código ya forma parte oficial de `main`.

---

### 🔹 Paso 6 (Final): Limpiar tu entorno local
Una vez que el PR fue aprobado y mezclado en GitHub:

```bash
# Vuelve a main
git checkout main

# Descarga todo lo nuevo (incluido tu propio PR ya fusionado)
git pull origin main

# Opcional: Borra tu rama local de la tarea para mantener limpio tu repo
git branch -d feature/nombre-de-tu-tarea
```

---

## 7. Cómo Resolver Conflictos (¡Sin Miedo!)

### ¿Por qué ocurre un conflicto?
Ocurre cuando **tú y otra persona modificaron exactamente las mismas líneas del mismo archivo** y Git no sabe cuál versión conservar.

Cuando haces un `git pull` o intentas fusionar, Git te avisará:
> `CONFLICT (content): Merge conflict in archivo.js`

### ¿Cómo solucionarlo?
1. Abre el archivo en conflicto en tu editor (VS Code o similar).
2. Verás unas marcas especiales como estas:

```javascript
<<<<<<< HEAD (Tu versión actual)
const velocidad = 15;
=======
const velocidad = 20;
>>>>>>> main (La versión que viene de la otra rama)
```

3. **Decide junto con tu compañero qué dejar**:
   - ¿Dejas el `15`?
   - ¿Dejas el `20`?
   - ¿O combinas ambas ideas?
4. **Borra las líneas con marcas** (`<<<<<<<`, `=======`, `>>>>>>>`) dejando solo el código limpio que debe quedar:
```javascript
const velocidad = 20;
```
5. Guarda el archivo y dile a Git que resolviste el conflicto:
```bash
git add archivo.js
git commit -m "fix: resuelve conflicto en velocidad de jugador"
git push
```

---

## 8. Reglas de Oro del Equipo 🛡️

1. 🚫 **NUNCA hagas `git push` directo a `main`**: Todo cambio debe pasar por una rama y un Pull Request.
2. 🔄 **Haz `git pull origin main` con frecuencia**: Mantenerte al día evita conflictos gigantescos al final.
3. 📦 **Commits pequeños y frecuentes**: Es mucho mejor hacer 5 commits con tareas concretas que 1 commit monstruoso de *"cambios generales"*.
4. 🙈 **Usa siempre un `.gitignore`**: Nunca subas carpetas como `node_modules/`, archivos `.env` con contraseñas o archivos temporales de tu sistema.
5. 💬 **Pregunta antes de borrar**: Si una rama o commit no es tuyo, consúltalo con el equipo antes de forzar cambios.

---

## 9. Tabla de Comandos Esenciales

| Comando | ¿Para qué sirve? |
| :--- | :--- |
| `git clone <url>` | Descarga una copia del repositorio remoto en tu PC |
| `git status` | Muestra el estado actual (archivos modificados o nuevos) |
| `git checkout -b <rama>` | Crea una rama nueva y salta a ella |
| `git checkout <rama>` | Cambia a una rama ya existente |
| `git branch` | Lista todas tus ramas locales |
| `git add .` | Prepara todos los cambios para el commit |
| `git commit -m "mensaje"` | Guarda los cambios preparados con un mensaje |
| `git push origin <rama>` | Sube tu rama y commits a GitHub |
| `git pull origin main` | Descarga e incorpora los cambios más recientes de `main` |
| `git log --oneline` | Muestra el historial reciente de commits de forma compacta |
| `git restore <archivo>` | Deshace los cambios locales de un archivo (¡cuidado!) |

---

¡Listo! Con estos pasos, cualquier equipo puede colaborar de forma profesional, ordenada y sin miedo a perder código.
