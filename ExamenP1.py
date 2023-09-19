import cv2
import numpy as np  # Importa NumPy

# Ruta de la imagen original
imagen_ruta = 'camera_man_ruido.png'

# Cargar la imagen
imagen = cv2.imread(imagen_ruta)

# Comprueba si la imagen se ha cargado correctamente
if imagen is not None:
    x_inicio = 100  # Coordenada x del punto de inicio
    y_inicio = 50   # Coordenada y del punto de inicio
    x_fin = 300     # Coordenada x del punto final
    y_fin = 250     # Coordenada y del punto final

    # Recortar la imagen
    imagen_recortada = imagen[y_inicio:y_fin, x_inicio:x_fin]

    # Guardar la imagen recortada
    cv2.imwrite('camera_man_face.png', imagen_recortada)

    imagen_tratada1 = cv2.GaussianBlur(imagen_recortada, (1, 1), 0)
    cv2.imwrite('camera_man_tratada1.png', imagen_tratada1)

    imagen_tratada2 = cv2.medianBlur(imagen_tratada1, 5)
    cv2.imwrite('camera_man_tratada2.png', imagen_tratada2)

    # Aplicar un filtro de realce de bordes para mejorar la claridad
    kernel = np.array([[-1, -1, -1],
                       [-1,  9, -1],
                       [-1, -1, -1]])
    imagen_tratada3 = cv2.filter2D(imagen_tratada2, -1, kernel=kernel)
    cv2.imwrite('camera_man_tratada3.png', imagen_tratada3)

    # Mostrar la imagen tratada
    cv2.imshow('Imagen Tratada', imagen_tratada3)

    # Espera hasta que se presione una tecla y luego cierra la ventana
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print('No se pudo cargar la imagen. Verifica la ruta de la imagen.')
