# toast-ponto-reminder
Cria lembrete para bater o ponto com notificação do windows em quatro horários:

09:00

12:00

13:00

18:00


Para que essa aplicação rode ao inicializar o windows, é só seguir o passo a passo abaixo:

* pressione **Win+R**

* digite **shell:startup**

* arraste o arquivo python `meu_script.py` para dentro da pasta
  * se você não precisa do console: altere a extensão do arquivo de *meu_script.py* para *meu_script.pyw*
  * se não: crie `run_my_script.cmd` com `python path\to\your\my_script.py`
