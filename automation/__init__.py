import pyautogui
import time
import logging
import tkinter as tk
from tkinter import messagebox

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

IMG_CADASTRAR = "cadastrar.png"
IMG_CADASTRAR_B = "cadastrar1.png"
IMG_CONTENT = "conteudo.png"
IMG_CONTENT_B = "conteudoBran.png"
IMG_MULTIPLE = "multipla.png"
IMG_NOME_BRANCO = "NomeBranc.png"
IMG_NOME_VERMELHO = "NomeRed.png"
IMG_OBJETIVA = "Objetiva.png"
IMG_OBJETO = "Objeto.png"
IMG_OBJETO_PRETO = "ObjetoBlack.png"
IMG_OBJETO_INTERATIVO = "objetoINTERATIVO.png"
IMG_OBJETO_VERMELHO = "ObjetoRed.png"
IMG_PREENCHA = "Preencha.png"
IMG_RELACIONE = "Relacione.png"
IMG_SALVAR = "salvar.png"
IMG_SCROLL = "scroll.png"
IMG_VIDEO = "video.png"
IMG_VIDEO_B = "videoBranc.png"
IMG_AULA = "Aula2.png"
IMG_AULA_B = "Aula22.png"

TIMEOUT = 2  # Tempo de espera para localizar a imagem na tela
ATTEMPTS = 3  # Número de tentativas para localizar a imagem na tela
IMAGE_PATH = "images"  # Caminho para as imagens


def run_automation():
    root = tk.Tk()
    root.withdraw()  # Esconde a janela principal
    user_response = messagebox.askyesno(
        "Iniciar Automação?",
        "Antes de iniciar o site deve estar com zoom de 75% e a aula desejada deve estar selecionada",
    )
    if user_response:
        try:
            # Video Aula 1
            record_step_by_step("Passo a passo 01")
            # Interatividade 01
            record_activity(IMG_OBJETO_INTERATIVO, "Treinamento 01", scroll=True)
            # Interatividade 02
            record_activity(IMG_OBJETO_INTERATIVO, "Avaliação 01", scroll=True)
            # Atividade 01..04
            for num in range(1, 5):
                record_activity(IMG_OBJETIVA, f"{num:02d}")
            # Atividade 05
            record_activity(IMG_RELACIONE, "Relacione as colunas")
            # Atividade 06
            record_activity(IMG_PREENCHA, "Preencha os espaços")
            # Atividade 07
            record_activity(IMG_MULTIPLE, "07")
            # Atividade 08
            record_activity(IMG_MULTIPLE, "08")
            # Video Aula 2
            record_step_by_step("Passo a passo 02")
        except ValueError as exc:
            logging.error("Erro ao executar a automação: %s", exc)
    else:
        logging.info("Usuário cancelou a automação.")

    root.destroy()  # Fecha a janela principal


def find_and_click(
    image_name: str, confidence: float = 0.8, *, raise_error: bool = False
) -> bool:
    """Localiza uma imagem na tela e clica nela."""
    for attempt in range(ATTEMPTS):
        # Localiza o centro da imagem na tela
        location = pyautogui.locateCenterOnScreen(image_name, confidence=confidence)
        if location:
            logging.info(
                f"Imagem '{IMAGE_PATH}\{image_name}' localizada em: {location}"
            )
            pyautogui.click(location)
            time.sleep(TIMEOUT)  # Espera para garantir que a ação seja concluída
            return True

        logging.info(f"'{image_name}' não encontrada. [{attempt + 1}/{ATTEMPTS}]")

    logging.error(f"Imagem '{image_name}' não encontrada após {ATTEMPTS} tentativas.")

    if raise_error:
        raise ValueError(f"Imagem '{image_name}' não encontrada.")
    return False


def record_step_by_step(title: str, link: str = "Sem link"):
    """Executa a automação passo a passo usando imagens de referência para localizar os elementos."""
    logging.info("Iniciando a automação passo a passo 01...")

    # Passo 1: Clicar em "Cadastrar"
    find_and_click(IMG_CADASTRAR, raise_error=False)

    if (
        not find_and_click(IMG_OBJETO)
        and not find_and_click(IMG_VIDEO_B)
        and not find_and_click(IMG_VIDEO)
    ):
        find_and_click(IMG_OBJETIVA, raise_error=True)

    find_and_click(IMG_VIDEO, raise_error=False)

    click_name()
    pyautogui.write(title)
    time.sleep(1)  # Espera para garantir que o texto seja escrito

    # Passo 4: Clicar no campo "Conteúdo" e preencher
    if not find_and_click(IMG_CONTENT):
        find_and_click(IMG_CONTENT_B, raise_error=True)

    pyautogui.write(link)

    # Passo 5: Salvar
    find_and_click(IMG_SALVAR, raise_error=True)


def click_cadastrar():
    if not find_and_click(IMG_CADASTRAR):
        find_and_click(IMG_CADASTRAR_B, raise_error=True)

    if not find_and_click(IMG_OBJETO_PRETO):
        find_and_click(IMG_OBJETO_VERMELHO, raise_error=True)


def click_name():
    if not find_and_click(IMG_NOME_VERMELHO):
        find_and_click(IMG_NOME_BRANCO, raise_error=True)


def record_activity(
    image: str, text: str = "Relacione as colunas", *, scroll: bool = False
) -> None:
    """Executa uma nova automação passo a passo usando imagens de referência diferentes."""
    click_cadastrar()
    if scroll:
        find_and_click(IMG_SCROLL, raise_error=True)
    find_and_click(image, raise_error=True)
    click_name()
    pyautogui.write(text)
    find_and_click(IMG_SALVAR, raise_error=True)


if __name__ == "__main__":
    run_automation()
