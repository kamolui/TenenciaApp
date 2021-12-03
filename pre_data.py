# Busca los periodos contenidos en la base dada
def periodos(df):
    per_p = ['Periodos_20' + str(x) for x in range(15, 25)]
    r = []

    for i in per_p:
        if i in df.columns:
            r.append(i)
    return r


# Suma los periodos pagados de cada contribuyente


def periodo(cols):
    return cols.sum()

# Linea donde se usa la funcion
# df['periodos'] = df[df[r].columns].apply(periodo, axis=1)

def y_max(data):
    return data.Inicio.max()

# year_max = y_max(data)

# Calcula la cantidad de periodos adeudados del contribuyente


def deudas(cols):
    ingreso = cols[0]
    pagos = cols[1]

    if pagos != y:
        deuda = (year_max - (ingreso - 1)) - pagos
    else:
        deuda = 0

    return deuda


# df['deuda'] = df[['Inicio', 'periodos']].apply(deudas, axis=1)