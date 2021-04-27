mochila = ['Pan', 'Capa', 'Sable de luz', 'otro']

def usar_fuerza(mochila, pos):
    if(pos< len(mochila)):
        if(mochila[pos] == 'Sable de luz'):
            return ('Fueron sacados', pos, 'objetos hasta encontrar el Sable de luz')
        else:
            return usar_fuerza(mochila, pos+1)
    else:
        return -1

print(usar_fuerza(mochila, 0))
