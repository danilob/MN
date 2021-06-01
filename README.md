## Algoritmos de Métodos Numéricos

### Métodos Implementados
- Gauss-Jacobi [Ref](https://www.youtube.com/watch?v=pf4l8gv_dCM)
- Gauss-Sidel [Ref](https://www.youtube.com/watch?v=rb83M5hgZdk)

### Arquivos de Entrada
Os arquivos de entrada que constituem um sistema `Ax=b` podem ser localizados na pasta `matrix/`, você mesmo pode criar sua entrada especificando:

2. `n` = tamanho da matriz A, considerando-se uma matriz quadrada
2. `n` linhas do sistema, desconsiderando as incognitas e o resultado da equação (somente os valores das constantes) 
2. `n` valores iniciais para as incognitas `x`
2. `e` = O erro da norma
2. `imax` = Quantidade máxima de passos

### Como executar?

Antes, verifique se você tem esses pacotes instalados (os pacotes abaixo são do Ubuntu):

```
sudo apt-get install build-essential python3-dev python3-venv python3-pip
```

Crie um virtualenv com python 3:

```
virtualenv -p python3 venv
```

Ative o virtualenv:

```
source venv/bin/activate
```

Instale as dependencias com o comando abaixo:

```
pip install -r requirements.txt
```

Execute

```
python solve-system.py matrix/exemple1.txt
```
