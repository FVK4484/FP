from audiencias import * 

def test_lee_audiencias (audiencias, nombre_programa):
    print(f"Audiencias del programa {nombre_programa}:")
    print(audiencias[:20])

def test_calcula_ediciones(audiencias, nombre_programa):
    print(f'Número de ediciones del programa {nombre_programa}: {calcula_ediciones(audiencias)}')

def main():
    '''
    Función principal
    '''
    #test de la función de lectura de ficheros--------------------------------------------------------------- 
    audiencias_gh = lee_audiencia(r'doc\teoria\TEO-Audiencias-main\data\GH.csv')
    # test_lee_audiencias(audiencias_gh, "Gran Hermano")
    test_calcula_ediciones(audiencias_gh, "Gran Hermano")
    
    audiencias_masterchef = lee_audiencia(r'doc\teoria\TEO-Audiencias-main\data\MasterChef.csv')
    # test_lee_audiencias(audiencias_masterchef, "Master Chef")
    test_calcula_ediciones(audiencias_masterchef, "Master Chef")

if __name__=="__main__":
    main()