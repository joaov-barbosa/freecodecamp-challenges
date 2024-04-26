from mean_var_std import calculate

def main():
    # Teste da função calculate() com entrada válida
    entrada_valida = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    resultado = calculate(entrada_valida)
    print("Resultado para entrada válida:")
    print(resultado)

    # Teste da função calculate() com entrada inválida
    entrada_invalida = [0, 1, 2, 3, 4, 5, 6, 7]
    try:
        resultado = calculate(entrada_invalida)
    except ValueError as e:
        print(f"Entrada inválida: {e}")

if __name__ == "__main__":
    main()