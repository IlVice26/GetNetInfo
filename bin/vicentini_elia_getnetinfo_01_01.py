# -*- coding: cp1252 -*-
"""
Si vuole monitorare la configurazione
(attributi che si ritengono significativi) delle schede di rete
installate sul computer locale e remoti accedendo alla classe
CIM, NetAdapterConfiguration. Il programma python getnetinfo.py avrà
il parametro enalbe in ingresso con cui decidere se monitorare le
informaznio delle schede abilitate (parametro -y) o se trattare le
informazioni di tutte le schede presenti (-n).

L'output del programma è un file di testo csv con le informazioni
delle configurazione recuperate oltre a nomemacchina e timestamp.

@author Vicentini Elia
@version 0.1
"""
import sys, wmi, socket, datetime, time

def main():
    argv = sys.argv
    f = open('getnetinfo.csv', 'w+')

    if len(argv) < 2 or len(argv) > 3:  #Controllo degli argomenti
        print('Errore')
    else:
        if argv[1] == '-n':             # Se l'argomento è -n
            enabledNetworkAdapter(f)     # Avvia la funzione 'Schede abilitate'
        elif argv[1] == '-y':           # Se l'arogmento è -y
            allNetworkAdapter(f)         # Avvia la funzione 'Tutte le schede'
        else:                           # Se l'argomento è sbagliato
            print('Errore, argomento non valido')    # Stampa 'Errore'

def enabledNetworkAdapter(f):
    """
    Questa funzione stampa a video tutte le informazioni delle
    schede abilitate
    """
    strComputer = '.'
    objWMIService = wmi.WMI()
    colItems = 'SELECT * FROM Win32_NetworkAdapterConfiguration'

    hostname = socket.gethostname()
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    f.write('Nome macchina: ' + hostname + '  ' + st)
    
    for i in objWMIService.query(colItems):
        #Controllo se la scheda di rete è attiva
        if i.IPEnabled == True:
            #Nome scheda di rete
            f.write('\n' + str(i.Index) + ') ' + i.Description)

            #DHCP
            if i.DHCPEnabled == True:
                if i.DHCPServer != None:
                    f.write('\n DCHP Domain: ' + i.DHCPServer)

            #DNS Domain
            if i.DNSHostName != None:
                f.write('\n DNS Hostname: ' + i.DNSHostName)

            #IP
            f.write('\n IP: ' + i.IPAddress[0])
            if i.IPXAddress != None:
                f.write('\n IPX Address: ' + i.IPXAddress)
            if i.IPSubnet != None:
                f.write('\n Subnet Mask: ' + i.IPSubnet[0])
            

            #Mac Address
            if i.MACAddress != None:
                print('\n MAC Address: ' + i.MACAddress)

            f.write('\n')
            
            
def allNetworkAdapter(f):
    """
    Questa funzione stampa a video tutte le informazioni di tutte
    le schede presenti
    """
    strComputer = '.'
    objWMIService = wmi.WMI()
    colItems = 'SELECT * FROM Win32_NetworkAdapterConfiguration'

    hostname = socket.gethostname()
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    f.write('Nome macchina: ' + hostname + '  ' + st + '\n')
    
    for i in objWMIService.query(colItems):
        #Nome scheda di rete
        f.write('\n' + str(i.Index) + ') ' + i.Description)

        #DHCP
        if i.DHCPEnabled == True:
            if i.DHCPServer != None:
                f.write('\n DCHP Domain: ' + i.DHCPServer)

        #DNS Domain
        if i.DNSHostName != None:
            f.write('\n DNS Hostname: ' + i.DNSHostName)

        #IP
        if i.IPAddress != None:
            f.write('\n IP: ' + i.IPAddress[0])
        if i.IPXAddress != None:
            f.write('\n IPX Address: ' + i.IPXAddress)
        if i.IPSubnet != None:
            f.write('\n Subnet Mask: ' + i.IPSubnet[0])

        #Mac Address
        if i.MACAddress != None:
            f.write('\n MAC Address: ' + i.MACAddress)

        f.write('\n')
            

if __name__ == "__main__":
    main()
    print("Stop")

