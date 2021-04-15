from telnetlib import Telnet


def bofh(host="bofh.jeffballard.us", port=666, timeout=180, secondCall=False):
    try:
        tn = Telnet(host, port, timeout)
        tn.open(host, port, timeout)
        header = tn.read_all()
        new_header = header[161:]
        print(new_header)
        tn.close()
        print("[!] Port %d seems to be open on %s" % (port, host))

    except Exception as e:
        try:
            code, reason = e.args
            print("[ERROR] %s on %s:%d (%d)" % (reason, host, port, code))
        except IndexError:
            if e.args[0] == "timed out" and port in port:
                if secondCall is False:
                    print("[!] extending timeout on common port (%d)" % port)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    bofh()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
