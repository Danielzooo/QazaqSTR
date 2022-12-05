from django.db import models


class FactorynameChoise(models.TextChoices):
    ALCAS = 'ALCAS', 'Алкас бетон'
    AKZHAR = 'AKZHAR', 'Акжар бетон'
    SALTANAT = 'SALTANAT', 'Салтанат бетон'
    BURUNDAI = 'BURUNDAI', 'Бурундай бетон'
    ALIANC = 'ALIANC', 'Альянс бетон'
    RBY = 'RBY', 'Рбу бетон'
    VOSTOK = 'VOSTOK', 'Восток бетон'
    KAZ = 'KAZ', 'Каз бетон'
    TAY = 'TAY', 'Тау бетон'
    AKSY = 'AKSY', 'Аксу бетон'
    TEMIR = 'TEMIR', 'Темир бетон'
    ZHSN = 'ZHSN', 'ЖСН бетон'
    ABK = 'ABK', 'АБК бетон'
    BARAKAT = 'BARAKAT', 'Баракат бетон'
    TASKILEM = 'TASKILEM', 'Таскилем бетон'
    ALIANC_ASTANA = 'ALIANC_ASTANA', 'Альянс(Астана) бетон'
    FARHAT = 'FARHAT', 'Фархат Инженеринг бетон'
    FAST_PROMO = 'FAST_PROMO', 'Фаст(Промо-С) бетон'
    FAST_KONKRIT = 'FAST_KONKRIT', 'Фаст(Конкрит) бетон'
    FAST_MELIOR = 'FAST_MELIOR', 'Фаст(Мелиор Логистик) бетон'
    SITI_LAIT = 'SITI_LAIT', 'Сити Лайт бетон'
    TSZH = 'TSZH', 'ТСЖ бетон'
    TAYEKEL = 'TAYEKEL', 'Тауекел бетон'


class MarkChoise(models.TextChoices):
    M1 = '120', '120'
    M2 = '220', '220'
    M3 = '340', '340'
    M4 = '520', '520'


class ConstructiveChoise(models.TextChoices):
    CTM = 'ctm', 'CNM'
    K = 'k', 'K'
    T = 't', 'T'
    MS = 'ms', 'MS'
