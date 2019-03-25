# Kullanışlı araçların bulunduğu dosya

def hex_to_rgb(hex):
    hex = hex.lstrip('#')
    color = tuple(int(hex[i:i+2], 16) for i in (0, 2 ,4))
    return color