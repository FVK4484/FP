import csv
from collections import namedtuple
from datetime import datetime, date

Video = namedtuple("Video", "id, fecha_trending, titulo, canal, categoria, visitas, likes, dislikes")

lista = []

def lee_trending_videos(fichero):
    with open(fichero, encoding = 'utf-8') as f:
        lector = csv.reader(f, delimiter = ';')
        next(lector)
        for id, fecha_trending, titulo, canal, categoria, visitas, likes, dislikes in lector:
            fecha_trending = datetime.strptime(fecha_trending, '%d/%m/%Y').date()
            visitas = int(visitas)
            likes = int(likes)
            dislikes = int(dislikes)
            tupla = Video(id, fecha_trending, titulo, canal, categoria, visitas, likes, dislikes)
            lista.append(tupla)
    return lista

def media_visitas(videos, fecha):
    res = 0
    for video in videos:
        cont += 1
        if fecha == video.fecha_trending:
            res += video.visitas
    return res / cont

# def media_visitas(videos, fecha):
#     visitas = [video.visitas for video in videos if fecha == video.fecha_trending]
#     media = 0
#     if len(visitas) > 0:
#         media = sum(visitas) / len(visitas)
#     return media

def video_mayor_ratio_likes_dislikes(videos, categoria = None):
    videos = [video for video in videos
              if(categoria == None or categoria == video.categoria) and video.dislikes > 0]
    return max(videos, key = lambda video: video.likes / video.dislikes)


