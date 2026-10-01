from trending import*

def test_lee_trending_videos(fichero):
    print(lee_trending_videos(fichero))

if __name__ == '__main__':
    test_lee_trending_videos(r'FP_25_26\doc\examenes\Exámenes-curso-2019-2020\Primer-examen-práctico-febrero-2020\Sesion1\data\sesion1.csv')