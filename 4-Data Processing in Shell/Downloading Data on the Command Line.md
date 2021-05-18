In this chapter, we learn how to download data files from web servers via the command line. In the process, we also learn about documentation manuals, option flags, and multi-file processing.

# Downing Data using CURL

``` shell
man curl
```
curl  is  a  tool  to  transfer data from or to a server, using one of the supported protocols (DICT, FILE, FTP, FTPS, GOPHER,
HTTP, HTTPS, IMAP, IMAPS, LDAP, LDAPS, POP3, POP3S, RTMP, RTSP, SCP, SFTP, SMB, SMBS, SMTP, SMTPS, TELNET and TFTP). The  com‐
mand is designed to work without user interaction.

``` shell
# Use curl to download the file from the redirected URL
curl -L https://assets.datacamp.com/production/repositories/4180/datasets/eb1d6a36fa3039e4e00064797e1a1600d267b135/201812SpotifyData.zip

# Download and rename the file in the same step
curl -o Spotify201812.zip -L https://assets.datacamp.com/production/repositories/4180/datasets/eb1d6a36fa3039e4e00064797e1a1600d267b135/201812SpotifyData.zip

# Download all 100 data files
curl -O https://s3.amazonaws.com/assets.datacamp.com/production/repositories/4180/datasets/files/datafile\[001\-100\].txt

# Print all downloaded files to directory
ls datafile\*.txt
```


# Downing data using Wget
``` shell
man wget
```
what is wget:
- derives its name from World Wide Web and get
- native to Linux but compatible for all operating systems
- used to download data from HTTP(S) and FTP
- better than curl at downloading multiple ?les recursively

``` shell
# Fill in the two option flags 
wget -bc https://assets.datacamp.com/production/repositories/4180/datasets/eb1d6a36fa3039e4e00064797e1a1600d267b135/201812SpotifyData.zip

# Verify that the Spotify file has been downloaded
ls

# Preview the log file 
cat wget-log

# View url\_list.txt to verify content
cat url_list.txt

# Create a mandatory 1 second pause between downloading all files in url\_list.txt
wget \--wait\=1 \-i url\_list.txt

# Take a look at all files downloaded
ls
```

