# csvTextModifier
### Transforms related field to gibberish/random data, csv version of xmlTextModifier
This project was written for mdit transformation ( randomisation of csv data ).  
This allows randomised import of data for import testing.  
However, it is generalised as well ( to a certain extent ). 

### methodology
This code doesn't use csv parsers. It reads the csv file as a text, and splits by comma delimiter.  

### technologies used
python 2.5.1

### how to use
Give permission to run executable .py
chmod 744 csvTextModifier.py  
./csvTextModifier.py sample.csv sampleout.csv "Last name" A.* 5 100 5 Test1 Test3  
argv[1] as file to import  
argv[2] as file to write  
argv[3] as item to match, i.e. mds  
argv[4] as regex field, i.e. */USD  
argv[5] as min  
argv[6] as max  
argv[7] as decimal place  
argv[8] onwards as fields  

### limitations
Cannot use later versions of python ==> cannot pip install packages/cannot venv  
(only can use pre-installed packages) 

### problems faced
1. no problems, just full of argv.

### further development
1. overgeneralise the import-export and exception handling in case wrong input is given
