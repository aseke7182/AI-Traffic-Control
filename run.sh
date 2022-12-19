fname=out.txt

# Clear "out.txt" file
if test -e $fname
then
	rm $fname
fi

# Run python script for each video and write car count in "out.txt" file
python multithreading.py "/videos/Abylaikhan sever-ug.MOV" >> out.txt
python multithreading.py "/videos/Abylaikhan ug-sever.MOV" >> out.txt
python multithreading.py "/videos/Tole bi vostok-zapad.MOV" >> out.txt
python multithreading.py "/videos/Tole bi zapad-vostok.MOV" >> out.txt

# Calculate the time of traffic lights with the received data
python program.py
