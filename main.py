import csv
import requests
import sys
import MySQLdb
from ftplib import FTP

def getRPKI():
    url = 'https://ftp.ripe.net/rpki/afrinic.tal/2022/01/02/roas.csv'
    r = requests.get(url)
    f = open('myfile.txt', 'w')
    f.write(r.text)
    f.close

# def upload(f, remote_path, local_path):
#     fp = open(local_path, "rb")
#     buf_size = 1024
#     f.storbinary("STOR {}".format(remote_path), fp, buf_size)
#     fp.close()


def download(f, remote_path, local_path):
    fp = open(local_path, "wb")
    buf_size = 1024
    f.retrbinary('RETR {}'.format(remote_path), fp.write, buf_size)
    fp.close()


if __name__ == "__main__":
    # getRPKI()
    # db = MySQLdb.connect("localhost", "root", "952730", "rpki", charset='utf8')
    # cursor = db.cursor()
    # f = open('myfile.txt', 'r')
    # for line in f.readlines()[1:]:
    #     # print(line)
    #     data = line.split(',')
    #     print(data)
    #     sql = "insert into ASNtoIP(URI, ASN, IPpre, MaxLen) values('"+data[0]+"', '"+data[1]+"', '"+data[2]+"', '"+data[3]+"');"
    #     cursor.execute(sql)
    #     cursor.connection.commit()
    # print(len(f.readlines()))
    # lines = str(f.readlines()[2])
    # print(lines.split(','))
    # for i in f.readlines():
    #     print(i)
    # print(f.readlines())
    ftp = FTP()
    ftp.connect('ftp.ripe.net', 21)      # 第一个参数可以是ftp服务器的ip或者域名，第二个参数为ftp服务器的连接端口，默认为21
    ftp.login()
    ftp.cwd("/rpki/afrinic.tal/2022/01/02/")                # 切换到tmp目录
    download(ftp, "roas.csv", "roas.csv")  # 将ftp服务器tmp目录下的ftp_a.txt文件下载到当前目录，命名为b.txt
    ftp.quit()
