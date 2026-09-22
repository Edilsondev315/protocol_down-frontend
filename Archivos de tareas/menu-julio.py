import pygame
import sys

# =========================
# INICIALIZACIÓN
# =========================

pygame.init()

ANCHO = 1920
ALTO = 1080

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego CCNA")

reloj = pygame.time.Clock()


# =========================
# COLORES
# =========================

FONDO = (25, 30, 40)
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (50, 100, 200)
ROJO = (200, 60, 60)
VERDE = (60, 180, 100)
GRIS = (100, 100, 100)


# =========================
# FUENTES
# =========================

fuente_titulo = pygame.font.Font(None, 60)
fuente = pygame.font.Font(None, 36)
fuente_pequena = pygame.font.Font(None, 28)


# =========================
# ESCENA
# =========================

escena = "menu"

modal_visible = False


# =========================
# JUGADOR
# =========================

jugador = pygame.Rect(200, 500, 50, 50)


# =========================
# OBJETO CCNA
# =========================

objeto_ccna = pygame.Rect(1500, 500, 80, 80)


# =========================
# BOTONES DEL MENÚ
# =========================

boton_jugar = pygame.Rect(810, 250, 300, 60)

boton_opciones = pygame.Rect(810, 380, 300, 60)

boton_salir = pygame.Rect(810, 510, 300, 60)


# =========================
# FUNCIÓN PARA DIBUJAR TEXTO
# =========================

def dibujar_texto(texto, fuente, color, superficie, x, y):

    imagen = fuente.render(texto, True, color)

    rect = imagen.get_rect(center=(x, y))

    superficie.blit(imagen, rect)


# =========================
# FUNCIÓN PARA CALCULAR DISTANCIA
# =========================

def calcular_distancia(rect1, rect2):

    x1, y1 = rect1.center
    x2, y2 = rect2.center

    distancia_x = x2 - x1
    distancia_y = y2 - y1

    distancia = (distancia_x ** 2 + distancia_y ** 2) ** 0.5

    return distancia


# =========================
# MENÚ PRINCIPAL
# =========================

def mostrar_menu():

    pantalla.fill(FONDO)

    # Título
    dibujar_texto(
        "JUEGO CCNA",
        fuente_titulo,
        BLANCO,
        pantalla,
        ANCHO // 2,
        130
    )

    # =========================
    # BOTÓN JUGAR
    # =========================

    pygame.draw.rect(
        pantalla,
        AZUL,
        boton_jugar
    )

    dibujar_texto(
        "JUGAR",
        fuente,
        BLANCO,
        pantalla,
        boton_jugar.centerx,
        boton_jugar.centery
    )

    # =========================
    # BOTÓN OPCIONES
    # =========================

    pygame.draw.rect(
        pantalla,
        AZUL,
        boton_opciones
    )

    dibujar_texto(
        "OPCIONES",
        fuente,
        BLANCO,
        pantalla,
        boton_opciones.centerx,
        boton_opciones.centery
    )

    # =========================
    # BOTÓN SALIR
    # =========================

    pygame.draw.rect(
        pantalla,
        ROJO,
        boton_salir
    )

    dibujar_texto(
        "SALIR",
        fuente,
        BLANCO,
        pantalla,
        boton_salir.centerx,
        boton_salir.centery
    )


# =========================
# ESCENA DEL JUEGO
# =========================

def mostrar_juego():

    pantalla.fill((35, 80, 60))

    # Título
    dibujar_texto(
        "ESCENA DEL JUEGO",
        fuente_titulo,
        BLANCO,
        pantalla,
        ANCHO // 2,
        80
    )

    # =========================
    # JUGADOR
    # =========================

    pygame.draw.rect(
        pantalla,
        AZUL,
        jugador
    )

    # =========================
    # OBJETO CCNA
    # =========================

    pygame.draw.rect(
        pantalla,
        VERDE,
        objeto_ccna
    )

    dibujar_texto(
        "CCNA",
        fuente_pequena,
        NEGRO,
        pantalla,
        objeto_ccna.centerx,
        objeto_ccna.centery
    )

    # =========================
    # DISTANCIA
    # =========================

    distancia = calcular_distancia(
        jugador,
        objeto_ccna
    )

    # =========================
    # MENSAJE DE INTERACCIÓN
    # =========================

    if distancia < 150:

        dibujar_texto(
            "Presiona E para interactuar",
            fuente,
            BLANCO,
            pantalla,
            ANCHO // 2,
            ALTO - 100
        )

    # =========================
    # VENTANA MODAL
    # =========================

    if modal_visible:

        mostrar_modal()


# =========================
# VENTANA MODAL
# =========================

def mostrar_modal():

    # Fondo oscuro
    fondo = pygame.Surface(
        (ANCHO, ALTO)
    )

    fondo.set_alpha(180)

    fondo.fill(NEGRO)

    pantalla.blit(
        fondo,
        (0, 0)
    )

    # =========================
    # VENTANA
    # =========================

    ventana = pygame.Rect(
        500,
        300,
        920,
        480
    )

    pygame.draw.rect(
        pantalla,
        BLANCO,
        ventana
    )

    pygame.draw.rect(
        pantalla,
        AZUL,
        ventana,
        5
    )

    # =========================
    # TÍTULO
    # =========================

    dibujar_texto(
        "INFORMACIÓN CCNA",
        fuente_titulo,
        AZUL,
        pantalla,
        ANCHO // 2,
        380
    )

    # =========================
    # INFORMACIÓN
    # =========================

    dibujar_texto(
        "Cisco Certified Network Associate",
        fuente,
        NEGRO,
        pantalla,
        ANCHO // 2,
        450
    )

    dibujar_texto(
        "Aquí aparecerá la información",
        fuente_pequena,
        NEGRO,
        pantalla,
        ANCHO // 2,
        510
    )

    dibujar_texto(
        "relacionada con el objeto CCNA.",
        fuente_pequena,
        NEGRO,
        pantalla,
        ANCHO // 2,
        550
    )

    dibujar_texto(
        "Presiona E para cerrar",
        fuente_pequena,
        GRIS,
        pantalla,
        ANCHO // 2,
        650
    )


# =========================
# BUCLE PRINCIPAL
# =========================

ejecutando = True

while ejecutando:

    # =========================
    # EVENTOS
    # =========================

    for evento in pygame.event.get():

        # Cerrar ventana
        if evento.type == pygame.QUIT:

            ejecutando = False

        # =========================
        # CLIC DEL MOUSE
        # =========================

        if evento.type == pygame.MOUSEBUTTONDOWN:

            posicion = pygame.mouse.get_pos()

            # Estamos en el menú
            if escena == "menu":

                # JUGAR
                if boton_jugar.collidepoint(posicion):

                    escena = "juego"

                # OPCIONES
                elif boton_opciones.collidepoint(posicion):

                    print("Opciones seleccionadas")

                # SALIR
                elif boton_salir.collidepoint(posicion):

                    ejecutando = False

        # =========================
        # TECLADO
        # =========================

        if evento.type == pygame.KEYDOWN:

            # Estamos en el juego
            if escena == "juego":

                # =========================
                # TECLA E
                # =========================

                if evento.key == pygame.K_e:

                    distancia = calcular_distancia(
                        jugador,
                        objeto_ccna
                    )

                    if distancia < 150:

                        modal_visible = not modal_visible

                # =========================
                # TECLA ESC
                # =========================

                if evento.key == pygame.K_ESCAPE:

                    if modal_visible:

                        modal_visible = False

                    else:

                        escena = "menu"


    # =========================
    # MOVIMIENTO DEL JUGADOR
    # =========================

    if escena == "juego" and not modal_visible:

        teclas = pygame.key.get_pressed()

        velocidad = 7

        # Izquierda
        if teclas[pygame.K_LEFT]:

            jugador.x -= velocidad

        # Derecha
        if teclas[pygame.K_RIGHT]:

            jugador.x += velocidad

        # Arriba
        if teclas[pygame.K_UP]:

            jugador.y -= velocidad

        # Abajo
        if teclas[pygame.K_DOWN]:

            jugador.y += velocidad

        # No salir de la pantalla
        jugador.clamp_ip(
            pantalla.get_rect()
        )


    # =========================
    # DIBUJAR ESCENA
    # =========================

    if escena == "menu":

        mostrar_menu()

    elif escena == "juego":

        mostrar_juego()


    # Actualizar pantalla
    pygame.display.flip()

    # 60 FPS
    reloj.tick(60)


# =========================
# CERRAR
# =========================

pygame.quit()

sys.exit()