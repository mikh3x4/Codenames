# Codenames

A computerized implementation of the fantastic [Codenames](https://en.wikipedia.org/wiki/Codenames_(board_game)) writen in pure python.

## Usage

You use one computer as the codemasters computer and another one as the game board everyone sees. The codemasters can mark the words as revelead by clicking on them. All communications happens over UDP boardcast so the two computers need to be on the same WiFi network using a slightly modified verision of hte [UDPComms](https://github.com/stanfordroboticsclub/UDP…) library.

## Running

The project has only been tested on a mac. The is a zipped app bundle avalible to download.

## Building

Install the [Platypus](https://sveinbjorn.org/platypus) command line tools and just run `make`.

## Languages

By defualt the game is in english but it also comes with polish language cards (The were translated using google translate :P). To run the game using the polish cards change the import statement at the top of `codemaster.py`. Alternately just download the polish zip
