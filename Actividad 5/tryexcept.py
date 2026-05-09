try:
    # Riesgo de error de tipo o valor
    res = 10 / int("a")
except (ZeroDivisionError, ValueError) as e:
    print(f"Ocurrió un error: {e}")
