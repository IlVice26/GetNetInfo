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
import sys, wmi

def main():
    argv = sys.argv

    if len(argv) < 2 or len(argv) > 3:  #Controllo degli argomenti
        print('Errore')
    else:
        if argv[1] == '-n':             # Se l'argomento è -n
            enabledNetworkAdapter()     # Avvia la funzione "Schede abilitate"
        elif argv[1] == '-y':           # Se l'arogmento è -y
            allNetworkAdapter()         # Avvia la funzione "Tutte le schede"
        else:                           # Se l'argomento è sbagliato
            print('Errore')              # Stampa "Errore"

def enabledNetworkAdapter():
    """
    Questa funzione stampa a video tutte le informazioni delle
    schede abilitate
    """
    strComputer = "."
    objWMIService = wmi.WMI()
    colItems = "SELECT * FROM Win32_NetworkAdapterConfiguration"

    for i in objWMIService.query(colItems):
        #Controllo se la scheda di rete è attiva
        if i.IPEnabled == True:
            #Nome scheda di rete
            print("\n" + str(i.Index) + ") " + i.Description)

            #DHCP
            if i.DHCPEnabled != None:
                print(" DHCP ENABLED: " + str(i.DHCPEnabled))
            if i.DHCPEnabled == True:
                print(" DCHP Domain: " + str(i.DHCPServer[0]))

            #DNS Domain
            if i.DNSHostName != None:
                print(" DNS Hostname: " + i.DNSHostName)

            #IP
            print(" IP: " + i.IPAddress[0])
            if i.IPXAddress != None:
                print(" IPX Address: " + i.IPXAddress)
            if i.IPSubnet != None:
                print(" IP Subnet: " + i.IPSubnet[0])
            

            #Mac Address
            if i.MACAddress != None:
                print(" MAC Address: " + i.MACAddress)
            
            
def allNetworkAdapter():
    """
    Questa funzione stampa a video tutte le informazioni di tutte
    le schede presenti
    """
    strComputer = "."
    objWMIService = wmi.WMI()
    colItems = "SELECT * FROM Win32_NetworkAdapterConfiguration"

    for i in objWMIService.query(colItems):
        #Nome scheda di rete
        print("\n" + str(i.Index) + ") " + i.Description)

        #DHCP
        print(" DHCP ENABLED: " + str(i.DHCPEnabled))
        if i.DHCPEnabled == True:
            if i.DHCPServer != None:
                print(" DCHP Domain: " + i.DHCPServer[0])

        #DNS Domain
        if i.DNSHostName != None:
            print(" DNS Hostname: " + i.DNSHostName)

        #IP
        if i.IPAddress != None:
            print(" IP: " + i.IPAddress[0])
        if i.IPXAddress != None:
            print(" IPX Address: " + i.IPXAddress)
        if i.IPSubnet != None:
            print(" IP Subnet: " + i.IPSubnet[0])

        #Mac Address
        if i.MACAddress != None:
            print(" MAC Address: " + i.MACAddress)
            

if __name__ == '__main__':
    main()
