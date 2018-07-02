while [[ 1 ]]; do
	data=`adb shell dumpsys meminfo | grep 'rhero2.aligam' | head -n 1`
	data=${data%:*}
	data=${data%K*}
	data=`echo $data | sed 's/,//g'`
	let data=($data / 1024)
	echo "$data M"
	sleep 0.01
done