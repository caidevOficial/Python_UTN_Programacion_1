from utn_fra.funciones.image_reducer import ImageReducer

RUTA_IMAGENES = './assets/background_2/'

img_reducer = ImageReducer(RUTA_IMAGENES)

img_reducer.reduce_image_size(factor_escala=0.5)
img_reducer.reduce_image_weight(nivel_compresion=9)