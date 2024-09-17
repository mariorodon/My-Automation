import pyautogui
import time
import logging
import ctypes
import tkinter.messagebox
import tkinter as tk
from tkinter import messagebox

def iniciar_automacao():
    # Aqui você coloca o código que inicia a sua automação
    print("Automação iniciada...")

def perguntar_inicio_automacao():
    # Criando a janela principal
    root = tk.Tk()
    root.withdraw()  # Esconde a janela principal
    
    # Exibindo a caixa de diálogo com a pergunta
    resposta = messagebox.askyesno("Iniciar Automação", "Você deseja iniciar a automação?")
    
    if resposta:
        iniciar_automacao()
    else:
        print("Automação não iniciada.")
    
    root.destroy()  # Fecha a janela principal

# Executa a função para mostrar a janela
perguntar_inicio_automacao()

#Executar apenas em zoom 75%
#Basta vc clicar na aula que deseja cadastrar
# Configuração do logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

#NOVO INTERATIVO IM AUTOMAÇÃO


cadas = 'cadastrar.png'
cadas1 = 'cadastrar1.png'
cont = 'conteudo.png'
contB = 'conteudoBran.png'
multipla = 'multipla.png'
namewhite = 'NomeBranc.png'
namered = 'NomeRed.png'
obj = 'Objetiva.png'
objeto = 'Objeto.png'
objeto1 = 'ObjetoBlack.png'
interativeobject = 'objetoINTERATIVO.png'
objetored = 'ObjetoRed.png'
preen = 'Preencha.png'
relation = 'Relacione.png'
salvar = 'salvar.png'
scroll = 'scroll.png'
video = 'video.png'
videoB = 'videoBranc.png'
aula = 'Aula2.png'
aula2 = 'Aula22.png'

def find_and_click(image_path, confidence=0.8, retries=3, interval=3):
    """Localiza uma imagem na tela e clica nela."""
    for attempt in range(retries):
        try:
            # Localiza o centro da imagem na tela
            location = pyautogui.locateCenterOnScreen(image_path, confidence=confidence)
            if location:
                logging.info(f"Imagem '{image_path}' localizada em: {location}")
                pyautogui.click(location)
                return True
            else:
                logging.warning(f"Imagem '{image_path}' não encontrada. Tentativa {attempt + 1}/{retries}")
        except Exception as e:
            logging.error(f"Erro ao tentar encontrar a imagem: {e}")
        
        time.sleep(interval)
    logging.error(f"Imagem '{image_path}' não encontrada após {retries} tentativas.")
    return False
  
def automacao_passoapasso01():
    """Executa a automação passo a passo usando imagens de referência para localizar os elementos."""
    logging.info("Iniciando a automação passo a passo 01...")

    # Passo 1: Clicar em "Cadastrar"
    if not find_and_click(cadas):
        logging.error("Não foi possível clicar em 'Cadastrar'.")
        return

    time.sleep(2)  # Espera para garantir que o menu esteja carregado

    # Passo 2: Clicar em "Tipo de Objeto" e selecionar "Video"
    if find_and_click(objeto):
        return
    
    if find_and_click(videoB):
        return
    if find_and_click(video):
        return
    if find_and_click(obj):
        return

    time.sleep(1)  # Espera para garantir que o menu esteja visível

    # Tenta clicar em 'video.png' ou fallback para 'alternativa.png'
    if not find_and_click(video):
        logging.warning("Não foi possível encontrar 'video.png'. Tentando alternativa.")
        return

    time.sleep(2)  # Espera para garantir que o campo de nome esteja acessível

    # Passo 3: Clicar no campo "Nome" e preencher
    if not find_and_click(namewhite):
        logging.error("Não foi possível clicar no campo 'Nome'.")
        if not find_and_click(namered):
            logging.error("Não foi possível localizar o 'NomeBranc.png'.")
            return

    pyautogui.write('Passo a passo 01')
    time.sleep(1)  # Espera para garantir que o texto seja escrito

    # Passo 4: Clicar no campo "Conteúdo" e preencher
    if not find_and_click(cont):
        logging.error("Não foi possível clicar no campo 'Conteúdo'.")
        if not find_and_click(contB):
            logging.error("Não foi possível clicar no campo 'Conteúdo branco'.")
            return
            
    pyautogui.write('SEM LINK')
    time.sleep(1)  # Espera para garantir que o texto seja escrito

    # Passo 5: Salvar
    if not find_and_click(salvar):
        logging.error("Não foi possível clicar em 'Salvar'.")
        return

    time.sleep(2)  # Espera para garantir que o texto seja escrito

def automacao_treinamento01():
    """Executa uma nova automação passo a passo usando imagens de referência diferentes."""
    logging.info("Iniciando a nova automação treinamento 01...")

    if not find_and_click(cadas1):
        logging.error('Nao encontrei o Cadastar. ')
        if not find_and_click(cadas):
            logging.error('Nao encontrei.')
    
    time.sleep(1)

    if not find_and_click(objeto1):
        logging.error("Infelizmente não encontrei o erro")
        if not find_and_click(objetored):
            logging.error("Infelizmento Não encontrei.")
            return
        
    time.sleep(1)

    if not find_and_click(scroll):
        logging.error("Nao encontrei")
        return

    time.sleep(1)

    if not find_and_click(interativeobject):
        logging.error("Nao achei")
        return

    time.sleep(2)

    if not find_and_click(namered):
        logging.error("nao achei o nome. LINHA 151")
        if not find_and_click(namewhite):
            logging.error("Nao achei o nome.Linha 153")

    time.sleep(1)

    pyautogui.write('Treinamento 01')
    time.sleep(1)


    if not find_and_click(salvar):
        logging.info('Sem Éxito para encontrar Salvar')
        return
    
    time.sleep(2)

def automacao_avaliacao_01():
    '''Executa uma nova automação passo a passo usando imagens de referência diferentes.'''
    logging.info("Iniciando a nova automação Avaliação 01...")

    if not find_and_click(cadas):
        logging.error(f'Localizando {cadas}, mas se não encontrar vou pular beleza.')
        if not find_and_click(cadas1):
            logging.error(f'Nao encontrei o {cadas1}. ')
    
    time.sleep(1)

    if not find_and_click(objeto1):
        logging.error("Infelizmente não encontrei o erro")
        if not find_and_click(objetored):
            logging.error("Infelizmento Não encontrei.")
            return
        
    time.sleep(1)

    if not find_and_click(scroll):
        logging.error("Nao encontrei")
        return

    time.sleep(1)

    if not find_and_click(interativeobject):
        logging.error("Nao achei")
        return

    time.sleep(2)

    if not find_and_click(namered):
        logging.error("nao achei o nome. LINHA 151")
        if not find_and_click(namewhite):
            logging.error("Nao achei o nome.Linha 153")

    time.sleep(1)

    pyautogui.write('Avaliacao 01')
    time.sleep(5)


    if not find_and_click(salvar):
        logging.info('Sem Éxito para encontrar Salvar')
        return

    time.sleep(2)

def automacao01():
    """Executa uma nova automação passo a passo usando imagens de referência diferentes."""
    logging.info("Iniciando a nova automação...")

    # Passo 1: Clicar em "Nova Ação"
    if not find_and_click(cadas):
        logging.error("Não foi possível clicar em 'cadastro'.")
        if not find_and_click(cadas1):
            return

    time.sleep(2)  # Espera para garantir que a nova tela esteja carregada

    # Passo 2: Selecionar um item específico
    if not find_and_click(objeto1):
        logging.error("Não foi possível clicar no item específico. Line 92")
        if not find_and_click(objetored):
            return

    time.sleep(3)  # Espera para garantir que o menu esteja visível

    # Passo 3: Preencher um campo com dados
    if not find_and_click(obj):
        logging.error("Não foi possível clicar no campo de dados.")
        return

    time.sleep(2)

    if not find_and_click(namered):
        logging.error("nao achei o nome. ")
        if not find_and_click(namewhite):
            logging.error("Nao achei o nome.")

    time.sleep(1) #ESPERAR UM POUCO

    pyautogui.write('01')
    time.sleep(1)  # Espera para garantir que o texto seja escrito

    # Passo 4: Confirmar a ação
    if not find_and_click(salvar):
        logging.error("Não foi possível clicar em 'salvar'.")
        return
    time.sleep(3)
    logging.info(f"Finalizei o cadastro da [automacao01] desta e vamos partir para a próxima...")

def automacao02():
    """Executa uma nova automação passo a passo usando imagens de referência diferentes."""
    logging.info("Iniciando a nova automação...")

    # Passo 1: Clicar em "Nova Ação"
    if not find_and_click(cadas):
        logging.error("Não foi possível clicar em 'cadastro'.")
        if not find_and_click(cadas1):
            return

    time.sleep(2)  # Espera para garantir que a nova tela esteja carregada

    # Passo 2: Selecionar um item específico
    if not find_and_click(objeto1):
        logging.error("Não foi possível clicar no item específico. Line 92")
        if not find_and_click(objetored):
            return

    time.sleep(3)  # Espera para garantir que o menu esteja visível

#     # Passo 3: Preencher um campo com dados
    if not find_and_click(obj):
        logging.error("Não foi possível clicar no campo de dados.")
        return

    time.sleep(2)

    if not find_and_click(namered):
        logging.error("nao achei o nome. ")
        if not find_and_click(namewhite):
            logging.error("Nao achei o nome.")

    time.sleep(1) #ESPERAR UM POUCO

    pyautogui.write('02')
    time.sleep(1)  # Espera para garantir que o texto seja escrito

#     # Passo 4: Confirmar a ação
    if not find_and_click(salvar):
        logging.error("Não foi possível clicar em 'salvar'.")
        return
    time.sleep(3)
    logging.info(f"Finalizei o cadastro da [automacao02] desta e vamos partir para a próxima...")

def automacao03():
    """Executa uma nova automação passo a passo usando imagens de referência diferentes."""
    logging.info("Iniciando a nova automação...")

    # Passo 1: Clicar em "Nova Ação"
    if not find_and_click(cadas):
        logging.error("Não foi possível clicar em 'cadastro'.")
        if not find_and_click(cadas1):
            return

    time.sleep(2)  # Espera para garantir que a nova tela esteja carregada

    # Passo 2: Selecionar um item específico
    if not find_and_click(objeto1):
        logging.error("Não foi possível clicar no item específico. Line 92")
        if not find_and_click(objetored):
            return

    time.sleep(3)  # Espera para garantir que o menu esteja visível

    # Passo 3: Preencher um campo com dados
    if not find_and_click(obj):
        logging.error("Não foi possível clicar no campo de dados.")
        return

    time.sleep(2)

    if not find_and_click(namered):
        logging.error("nao achei o nome. ")
        if not find_and_click(namewhite):
            logging.error("Nao achei o nome.")

    time.sleep(1) #ESPERAR UM POUCO

    pyautogui.write('03')
    time.sleep(1)  # Espera para garantir que o texto seja escrito

    # Passo 4: Confirmar a ação
    if not find_and_click(salvar):
        logging.error("Não foi possível clicar em 'salvar'.")
        return
    time.sleep(3)
    logging.info(f"Finalizei o cadastro da [automacao03] desta e vamos partir para a próxima...")

def automacao04():
    """Executa uma nova automação passo a passo usando imagens de referência diferentes."""
    logging.info("Iniciando a nova automação...")

#     # Passo 1: Clicar em "Nova Ação"
    if not find_and_click(cadas):
        logging.error("Não foi possível clicar em 'cadastro'.")
        if not find_and_click(cadas1):
            return

    time.sleep(2)  # Espera para garantir que a nova tela esteja carregada

#     # Passo 2: Selecionar um item específico
    if not find_and_click(objeto1):
        logging.error("Não foi possível clicar no item específico. Line 92")
        if not find_and_click(objetored):
            return

    time.sleep(3)  # Espera para garantir que o menu esteja visível

#     # Passo 3: Preencher um campo com dados
    if not find_and_click(obj):
        logging.error("Não foi possível clicar no campo de dados.")
        return

    time.sleep(2)

    if not find_and_click(namered):
        logging.error("nao achei o nome. ")
        if not find_and_click(namewhite):
            logging.error("Nao achei o nome.")

    time.sleep(1) #ESPERAR UM POUCO

    pyautogui.write('04')
    time.sleep(1)  # Espera para garantir que o texto seja escrito

#     # Passo 4: Confirmar a ação
    if not find_and_click(salvar):
        logging.error("Não foi possível clicar em 'salvar'.")
        return
    time.sleep(3)
    logging.info(f"Finalizei o cadastro da [automacao04] desta e vamos partir para a próxima...")

def automacao05():
    """Executa uma nova automação passo a passo usando imagens de referência diferentes."""
    logging.info("Iniciando a nova automação...")

    # Passo 1: Clicar em "Nova Ação"
    if not find_and_click(cadas):
        logging.error("Não foi possível clicar em 'cadastro'.")
        if not find_and_click(cadas1):
            return

    time.sleep(2)  # Espera para garantir que a nova tela esteja carregada

    # Passo 2: Selecionar um item específico
    if not find_and_click(objeto1):
        logging.error("Não foi possível clicar no item específico. Line 92")
        if not find_and_click(objetored):
            return

    time.sleep(2)  # Espera para garantir que o menu esteja visível

    # Passo 3: Preencher um campo com dados
    if not find_and_click(relation):
        logging.error("Não foi possível clicar no campo de dados.")
        return

    time.sleep(2)

    if not find_and_click(namered):
        logging.error("nao achei o nome. ")
        if not find_and_click(namewhite):
            logging.error("Nao achei o nome.")

    time.sleep(1) #ESPERAR UM POUCO

    pyautogui.write('Relacione as colunas')
    time.sleep(5)  # Espera para garantir que o texto seja escrito

    # Passo 4: Confirmar a ação
    if not find_and_click(salvar):
        logging.error("Não foi possível clicar em 'salvar'.")
        return
    time.sleep(3)
    logging.info(f"Finalizei o cadastro da [automacao05] desta e vamos partir para a próxima...")

def automacao06():
    """Executa uma nova automação passo a passo usando imagens de referência diferentes."""
    logging.info("Iniciando a nova automação...")

    # Passo 1: Clicar em "Nova Ação"
    if not find_and_click(cadas):
        logging.error("Não foi possível clicar em 'cadastro'.")
        if not find_and_click(cadas1):
            return

    time.sleep(2)  # Espera para garantir que a nova tela esteja carregada

    # Passo 2: Selecionar um item específico
    if not find_and_click(objeto1):
        logging.error("Não foi possível clicar no item específico. Line 92")
        if not find_and_click(objetored):
            return

    time.sleep(3)  # Espera para garantir que o menu esteja visível

    # Passo 3: Preencher um campo com dados
    if not find_and_click(preen):
        logging.error("Não foi possível clicar no campo de dados.")
        return

    time.sleep(2)

    if not find_and_click(namered):
        logging.error("nao achei o nome. ")
        if not find_and_click(namewhite):
            logging.error("Nao achei o nome.")

    time.sleep(1) #ESPERAR UM POUCO

    pyautogui.typewrite('Preencha os espacos', interval=0.1)
    time.sleep(5)  # Espera para garantir que o texto seja escrito

    # Passo 4: Confirmar a ação
    if not find_and_click(salvar):
        logging.error("Não foi possível clicar em 'salvar'.")
        return
    time.sleep(3)
    logging.info(f"Finalizei o cadastro da [automacao04] desta e vamos partir para a próxima...")

def automacao07():
    """Executa uma nova automação passo a passo usando imagens de referência diferentes."""
    logging.info("Iniciando a nova automação...")

#     # Passo 1: Clicar em "Nova Ação"
    if not find_and_click(cadas):
        logging.error("Não foi possível clicar em 'cadastro'.")
        if not find_and_click(cadas1):
            return

    time.sleep(2)  # Espera para garantir que a nova tela esteja carregada

#     # Passo 2: Selecionar um item específico
    if not find_and_click(objeto1):
        logging.error("Não foi possível clicar no item específico. Line 92")
        if not find_and_click(objetored):
            return

    time.sleep(3)  # Espera para garantir que o menu esteja visível

    # Passo 3: Preencher um campo com dados
    if not find_and_click(multipla):
        logging.error("Não foi possível clicar no campo de dados.")
        return

    time.sleep(2)

    if not find_and_click(namered):
        logging.error("nao achei o nome. ")
        if not find_and_click(namewhite):
            logging.error("Nao achei o nome.")

    time.sleep(1) #ESPERAR UM POUCO

    pyautogui.write('07')
    time.sleep(1)  # Espera para garantir que o texto seja escrito

#     # Passo 4: Confirmar a ação
    if not find_and_click(salvar):
        logging.error("Não foi possível clicar em 'salvar'.")
        return
    time.sleep(3)
    logging.info(f"Finalizei o cadastro da [automacao07] desta e vamos partir para a próxima...")

def automacao08():
    """Executa uma nova automação passo a passo usando imagens de referência diferentes."""
    logging.info("Iniciando a nova automação...")

    # Passo 1: Clicar em "Nova Ação"
    if not find_and_click(cadas):
        logging.error("Não foi possível clicar em 'cadastro'.")
        if not find_and_click(cadas1):
            return

    time.sleep(2)  # Espera para garantir que a nova tela esteja carregada

    # Passo 2: Selecionar um item específico
    if not find_and_click(objeto1):
        logging.error("Não foi possível clicar no item específico. Line 92")
        if not find_and_click(objetored):
            return

    time.sleep(3)  # Espera para garantir que o menu esteja visível

    # Passo 3: Preencher um campo com dados
    if not find_and_click(multipla):
        logging.error("Não foi possível clicar no campo de dados.")
        return

    time.sleep(2)

    if not find_and_click(namered):
        logging.error("nao achei o nome. ")
        if not find_and_click(namewhite):
            logging.error("Nao achei o nome.")

    time.sleep(1) #ESPERAR UM POUCO

    pyautogui.write('08')
    time.sleep(1)  # Espera para garantir que o texto seja escrito

    # Passo 4: Confirmar a ação
    if not find_and_click(salvar):
        logging.error("Não foi possível clicar em 'salvar'.")
        return
    time.sleep(3)
    logging.info(f"Finalizei o cadastro da [automacao08] desta e vamos partir para a próxima...")

    logging.info("Estou Indo para a proxima fase do cadastro de Estrutura.")

def automacao_passoapasso02():
    """Executa a automação passo a passo usando imagens de referência para localizar os elementos."""
    logging.info("Iniciando a automação passo a passo 01...")

    # Passo 1: Clicar em "Cadastrar"
    if not find_and_click(cadas):
        logging.error("Não foi possível clicar em 'Cadastrar'.")
        return

    time.sleep(2)  # Espera para garantir que o menu esteja carregado

    # Passo 2: Clicar em "Tipo de Objeto" e selecionar "Video"
    if not find_and_click(objeto):
        if not find_and_click(videoB):
            if not find_and_click(video):
                if not find_and_click(obj):
                    return

    time.sleep(1)  # Espera para garantir que o menu esteja visível

    # Tenta clicar em 'video.png' ou fallback para 'alternativa.png'
    if not find_and_click(video):
        logging.warning("Não foi possível encontrar 'video.png'. Tentando alternativa.")
        return

    time.sleep(2)  # Espera para garantir que o campo de nome esteja acessível

    # Passo 3: Clicar no campo "Nome" e preencher
    if not find_and_click(namewhite):
        logging.error("Não foi possível clicar no campo 'Nome'.")
        if not find_and_click(namered):
            logging.error("Não foi possível localizar o 'NomeBranc.png'.")
            return

    pyautogui.write('Passo a passo 02')
    time.sleep(1)  # Espera para garantir que o texto seja escrito

    # Passo 4: Clicar no campo "Conteúdo" e preencher
    if not find_and_click(cont):
        logging.error("Não foi possível clicar no campo 'Conteúdo'.")
        if not find_and_click(contB):
            logging.error("Não foi possível clicar no campo 'Conteúdo branco'.")
            return
            
    pyautogui.write('SEM LINK')
    time.sleep(1)  # Espera para garantir que o texto seja escrito

    # Passo 5: Salvar
    if not find_and_click(salvar):
        logging.error("Não foi possível clicar em 'Salvar'.")
        return

    time.sleep(2)  # Espera para garantir que o texto seja escrito

def automacao_treinamento02():
    """Executa uma nova automação passo a passo usando imagens de referência diferentes."""
    logging.info("Iniciando a nova automação treinamento 01...")

    if not find_and_click(cadas):
        logging.error('Nao encontrei o Cadastar. ')
        if not find_and_click(cadas1):
            logging.error('Nao encontrei o cadastrar1. ')
    
    time.sleep(1)

    if not find_and_click(objeto1):
        logging.error("Infelizmente não encontrei o erro")
        if not find_and_click(objetored):
            logging.error("Infelizmento Não encontrei o ObjetoRed")
            return
        
    time.sleep(1)

    if not find_and_click(scroll):
        logging.error("Nao encontrei")
        return

    time.sleep(1)

    if not find_and_click(interativeobject):
        logging.error("Nao achei")
        return

    time.sleep(2)

    if not find_and_click(namered):
        logging.error("nao achei o nome. LINHA 151")
        if not find_and_click(namewhite):
            logging.error("Nao achei o nome.Linha 153")

    time.sleep(1)

    pyautogui.write('Treinamento 02')
    time.sleep(1)


    if not find_and_click(salvar):
        logging.info('Sem Éxito para encontrar Salvar')
        return
    
    time.sleep(2)

def automacao_avaliacao_02():
    '''Executa uma nova automação passo a passo usando imagens de referência diferentes.'''
    logging.info("Iniciando a nova automação Avaliação 01...")

    if not find_and_click(cadas):
        logging.error(f'Localizando {cadas}, mas se não encontrar vou pular beleza.')
        if not find_and_click(cadas1):
            logging.error(f'Nao encontrei o {cadas1}. LINHA 110')
    
    time.sleep(1)

    if not find_and_click(objeto1):
        logging.error("Infelizmente não encontrei o erro")
        if not find_and_click(objetored):
            logging.error("Infelizmento Não encontrei o ObjetoRed")
            return
        
    time.sleep(1)

    if not find_and_click(scroll):
        logging.error("Nao encontrei")
        return

    time.sleep(1)

    if not find_and_click(interativeobject):
        logging.error("Nao achei")
        return

    time.sleep(2)

    if not find_and_click(namered):
        logging.error("nao achei o nome. LINHA 151")
        if not find_and_click(namewhite):
            logging.error("Nao achei o nome.Linha 153")

    time.sleep(1)

    pyautogui.write('Avaliacao 02')
    time.sleep(5)


    if not find_and_click(salvar):
        logging.info('Sem Éxito para encontrar Salvar')
        return

    time.sleep(2)

def automacao11():
    """Executa uma nova automação passo a passo usando imagens de referência diferentes."""
    logging.info("Iniciando a nova automação...")

    # Passo 1: Clicar em "Nova Ação"
    if not find_and_click(cadas):
        logging.error("Não foi possível clicar em 'cadastro'.")
        if not find_and_click(cadas1):
            return

    time.sleep(2)  # Espera para garantir que a nova tela esteja carregada

    # Passo 2: Selecionar um item específico
    if not find_and_click(objeto1):
        logging.error("Não foi possível clicar no item específico. Line 92")
        if not find_and_click(objetored):
            return

    time.sleep(3)  # Espera para garantir que o menu esteja visível

    # Passo 3: Preencher um campo com dados
    if not find_and_click(obj):
        logging.error("Não foi possível clicar no campo de dados.")
        return

    time.sleep(2)

    if not find_and_click(namered):
        logging.error("nao achei o nome. ")
        if not find_and_click(namewhite):
            logging.error("Nao achei o nome.")

    time.sleep(1) #ESPERAR UM POUCO

    pyautogui.write('01')
    time.sleep(1)  # Espera para garantir que o texto seja escrito

    # Passo 4: Confirmar a ação
    if not find_and_click(salvar):
        logging.error("Não foi possível clicar em 'salvar'.")
        return
    time.sleep(3)
    logging.info(f"Finalizei o cadastro da [automacao01] desta e vamos partir para a próxima...")

def automacao22():
    """Executa uma nova automação passo a passo usando imagens de referência diferentes."""
    logging.info("Iniciando a nova automação...")

    # Passo 1: Clicar em "Nova Ação"
    if not find_and_click(cadas):
        logging.error("Não foi possível clicar em 'cadastro'.")
        if not find_and_click(cadas1):
            return

    time.sleep(2)  # Espera para garantir que a nova tela esteja carregada

    # Passo 2: Selecionar um item específico
    if not find_and_click(objeto1):
        logging.error("Não foi possível clicar no item específico. Line 92")
        if not find_and_click(objetored):
            return

    time.sleep(3)  # Espera para garantir que o menu esteja visível

    # Passo 3: Preencher um campo com dados
    if not find_and_click(obj):
        logging.error("Não foi possível clicar no campo de dados.")
        return

    time.sleep(2)

    if not find_and_click(namered):
        logging.error("nao achei o nome. ")
        if not find_and_click(namewhite):
            logging.error("Nao achei o nome.")

    time.sleep(1) #ESPERAR UM POUCO

    pyautogui.write('02')
    time.sleep(1)  # Espera para garantir que o texto seja escrito

    # Passo 4: Confirmar a ação
    if not find_and_click(salvar):
        logging.error("Não foi possível clicar em 'salvar'.")
        return
    time.sleep(3)
    logging.info(f"Finalizei o cadastro da [automacao02] desta e vamos partir para a próxima...")

def automacao33():
    """Executa uma nova automação passo a passo usando imagens de referência diferentes."""
    logging.info("Iniciando a nova automação...")

    # Passo 1: Clicar em "Nova Ação"
    if not find_and_click(cadas):
        logging.error("Não foi possível clicar em 'cadastro'.")
        if not find_and_click(cadas1):
            return

    time.sleep(2)  # Espera para garantir que a nova tela esteja carregada

    # Passo 2: Selecionar um item específico
    if not find_and_click(objeto1):
        logging.error("Não foi possível clicar no item específico. Line 92")
        if not find_and_click(objetored):
            return

    time.sleep(3)  # Espera para garantir que o menu esteja visível

    # Passo 3: Preencher um campo com dados
    if not find_and_click(obj):
        logging.error("Não foi possível clicar no campo de dados.")
        return

    time.sleep(2)

    if not find_and_click(namered):
        logging.error("nao achei o nome. ")
        if not find_and_click(namewhite):
            logging.error("Nao achei o nome.")

    time.sleep(1) #ESPERAR UM POUCO

    pyautogui.write('03')
    time.sleep(1)  # Espera para garantir que o texto seja escrito

    # Passo 4: Confirmar a ação
    if not find_and_click(salvar):
        logging.error("Não foi possível clicar em 'salvar'.")
        return
    time.sleep(3)
    logging.info(f"Finalizei o cadastro da [automacao03] desta e vamos partir para a próxima...")

def automacao44():
    """Executa uma nova automação passo a passo usando imagens de referência diferentes."""
    logging.info("Iniciando a nova automação...")

     # Passo 1: Clicar em "Nova Ação"
    if not find_and_click(cadas):
        logging.error("Não foi possível clicar em 'cadastro'.")
        if not find_and_click(cadas1):
            return

    time.sleep(2)  # Espera para garantir que a nova tela esteja carregada

     # Passo 2: Selecionar um item específico
    if not find_and_click(objeto1):
        logging.error("Não foi possível clicar no item específico. Line 92")
        if not find_and_click(objetored):
            return

    time.sleep(3)  # Espera para garantir que o menu esteja visível

#     # Passo 3: Preencher um campo com dados
    if not find_and_click(obj):
        logging.error("Não foi possível clicar no campo de dados.")
        return

    time.sleep(2)

    if not find_and_click(namered):
        logging.error("nao achei o nome. ")
        if not find_and_click(namewhite):
            logging.error("Nao achei o nome.")

    time.sleep(1) #ESPERAR UM POUCO

    pyautogui.write('04')
    time.sleep(1)  # Espera para garantir que o texto seja escrito

#     # Passo 4: Confirmar a ação
    if not find_and_click(salvar):
        logging.error("Não foi possível clicar em 'salvar'.")
        return
    time.sleep(3)
    logging.info(f"Finalizei o cadastro da [automacao04] desta e vamos partir para a próxima...")

def automacao55():
    """Executa uma nova automação passo a passo usando imagens de referência diferentes."""
    logging.info("Iniciando a nova automação...")

    # Passo 1: Clicar em "Nova Ação"
    if not find_and_click(cadas):
        logging.error("Não foi possível clicar em 'cadastro'.")
        if not find_and_click(cadas1):
            return

    time.sleep(2)  # Espera para garantir que a nova tela esteja carregada

    # Passo 2: Selecionar um item específico
    if not find_and_click(objeto1):
        logging.error("Não foi possível clicar no item específico. Line 92")
        if not find_and_click(objetored):
            return

    time.sleep(3)  # Espera para garantir que o menu esteja visível

    # Passo 3: Preencher um campo com dados
    if not find_and_click(relation):
        logging.error("Não foi possível clicar no campo de dados.")
        return

    time.sleep(2)

    if not find_and_click(namered):
        logging.error("nao achei o nome. ")
        if not find_and_click(namewhite):
            logging.error("Nao achei o nome.")

    time.sleep(1) #ESPERAR UM POUCO

    pyautogui.write('Relacione as colunas')
    time.sleep(5)  # Espera para garantir que o texto seja escrito

    # Passo 4: Confirmar a ação
    if not find_and_click(salvar):
        logging.error("Não foi possível clicar em 'salvar'.")
        return
    time.sleep(3)
    logging.info(f"Finalizei o cadastro da [automacao05] desta e vamos partir para a próxima...")

def automacao66():
    """Executa uma nova automação passo a passo usando imagens de referência diferentes."""
    logging.info("Iniciando a nova automação...")

    # Passo 1: Clicar em "Nova Ação"
    if not find_and_click(cadas):
        logging.error("Não foi possível clicar em 'cadastro'.")
        if not find_and_click(cadas1):
            return

    time.sleep(2)  # Espera para garantir que a nova tela esteja carregada

    # Passo 2: Selecionar um item específico
    if not find_and_click(objeto1):
        logging.error("Não foi possível clicar no item específico. Line 92")
        if not find_and_click(objetored):
            return

    time.sleep(3)  # Espera para garantir que o menu esteja visível

    # Passo 3: Preencher um campo com dados
    if not find_and_click(preen):
        logging.error("Não foi possível clicar no campo de dados.")
        return

    time.sleep(2)

    if not find_and_click(namered):
        logging.error("nao achei o nome. ")
        if not find_and_click(namewhite):
            logging.error("Nao achei o nome.")

    time.sleep(1) #ESPERAR UM POUCO

    pyautogui.typewrite('Preencha os espacos', interval=0.1)
    time.sleep(5)  # Espera para garantir que o texto seja escrito

    # Passo 4: Confirmar a ação
    if not find_and_click(salvar):
        logging.error("Não foi possível clicar em 'salvar'.")
        return
    time.sleep(3)
    logging.info(f"Finalizei o cadastro da [automacao04] desta e vamos partir para a próxima...")

def automacao77():
    """Executa uma nova automação passo a passo usando imagens de referência diferentes."""
    logging.info("Iniciando a nova automação...")

#     # Passo 1: Clicar em "Nova Ação"
    if not find_and_click(cadas):
        logging.error("Não foi possível clicar em 'cadastro'.")
        if not find_and_click(cadas1):
            return

    time.sleep(2)  # Espera para garantir que a nova tela esteja carregada

    # Passo 2: Selecionar um item específico
    if not find_and_click(objeto1):
       logging.error("Não foi possível clicar no item específico. Line 92")
       if not find_and_click(objetored):
        return

    time.sleep(3)  # Espera para garantir que o menu esteja visível

#     # Passo 3: Preencher um campo com dados
    if not find_and_click(multipla):
        logging.error("Não foi possível clicar no campo de dados.")
        return

    time.sleep(2)

    if not find_and_click(namered):
        logging.error("nao achei o nome. ")
        if not find_and_click(namewhite):
            logging.error("Nao achei o nome.")

    time.sleep(1) #ESPERAR UM POUCO

    pyautogui.write('07')
    time.sleep(1)  # Espera para garantir que o texto seja escrito

    # Passo 4: Confirmar a ação
    if not find_and_click(salvar):
        logging.error("Não foi possível clicar em 'salvar'.")
        return
    time.sleep(3)
    logging.info(f"Finalizei o cadastro da [automacao07] desta e vamos partir para a próxima...")

def automacao88():
    """Executa uma nova automação passo a passo usando imagens de referência diferentes."""
    logging.info("Iniciando a nova automação...")

    # Passo 1: Clicar em "Nova Ação"
    if not find_and_click(cadas):
        logging.error("Não foi possível clicar em 'cadastro'.")
        if not find_and_click(cadas1):
            return

    time.sleep(2)  # Espera para garantir que a nova tela esteja carregada

    # Passo 2: Selecionar um item específico
    if not find_and_click(objeto1):
        logging.error("Não foi possível clicar no item específico. Line 92")
        if not find_and_click(objetored):
            return

    time.sleep(3)  # Espera para garantir que o menu esteja visível

    # Passo 3: Preencher um campo com dados
    if not find_and_click(multipla):
        logging.error("Não foi possível clicar no campo de dados.")
        return

    time.sleep(2)

    if not find_and_click(namered):
        logging.error("nao achei o nome. ")
        if not find_and_click(namewhite):
            logging.error("Nao achei o nome.")

    time.sleep(1) #ESPERAR UM POUCO

    pyautogui.write('08')
    time.sleep(1)  # Espera para garantir que o texto seja escrito

    # Passo 4: Confirmar a ação
    if not find_and_click(salvar):
        logging.error("Não foi possível clicar em 'salvar'.")
        return
    time.sleep(3)
    logging.info(f"FINALIZEI O CADASTRO DESTA AULA CHEFE!")
    tkinter.messagebox.showinfo(title='AVISO', message='FINALIZEI O CADASTRO DESTA AULA CHEFE!')

    #alert(text=f"TERMINEI A ESTRUTURA AQUI MÁRIO, VALEU!!", title='Aviso', button='Valeu')

logging.info('BORA CADASTRAR A PROXIMA AULA')
time.sleep(3)



# def aula_2():

#     if not find_and_click(aula):
#         logging.error('Nao encontrei essa AULA 2')
#         if not find_and_click(aula2):
#             return

# time.sleep(10)

# passo01()
# passo02()
# passo03()
# passo04()
# passo05()
# passo06()
# passo07()
# passo08()

# passo09()
# passo10()
# passo11()
# passo12()
# passo13()
# passo14()
# passo15()
# passo16()
# passo18()
# passo19()
# passo20()


if __name__ == "__main__":
    automacao_passoapasso01()
    automacao_treinamento01()
    automacao_avaliacao_01()
    automacao01()
    automacao02()
    automacao03()    
    automacao04()
    automacao05()
    automacao06()
    automacao07()
    automacao08()
    automacao_passoapasso02()
    automacao_treinamento02()
    automacao_avaliacao_02()
    automacao01()
    automacao22()
    automacao33()    
    automacao44()
    automacao55()
    automacao66()
    automacao77()
    automacao88()
    #aula_2()