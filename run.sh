python run_server.py > log.txt  2>&1 &

while (true); do
	if fuser 5000/tcp 
	then
		continue
	else
		echo "restart"
		python run_server.py > log.txt  2>&1 &
	fi
done
