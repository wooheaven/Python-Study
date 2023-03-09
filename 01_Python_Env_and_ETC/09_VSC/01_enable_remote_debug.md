```
1) 설치 : Remote Development
VSC
> Extensions
> Search Extensions in Marketplace
> Remote Development

2) 설정 : config
VSC
> Show All Command
> Remote-SSH : Connect to Host...
> SSH 호스트 구성...
> ~/.ssh/config
Host prefix_user00               # Alias for Client VSC > Remote-SSH
    HostName prefix.company.tail # Hostname or IP for Remote Server
    Port 22                      # SSH Port for Remote Server
    User prefix_user00           # SSH User for Remote Server

3) 연결 : SSH
VSC
> Show All Command
> Remote-SSH : Connect to Host...
> prefix_user00
> VSC in new window
> Enter password

4) 설치 : Python extension for Visual Studio Code
VSC for Remote-SSH
> Extensions
> Python extension for Visual Studio Code

5) 원격 디버깅
VSC for Remote-SSH
> Explorer
> code
> Breakpoint
> Start Debugging
```
