def pedir_confirmacion(prompt, reintentos = 4, queja = "Si o no, por favor!"):
    while True:
        ok = raw_input(prompt + '\t')
        ok = ok.lower()
        if ok in ('s', 'si'):
            return True
        if ok in ('n', 'no'):
            return False
        reintentos = reintentos - 1
        if reintentos < 0:
            raise IOError('usuario duro')
        print queja
