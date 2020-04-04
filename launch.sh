gnome-terminal --title="MASTER" -x bash -c "sleep 4s; conda activate corona; cd Documents/corona; python main.py 1"
gnome-terminal --title="CLONE3" -x bash -c "sleep 2s; conda activate corona; cd Documents/corona; python main.py 0"
gnome-terminal --title="CLONE1" -x bash -c "sleep 6s; conda activate corona; cd Documents/corona; python main.py 2"
gnome-terminal --title="CLONE2" -x bash -c "sleep 8s; conda activate corona; cd Documents/corona; python main.py 3"