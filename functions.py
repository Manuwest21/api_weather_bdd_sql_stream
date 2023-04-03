def conversion(wind):
    if 0 <= wind <= 20 or 340 <= wind <= 360:
        return "nord"
    elif 20 < wind <= 70:
        return "nord-est"
    elif 70 < wind <= 110:
        return "est"
    elif 110 < wind <= 160:
        return "sud-est"
    elif 160 < wind <= 200:
        return "sud"
    elif 200 < wind <= 240:
        return "sud-ouest"
    elif 240 < wind <= 280:
        return "ouest"
    elif 280 < wind < 340:
        return "sud"