# Protocol Down — Frontend

---

## 📥 1. Instalar Git

- **Windows**: Descargar e instalar desde 👉 [git-scm.com/download/win](https://git-scm.com/download/win) (dejar opciones por defecto).
- **macOS**: Ejecutar `brew install git` o `xcode-select --install`.
- **Linux**: Ejecutar `sudo apt install git -y`.

Verificar la instalación:

```bash
git --version
```

---

## ⚙ 2. Configurar Git (una sola vez)

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu.correo@ejemplo.com"
git config --global init.defaultBranch main
```

> ⚠️ Usa el **mismo correo** de tu cuenta de GitHub.

---

## 🔑 3. Crear Token de Acceso en GitHub

1. Ir a 👉 [github.com/settings/tokens/new](https://github.com/settings/tokens/new)
2. En **Note** escribir un nombre (ej: `mi-pc`).
3. Seleccionar una expiración.
4. Marcar el scope **`repo`**.
5. Click en **Generate token** y **copiar el token** (solo se muestra una vez).

Para no tener que ingresar el token cada vez:

```bash
# Windows
git config --global credential.helper wincred

# macOS
git config --global credential.helper osxkeychain

# Linux
git config --global credential.helper store
```

> La primera vez que hagas `push` o `pull`, Git pedirá usuario y contraseña. En **contraseña pegar el token**, no la contraseña de GitHub.

---

## 🚀 4. Clonar el Proyecto

```bash
cd C:\Users\TuUsuario\Documents\Proyectos   # Ubicarte en tu carpeta de trabajo

git clone https://github.com/Edilsondev315/protocol_down-frontend.git
cd protocol_down-frontend
// npm install 

```

---

## 🌿 5. Flujo de Trabajo Diario

```bash
# Actualizar tu rama principal
git checkout main
git pull origin main

# Crear una rama para tu tarea
git checkout -b feature/nombre-de-tu-tarea

# ... trabajar en tus archivos ...

# Guardar y subir tus cambios
git add .
git commit -m "feat: descripción del cambio"
git push origin feature/nombre-de-tu-tarea
```

Luego ir a GitHub y crear un **Pull Request** desde tu rama hacia `main`.

### Convención de commits

| Prefijo      | Uso                          | Ejemplo                                  |
|-------------|------------------------------|------------------------------------------|
| `feat:`     | Nueva funcionalidad          | `feat: agregar barra de navegación`      |
| `fix:`      | Corrección de errores        | `fix: corregir desbordamiento en móvil`  |
| `style:`    | Cambios de estilo / formato  | `style: ajustar colores del tema`        |
| `docs:`     | Documentación                | `docs: actualizar README`                |
| `refactor:` | Refactorización              | `refactor: extraer componente`           |

---

## 🛠 6. Problemas Comunes

| Error | Solución |
|-------|----------|
| `repository not found` | Verificar acceso al repo. Pedir invitación al admin. |
| `Authentication failed` | Regenerar el token de acceso y volver a intentar. |
| `failed to push some refs` | Ejecutar `git pull origin main` antes de `push`. |
| `Merge conflict` | Abrir el archivo, resolver las marcas `<<<<<<<` / `>>>>>>>`, y hacer `git add` + `git commit`. |

---

## ⚡ Resumen Rápido

```bash
# Configurar (una vez)
git config --global user.name "Tu Nombre"
git config --global user.email "tu@correo.com"

# Clonar (una vez)
git clone https://github.com/Edilsondev315/protocol_down-frontend.git
cd protocol_down-frontend && npm install

# Trabajar (cada tarea)
git checkout main && git pull origin main
git checkout -b feature/mi-tarea
git add . && git commit -m "feat: mi cambio" && git push origin feature/mi-tarea
# → Crear Pull Request en GitHub
```
