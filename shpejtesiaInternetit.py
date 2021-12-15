import speedtest

st = speedtest.Speedtest()

option = int(input('''Qka deshironi te testoni:
1) Shpejtesine e shkarkimit

2) Shpejtesine e uploadimit

3) Pingun

4) Te gjitha
Zgjedhja: 
'''))

if option == 1:
    print(st.download())
elif option == 2:
    print(st.upload())
elif option == 3:
    servernames = []
    st.get_servers(servernames)
    print(st.results.ping)
elif option == 4:
    print(st.download())
    print(st.upload())
    servernames = []
    st.get_servers(servernames)
    print(st.results.ping)
else:
    print("--------Zgjedhni nje opsion te shenuar me larte--------")