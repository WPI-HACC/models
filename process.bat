python -m unittest discover -s "test" -p "*_test.py"

REM process datasets and generate dictionary (note: only need to do this once.)

python utils\process_imdb.py
python utils\process_dataset.py
python utils\generate_dictionary.py

REM convert imdb results

python utils\convert.py --input data\imdb\aggregated\train.input.txt     --map data\dictionary\words.dictionary.txt data\dictionary\label.dictionary.txt --output data\imdb\ctf\train.ctf
python utils\convert.py --input data\imdb\aggregated\val.input.txt       --map data\dictionary\words.dictionary.txt data\dictionary\label.dictionary.txt --output data\imdb\ctf\test.ctf
python utils\convert.py --input data\imdb\aggregated\test.input.txt      --map data\dictionary\words.dictionary.txt data\dictionary\label.dictionary.txt --output data\imdb\ctf\val.ctf

REM convert mturk results into ctf

REM python utils\convert.py --input data\all\aggregated\imdb.train.input.txt --map data\dictionary\words.dictionary.txt data\dictionary\label.dictionary.txt --output data\all\ctf\train.ctf
REM python utils\convert.py --input data\all\aggregated\imdb.val.input.txt   --map data\dictionary\words.dictionary.txt data\dictionary\label.dictionary.txt --output data\all\ctf\test.ctf
REM python utils\convert.py --input data\all\aggregated\imdb.test.input.txt  --map data\dictionary\words.dictionary.txt data\dictionary\label.dictionary.txt --output data\all\ctf\val.ctf
