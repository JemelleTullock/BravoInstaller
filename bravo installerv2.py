import os
import sys


print("*These applications are being installed from entwsopapp01*")

software_options = [
    {
        'name': 'Bravo Cage',
        'items': [
            {'name': 'Bravo Cage', 'path': r'\\entwsopapp01\GenesisBravo\Current Bravo Installs\Bravo Cage\BravoCageSetup.msi'},
            
        ]
    },
    {
        'name': 'Bravo Kiosk',
        'items': [
            {'name': 'Bravo Kiosk', 'path': r'\\entwsopapp01\GenesisBravo\Current Bravo Installs\Bravo Kiosk\BravoKiosk2.1.66Release'}
        ]
    },
    {
        'name': 'Bravo Reports',
        'items': [
            {'name': 'Bravo Reports', 'path': r'\\entwsopapp01\GenesisBravo\Current Bravo Installs\Bravo Reports\BravoReportSetup.msi'}
        ]
    },
    {
        'name': 'Card Watch',
        'items': [
            {'name': 'Card Watch', 'path': r'\\entwsopapp01\GenesisBravo\Current Bravo Installs\Cardwatch\Setup\CardWatchSetup.msi'}
        ]
    },
    {
        'name': 'Tournament Clock',
        'items': [
            {'name': 'Tournament Clock', 'path': r'\\entwsopapp01\GenesisBravo\Current Bravo Installs\Tournament Clock\BravoTournamentClock2.2.54Release.exe'}
        ]
    },
    {
        'name': 'Tournament Payment',
        'items': [
            {'name': 'Tournament Payment', 'path': r'\\entwsopapp01\GenesisBravo\Current Bravo Installs\TournamentPayment\TournamentPayment2.1.12Release.exe'}
        ]
    },
    {
        'name': 'Tournament Watch',
        'items': [
            {'name': 'Tournament Watch', 'path': r'\\entwsopapp01\GenesisBravo\Current Bravo Installs\TournamentWatch\Setup\TournamentWatchSetup.msi'}
        ]
    },
    {
        'name': 'Java ERM',
        'items': [
            {'name': 'Java ERM', 'path': r'\\reglvblade1fs\LVITOPS\Software\Java\ERM\jre-8u144-i586.exe'}
        ]
    },
    {
        'name': 'Crystal 2011 Runtime',
        'items': [
            {'name': 'Crystal 2011 Runtime', 'path': r'\\entwsopapp01\GenesisBravo\Current Bravo Installs\Crystal 2011 Runtime (.NET 4.7.2)\CRRuntime_32bit_13_0_22.msi\Crystal10RDC.msi'}
        ]
    },
    {
        'name': 'SQL Native Client',
        'items': [
            {'name': 'SQL Native Client', 'path': r'\\entwsopapp01\GenesisBravo\Current Bravo Installs\SQL Native Client 11.0.7001.0\64Bit\sqlncli.msi'}
        ]
    },
    {
        'name': 'All Bravo except Kiosk and Clock',
        'items': [
            {'name': 'Bravo Cage', 'path': r'\\entwsopapp01\GenesisBravo\Current Bravo Installs\Bravo Cage\BravoCageSetup.msi'},
            {'name': 'Bravo Reports', 'path': r'\\entwsopapp01\GenesisBravo\Current Bravo Installs\Bravo Reports\BravoReportSetup.msi'},
            {'name': 'Card Watch', 'path': r'\\entwsopapp01\GenesisBravo\Current Bravo Installs\Cardwatch\Setup\CardWatchSetup.msi'},
            {'name': 'Tournament Payment', 'path': r'\\entwsopapp01\GenesisBravo\Current Bravo Installs\TournamentPayment\TournamentPayment2.1.12Release.exe'},
            {'name': 'Tournament Watch', 'path': r'\\entwsopapp01\GenesisBravo\Current Bravo Installs\TournamentWatch\Setup\TournamentWatchSetup.msi'}
            
            
            
            
            
        ]
    }
]

def install_software(software_options, selected_options):
    for i, option in enumerate(software_options):
        if i in selected_options:
            for item in option['items']:
                print(f"Installing {item['name']}...")
                if item['path'].startswith('http'):
                    status = os.system(f"start {item['path']}")
                else:
                    status = os.system(f"start \"\" \"{item['path']}\"")
                if status != 0:
                    print(f"Installation of {item['name']} failed")
                    choice = input("Do you want to install another application? (Y/N): ")
                    if choice.lower() == 'n':
                        sys.exit()
                    else:
                        break

def prompt_options():
    print("Please select the software options to install:")
    for i, option in enumerate(software_options):
        print(f"{i+1}. {option['name']}")
    selected_options = input("Enter the option numbers separated by commas: ")
    selected_options = [int(opt)-1 for opt in selected_options.split(',')]
    return selected_options

while True:
    selected_options = prompt_options()
    install_software(software_options, selected_options)
    choice = input("Do you want to install another application? (Y/N): ")
    if choice.lower() == 'n':
        break
