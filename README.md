# WAB - World in A Box

## Operazioni preliminari
---

### utente e password

```
utente: unter
password: wasser
```

### abilitare ssh

Procedura:

- Andare sul lampone in basso a sinistra
- scegliere la voce **Preferenze**
- scegliere la vode **Configurazione di Raspberry Pi**
- Andare su **Interfacce** e abilitare la voce **ssh**

### aggiornamento

```bash
sudo apt update
sudo apt full-upgrade
```

### stress test

```bash
sudo apt install stress
```

```bash
while true; do vcgencmd measure_clock arm; vcgencmd measure_temp; sleep 10; done& stress -c 4 -t 900s
```

### audio

Assicurarsi che l'uscita sia effettivamente **Headphone**:

```bash
sudo raspi-config
```

andare in **1 System Options/S2 Audio** e scegliere **Headphone**

### Disabilitare lo spegnimento del monitor

Procedura:

- Andare sul lampone in basso a sinistra
- scegliere la voce **Preferenze**
- scegliere la vode **Configurazione di Raspberry Pi**
- Andare su **Schermo** e disabilitare la voce **Spegnimento schermo**

### Disabilitare il wifi e il bluetooth (opzionale)

Nel file `/boot/config.txt` aggiungere in basso, dopo la riga `[all]` le seguenti linee:

```
dtoverlay=disable-wifi
dtoverlay=disable-bt
```

salva e riavvia.

*N.B. Cancella queste due righe per riavviare i servizi*

### Creare un collegamento della cartella dei video sul Desktop 

```bash
ln -s ~/Documenti/world_in_a_box/VIDEO/ VIDEO
```

### installare mpv

#### sistema

```bash
sudo apt install mpv libmpv-dev 
```

#### python (version 0.5.2)

```bash
pip3 install python-mpv==0.5.2
```

### Attivare wab all'avvio di raspi

Copiare i file **wab_main.desktop** e **web_worker.desktop** nella cartella `/etc/xdg/autostart/`. 
Riavviare per verificare l'attivazione al *boot*

## Comportamento di WAB
---

All'accensione del **Raspberry** l'applicazione si attiva automaticamente. Un breve conto alla rovescia avverte dell'avvenuto caricamento del software.

Alla pressione di uno dei due tasti principali (1 e/o 2) il video parte e i tasti vengono momentaneamente disattivati durante la riproduzione. 

Al termine della riproduzione i tasti tornano in ascolto.

Il tasto 3 (tasto di regia) ha due funzioni:

1.  Mettere in pausa o riprendere la riproduzione di un video (pressione breve)
2.  Spegnere/riaccendere l'applicazione (pressione lunga, circa due secondi)


## Impostazione e caricamento dei video da riprodurre
---

I video da riprodurre risiedono nella cartella **VIDEO**, collegata sul Desktop all'omonimo link. Si possono cambiare i video a piacimento, l'importante è che il nome dei due file da riprodurre inizi, rispettivamente, con il prefisso **1_** e **2_**.

Il file col prefisso **1_** sarà associato al **tasto 1**, l'altro al **tasto 2**.

Esempio: ho due video che si chiamano rispettivamente, *pippo.mp4* e *pluto.mp4*. Intendo associare pippo.mp4 al tasto 1 e pluto.mp4 al tasto 2. Rinomino quindi i due file in questo modo:

*   1_pippo.mp4
*   2_pluto.mp4

e copio i file nella cartella VIDEO.

*N.B. Preferibilmente è bene non avere altri file all'interno della cartella VIDEO.*

Consiglio per portare i video su raspberry:
- usare una chiavetta USB

## Accendere e spegnere raspi

---

Per accendere raspi è sufficiente alimentarla, quindi nel caso di un cavo dotato di interruttore, basta spostare la levetta per accenderlo. 

Per spegnere raspi si può usare la stessa procedura al contrario, ma sarebbe preferibile spegnere prima il sistema operativo. Per fare questo:

- chiudere l'applicazione WAB tenendo premuto il pulsante di regia per un paio di secondi
- fare *tap* sul lampone in basso a sinistra del Desktop
- scegliere dal menu la voce **chiudi sessione**
- nella nuova finestra che compare (entro un paio di secondi) fare *tap* su **arresta**
- attendere qualche secondo e spegnere la corrente



