#!/bin/bash
# calculadora bash - atividade linux
# autor: claudio santos


echo "calculadora bash"

read -p "digite o primeiro numero:  " NUM1
read -p "digite o segundo numero:   " NUM2

echo ""
echo "escolha a operacao:"
echo "  1 - adicao       (+)"
echo "  2 - subtracao    (-)"
echo "  3 - multiplicacao (x)"
echo "  4 - divisao      (/)"
read -p "digite a opcao (1-4): " OPCAO


case $OPCAO in
  1)
   resultado=$(echo "$NUM1 + $NUM2" | bc)
    echo "resultado: $NUM1 + $NUM2 = $resultado"
    ;;
  2)
    resultado=$(echo "$NUM1 - $NUM2" | bc)
    echo "resultado: $NUM1 - $NUM2 = $resultado"
    ;;
  3)
    resultado=$(echo "$NUM1 * $NUM2" | bc)
    echo "resultado: $NUM1 x $NUM2 = $resultado"
    ;;
  4)
    if [ "$NUM2" -eq 0 ]; then
      echo "erro: divisao por zero nao e permitida!"
    else
      RESULTADO=$(echo "scale=2; $NUM1 / $NUM2" | bc)
      echo "resultado: $NUM1 / $NUM2 = $resultado"
    fi
    ;;
  *)
    echo "opcao invalida! digite um numero entre 1 e 4."
    ;;
esac

echo ""
echo "   obrigado por usar a calculadora!"
