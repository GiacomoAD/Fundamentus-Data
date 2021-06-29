# Fundamentus Data

Fundamentus Data é uma interface feita em Python para filtrar empresas da BOVESPA a partir de dados financeiros e fundamentalistas, disponíveis em [FUNDAMENTUS](https://www.fundamentus.com.br).


## Instalação

Clone este repositório:

```git
git clone https://github.com/GiacomoAD/Fundamentus-Data
```

Utilize o gerenciador de pacotes [pip](https://pip.pypa.io/en/stable/) para instalar os requerimentos:

```bash
pip install requirements.txt
```

## Utilização
**É NECESSÁRIA CONEXÃO COM INTERNET**

Para executar a interface:

```python
python main_app.py
```

O usuário pode selecionar o arquivo de saída e estabelecer as faixas para filtragem de acordo com os seguintes parâmetros:

* Valor de mercado da empresa;
* Retorno de investimento (R.O.E.);
* Liquidez Corrente (L.C.);
* Divida Liquida/Patrimonio Liquido;
* Divida Liquida/EBITDA.

Após ajustado os parâmetros, o usuário deve clicar no botão "Run" para iniciar o processo.


Ao finalizar o processo, será gerada uma tabela (no formato ".xlsx") contendo as seguintes informações sobre as empresas selecionadas:

|Codigo| Valor | R.O.E | EBITDA | DivLiq/PatLiq | DivLiq/EBITDA | L.C. | Setor | EY | P/L | P/VP | EV/EBITDA | EV/RecLiq | DivYield|
| ------------- |:-------------:| -----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|
