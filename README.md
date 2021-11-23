# YahooStock

Simple program to download data (open close high low volume) from Yahoo finance using a list of symbols.
Recent updates to Yahoo Finance have meant that a header must now be sent along with the request, as such some older versions of Yahoo Finance tools may not work.

Specify a list of symbols in a csv format with the symbol name as the first column. Then run with

```
python main.py -d ./downloads/ -s ./symbol_list.csv
```
