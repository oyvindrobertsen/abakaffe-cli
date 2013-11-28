# CLI for [kaffe.abakus.no](http://kaffe.abakus.no)

## Installasjon

    pip install abakaffe-cli 

Mest sannsynlig har du lyst å skrive sudo foran den linja.

## Eksempel

    $ abakaffe
    Kaffe ble sist traktet for 4 timer og 57 minutter siden.
    $ abakaffe --stats
    Kaffe ble sist traktet for 4 timer og 58 minutter siden.
    2013-11-26 |### 3
    2013-11-27 |############# 13
    $ abakaffe --ascii
               _           _          __  __
         /\   | |         | |        / _|/ _|
        /  \  | |__   __ _| | ____ _| |_| |_ ___
       / /\ \ | '_ \ / _` | |/ / _` |  _|  _/ _ \
      / ____ \| |_) | (_| |   < (_| | | | ||  __/
     /_/    \_\_.__/ \__,_|_|\_\__,_|_| |_| \___|

    Kaffe ble sist traktet for 4 timer og 58 minutter siden.

## Hvilke valg har jeg?

    $ abakaffe --help
    usage: abakaffe-cli [-h] [-a] [-s] [-o] [--version]

    When was the coffee brewed?

    optional arguments:
      -h, --help    show this help message and exit
      -a, --ascii   prints the Abakaffe ascii-art
      -s, --stats   prints a graph displaying Abakus' coffee consumption
      -o, --online  should I go one floor down to Online?
      --version     prints the abakaffe-cli version number