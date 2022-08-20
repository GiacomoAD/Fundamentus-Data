# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 02:39:12 2021

@author: GiacomoAD
"""



## ==> GUI FILE
from main_app import *
from threading import Thread

from bs4 import BeautifulSoup
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import pandas as pd
import lxml
import os
import sys

#import bc.bancocentral as bancocentral
from datetime import datetime
from datetime import date


ANO_BALANCO = date.today().year

class appFunctions(MainWindow):


    def runApp(self, console_signal, pBar_signal):
        #print("Testando")
        
        lim_inf_val = float(self.ui.lineEdit.text())
        self.ui.lineEdit.setReadOnly(True)
        
        lim_sup_val = float(self.ui.lineEdit_2.text())
        self.ui.lineEdit_2.setReadOnly(True)
        
        lim_ROE = float(self.ui.lineEdit_5.text())
        self.ui.lineEdit_5.setReadOnly(True)
        
        lim_LC = float(self.ui.lineEdit_6.text())
        self.ui.lineEdit_6.setReadOnly(True)
        
        lim_SOLFIN = float(self.ui.lineEdit_3.text())
        self.ui.lineEdit_3.setReadOnly(True)
        
        lim_DIV_EBITDA = float(self.ui.lineEdit_4.text())
        self.ui.lineEdit_4.setReadOnly(True)

        self.ui.button_run.setEnabled(False)

        #console_signal.emit(str(lim_inf_val) +'\n' +  str(lim_sup_val) +'\n' +  str(lim_ROE) +'\n' +  str(lim_LC) +'\n')
        
        nome_arquivo = self.ui.lineEdit_7.text()

        runningThread = Thread(target=appFunctions.threadedRun, args=(self, lim_inf_val, lim_sup_val, lim_ROE, lim_LC, lim_SOLFIN, lim_DIV_EBITDA, console_signal, pBar_signal, nome_arquivo))
        runningThread.daemon = True
        runningThread.start()
        
        return
    
    def threadedRun(self, lim_inf_val, lim_sup_val, lim_ROE, lim_LC, lim_SOLFIN, lim_DIV_EBITDA, console_signal, pBar_signal, nome_arquivo):
        
        urlbase1 = 'http://www.fundamentus.com.br/detalhes.php?papel='
        header  = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
        req = requests.get(urlbase1, headers=header)
        print(req.status_code)
        
        if req.status_code == 200:
            print('Requisicao bem sucedida!')
            content = req.content
            
        soup    =   BeautifulSoup(content, 'html.parser')
        table   =   soup.find_all(name = 'table')
            
        tabela0 = str(table[0])
            
        df0     =   (pd.read_html(tabela0))[0]
            
        empresas = []
            
        for i in range(0, len(df0)):
            empresas.append(df0.Papel[i])
            
            
            
            
        URLbase2 = 'https://www.fundamentus.com.br/detalhes.php?papel='
        
        selecionadas = {}
        console_signal.emit('Serao analisadas ' + str(len(empresas)) + ' empresas\n')
        contador = 0
        pBar_signal.emit(contador, len(empresas))

        for empresa in empresas:
            print(empresa)
            URL = URLbase2 + empresa
            
                        
            retry_strategy = Retry(
                total=3,
                status_forcelist=[429, 500, 502, 503, 504],
                method_whitelist=["HEAD", "GET", "OPTIONS"]
            )

            adapter = HTTPAdapter(max_retries=retry_strategy)
            http = requests.Session()
            http.mount("http://", adapter)
            
            req = http.get(URL, headers=header)
        
            contador += 1
            
        
            if req.status_code == 200:
                #print('Requisicao ' + str(contador) + ' bem sucedida!')
                content = req.content
        
            soup = BeautifulSoup(content, 'html.parser')
            table = soup.find_all(name='table')
            
            pBar_signal.emit(contador, len(empresas))
            try:
                
                tabela0 = str(table[0])
                tabela1 = str(table[1])
                tabela2 = str(table[2])
                tabela3 = str(table[3])
                tabela4 = str(table[4])
        
                df0 = (pd.read_html(tabela0))[0]                              #Nome / Setor / Ultima cotaçao
                df1 = (pd.read_html(tabela1))[0]                              #Contem valor de mercado / Ultimo balanço
                df2 = (pd.read_html(tabela2,decimal=',', thousands='.'))[0]   #Alguns indicadores
                df3 = (pd.read_html(tabela3,decimal=',', thousands='.'))[0]   #Ativos
                df4 = (pd.read_html(tabela4,decimal=',', thousands='.'))[0]   #Receita / EBIT
        
                codigo = df0[1][0]
                att = appFunctions.find_att(df1)
                valor_mercado = appFunctions.find_valorMercado(df1)
                ROE = appFunctions.find_ROE(df2)
                LC = appFunctions.find_LC(df2)
                SolFin = appFunctions.find_solFin(df3)
                CresRec = appFunctions.find_CresRec(df2)
                lucro = appFunctions.find_lucro3mes(df4)
                ebitda = appFunctions.find_ebitda(df2, df4)
                setor = appFunctions.find_setor(df0)
                p_l = appFunctions.find_pl(df2)
                p_vp = appFunctions.find_pvp(df2)
                ev_ebitda  = appFunctions.find_evEbitda(df2)
                ev_recliq = appFunctions.find_evRecliq(df4, df2)
                ey = appFunctions.find_ey(df2)
                divLiq_ebitda = appFunctions.find_div_ebitda(df3,ebitda)
                divYield = appFunctions.find_divYield(df2)
                        
                teste_lucro = lucro/1000000
                teste_valor = valor_mercado/1000000000
        
        
                if((teste_valor >= float(lim_inf_val)) and (teste_valor <= float(lim_sup_val)) and (ROE > float(lim_ROE)) and (LC > float(lim_LC)) and (SolFin < float(lim_SOLFIN)) and (att == 0) and (teste_lucro > 0) and (divLiq_ebitda <= float(lim_DIV_EBITDA))):
                    console_signal.emit('Empresa encontrada: ' + str(codigo) + '\n')
                    i = i + 1
                    
                    info = [str(codigo), (valor_mercado), (ROE), (ebitda), (SolFin), (divLiq_ebitda), (LC), str(setor),
                   (ey), (p_l), (p_vp), (ev_ebitda), (ev_recliq), str(divYield)]
                    
                    appFunctions.setorizando(selecionadas, info, setor)
                    
                    
                    
                
            except Exception as e:
                print(e)
                pass
        
        
        
        tabelas = appFunctions.tabelando(selecionadas)
        
        tabelas[0].columns=['Codigo', 'Valor', 'ROE', 'EBITDA', 'DivLiq/PatLiq', 'DivLiq/EBITDA','LC','Setor','EY','P/L','P/VP','EV/EBITDA','EV/RecLiq', 'DivYield']
        teste = tabelas.pop(0)

        for tabela in tabelas:
            tabela.columns=['Codigo', 'Valor', 'ROE', 'EBITDA', 'DivLiq/PatLiq', 'DivLiq/EBITDA','LC','Setor','EY','P/L','P/VP','EV/EBITDA','EV/RecLiq', 'DivYield']

        for tabela in tabelas:
            teste = teste.append(tabela)
        
        teste = teste.reset_index(drop=True)

        teste = teste.sort_values(by='ROE', ascending=False)
        teste['ROE INDEX'] = range(1, 1+len(teste))

        teste = teste.sort_values(by='P/L')
        teste['P/L INDEX'] = range(1, 1+len(teste))

        soma = teste['ROE INDEX'] + teste['P/L INDEX']
        teste['RANKING'] = soma
        teste = teste.sort_values(by='RANKING')

        df_header = pd.DataFrame([{'Codigo':0, 'Valor':str(lim_inf_val)+' < '+str(lim_sup_val), 'ROE':'> '+str(lim_ROE), 'EBITDA':0, 'DivLiq/PatLiq':'< '+ str(lim_SOLFIN), 'DivLiq/EBITDA':'< '+str(lim_DIV_EBITDA),'LC':'> '+str(lim_LC),'Setor':0,'EY':0,'P/L':0,'P/VP':0,'EV/EBITDA':0,'EV/RecLiq':0, 'DivYield':0, 'ROE INDEX':0, 'P/L INDEX':0, 'RANKING':0}],index=['CONDICOES FILTRO'])
        #df2 = pd.DataFrame([{'Codigo':0, 'Valor':str(lim_inf_val)+' < '+str(lim_sup_val), 'ROE':0, 'EBITDA':0, 'DivLiq/PatLiq':0, 'DivLiq/EBITDA':0,'LC':0,'Setor':0,'EY':0,'P/L':0,'P/VP':0,'EV/EBITDA':0,'EV/RecLiq':0, 'DivYield':0}],index=[0])
        
        final = pd.concat([df_header, teste])
        
        with pd.ExcelWriter(nome_arquivo) as writer:
            final.to_excel(writer, sheet_name="Selecao")

        # with pd.ExcelWriter(nome_arquivo) as writer:
        #     for tabela in tabelas:
        #         tabela.columns=['Codigo', 'Valor', 'ROE', 'EBITDA', 'DivLiq/PatLiq', 'DivLiq/EBITDA','LC','Setor','EY','P/L','P/VP','EV/EBITDA','EV/RecLiq']
        #         tabela.to_excel(writer, sheet_name=tabela['Setor'].values[0])
        #         tabela.to_excel(writer, sheet_name=tabela['Setor'].values[0])
                
        
        console_signal.emit('Arquivo salvo em: ' + nome_arquivo +'\n')     
        console_signal.emit('------ PROGRAMA FINALIZADO ------' +'\n')
        
        return
    
    def chooseFile(self):
        print("Testando 2")
        diretorio = QtWidgets.QFileDialog.getSaveFileName(None, 'Select a folder:')
        diretorio = diretorio[0]
        
        if diretorio == '':
            diretorio = os.getcwd()
            diretorio = diretorio + r'\PlanilhaSaida.xlsx' 

        else:
            diretorio = diretorio + r'.xlsx'
            
        print(diretorio)
        
        self.ui.lineEdit_7.setText(diretorio)
        
        return
    
    def setorizando(lista, info, setor):
    
        if setor in lista.keys():
            
            lista[setor].append(info)
            
        else:
            
            lista[setor] = [info]
        
        return

    def tabelando(lista):
        tabelas = []
        i=0
        for setor in lista:
            #print(setor)
            #tabelas.append(pd.DataFrame(columns=['Codigo', 'Valor', 'ROE', 'EBITDA', 'DivLiq/PatLiq', 'DivLiq/EBITDA','LC','Setor','EY','P/L','P/VP','EV/EBITDA','EV/RecLiq']))
            tabelas.append(pd.DataFrame())
            for elemento in lista[setor]:
                #print(elemento)
                tabelas[i] = tabelas[i].append(pd.DataFrame(elemento).T)
                    
            i+=1
            
        
        return tabelas

    def find_att(dataframe):
        att = dataframe[3][0]
        att = int(att[len(att)-4::])
        
        year = int(datetime.now().year)

        if(att - year == 0 or att - (year-1) == 0):
            return 0

        else:
            return 1


        return att
    

    def find_ROE(dataframe):
        ROE = dataframe[5][8]

        ROE = ROE.replace('%', '')

        return float(ROE.replace(',', '.'))

    def find_valorMercado(dataframe):

        valormercado = dataframe[1][0]

        valor = int(valormercado.replace('.', ''))


        return valor

    def find_LC(dataframe):

        LC = float(dataframe[5][9].replace(',', '.'))

        return LC

    def find_solFin(dataframe):

        try:

            PatLiq = dataframe[3][3]
            DivLiq = dataframe[3][2]

            DivLiq = float(DivLiq.replace('.', ''))
            PatLiq = float(PatLiq.replace('.', ''))
            
            if PatLiq <= 0:
                return 999

            SolFin = DivLiq/PatLiq
            SolFin = "{0:.3f}".format(SolFin)
            return float(SolFin)

        except:
            return 999

    def find_CresRec(dataframe):
        
        try:
            CresRec = dataframe[3][11]
            CresRec = CresRec.replace('%','')
            CresRec = CresRec.replace(',','.')
            CresRec = float(CresRec)    
        
            return (CresRec)

        except:
            return '-'

    def find_lucro3mes(dataframe):

        lucro = dataframe[3][4]

        valor = int(lucro.replace('.', ''))


        return valor

    def find_ebitda(df1, df2):
        
        ebit = df2[1][3]
        ebit = float(ebit.replace('.',''))
        ev_ebit = float(df1[3][10])
        
        ev = ebit*ev_ebit
        
        ev_ebitda = float(df1[3][9])
        
        ebitda = 1/ev_ebitda
        ebitda = ev*ebitda
        
        
        return ebitda

    def find_div_ebitda(dataframe, ebitda):
        
        return float(dataframe[3][2])/ebitda

    def find_setor(dataframe):
        return dataframe[1][3]

    def find_pvp(dataframe):
        return float(dataframe[3][2])

    def find_pl(dataframe):
        return float(dataframe[3][1])

    def find_evEbitda(dataframe):
        return float(dataframe[3][9])

    def find_evRecliq(df4, df2):

        rec_liq = float(df4[1][2])
        ebit = float(df4[1][3])
        ev_ebit = float(df2[3][10])
    
    
        return ((ev_ebit*ebit)/(rec_liq))

    def find_ey(dataframe):
        return 1/(float(dataframe[3][10]))

    def find_divYield(dataframe):
    
        divYield = dataframe[3][8]

        divYield = divYield.replace('%', '')

        return (divYield.replace(',', '.'))
