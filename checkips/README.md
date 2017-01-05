### Watch IPs

Script to monitor a list of IP addresses.
Generally used to monitor a few IPs rather than a subnet.
Utilises `watch` command on *nix and mac.

#### Usage

 * Add an IP to each line of `iplist.txt`
```
echo 10.10.10.2 >> iplist.txt
```
or add them in your favourate editior (joe, vim, nano) etc

 * To run once only
```
sh check-ips.sh
```
 * To monitor constantly **(defaults to 1 second)**
```
sh watch-ips.sh
```
 * To monitor every X seconds
```
sh watch-ips.sh 5
```
```
sh watch-ips.sh 10
```

#### Notes

 * If watch does not work on mac it may need to be installed

**Mac**
```
brew install watch 
```
