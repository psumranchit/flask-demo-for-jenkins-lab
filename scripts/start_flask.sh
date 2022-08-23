MYINID=$(curl -s http://169.254.169.254/latest/meta-data/instance-id)
sudo sed -i "s/REPLACE_ME/$MYINID/g" /web-demo/templates/home.html

nohup python /web-demo/main.py > /dev/null 2>&1 &
