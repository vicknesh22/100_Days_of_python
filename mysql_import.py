import time
import socket
import sys
import os
import subprocess
import logging
import mysql.connector
import json
import urllib
from socket import AF_INET, SOCK_STREAM
from threading import Lock as Lock
from multiprocessing.dummy import Pool as ThreadPool
from os import listdir, path
from os.path import isfile, join
from google.cloud import storage
from elasticsearch import Elasticsearch

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.getcwd() + '/gcp_storage.json'
storage_client = storage.Client()
## add this if we want to accept domain from outise the script
DOMAIN = "blackbox"
STACK = sys.argv[2]


class DataImport:

    def check_complete_dir(self):
        if path.exists('/mnt/volumeshare/data_volumes/' + STACK + '/complete'):
            print("data import is already completed, stopping data import script from further execution")
            sys.exit()
        else:
            print("complete dir not present, starting data import now")

    def mysql_connection_check(self):
        domain = DOMAIN + 'mysql'
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        location = (domain, 3306)
        c = 0
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        while (c != 1):
            try:
                s.connect_ex(location)
                print("Connection successful to " + domain)
                c = 1
                time.sleep(5)
            except socket.error as error:
                # error_code = os.strerror(error.errno)
                print("Failed to connect to " + domain)
                print(error)
                time.sleep(10)
                c = 0
        s.close()

    def schema_import_new(self):
        mysql_domain = DOMAIN + 'mysql'
        current_schema_directory = os.getcwd() + "/nobroker/modules/nobroker-build-plugin/build/mysql/schema/current/";
        current_schema_files = ['nobroker_schema_upgrade.sql'];
        command = "MYSQL_PWD=admin mysql -uroot" + " -f " + " -v " + " -t " + " -h" + mysql_domain
        for current_schema_file in current_schema_files:
            cmd = command + ' <' + current_schema_directory + current_schema_file;
            exe_cmd(cmd);

    def create_dir(self, directory):
        if not os.path.exists(directory):
            os.makedirs(directory);

    def data_import_new(self):
        current_data_directory = os.getcwd() + "/nobroker/modules/nobroker-build-plugin/build/mysql/data/current/";
        current_data_files = ['nobroker_users_data.sql', 'nobroker_data_upgrade.sql'];
        mysql_domain = DOMAIN + 'mysql'
        command = "MYSQL_PWD=admin mysql -uroot" + " -f " + " -v " + " -t " + " -h" + mysql_domain
        for current_data_file in current_data_files:
            cmd = command + ' nobroker <' + current_data_directory + current_data_file;
            exe_cmd(cmd);


def exe_cmd(cmd, ignoreErr="false"):
    ## run it ##
    logging.debug("Command to execute : " + cmd);
    p = subprocess.Popen(cmd, shell=True, stderr=subprocess.PIPE)
    ## But do not wait till netstat finish, start displaying output immediately ##
    while True:
        # print '[CMD_OUTPUT_BEGIN] : ' + '' + cmd + ''
        out = p.stderr.read(1)
        if out == '' and p.poll() != None:
            logging.debug("[CMD_OUTPUT_END] : " + str(p.returncode) + ignoreErr);
            if (ignoreErr == 'false' and p.returncode != 0):
                logging.debug("##################################################")
                logging.debug("[CMD_ERR] : " + cmd);
                logging.debug("##################################################")
                sys.exit("[Failed Command Execution] : " + cmd);
            break
        if out != '':
            sys.stdout.write(out)
            sys.stdout.flush()


# def setup_docker():
#     docker = Docker();
# docker.setup_es5(); (no need since added plugins in image )
def opener():
    host = 'localhost'
    # port = int(input('some port to be opened: '))
    port = 6000
    socket1 = socket.socket(AF_INET, SOCK_STREAM)
    socket1.bind((host, port))
    socket1.listen(1)
    socket1.accept()
    print
    'Port open for connections'
    time.sleep(120)
    socket1.close()
    print
    'Port closed for connection'


def devops_status():
    mysql_domain = DOMAIN + 'mysql'
    command = "MYSQL_PWD=admin mysql -uroot" + " -h" + mysql_domain
    exe_cmd(command + " -e 'select current_time'", "true");
    exe_cmd(
        command + " -Dnobroker" + " -e " + "'UPDATE devops_status SET completed = \"completed\" WHERE status = status;'")
    time.sleep(60)


def data_import():
    data_import = DataImport();
    data_import.check_complete_dir();
    data_import.mysql_connection_check();
    data_import.schema_import_new();
    data_import.data_import_new();


# setup_docker();
logging.basicConfig(level=logging.DEBUG)
data_import();
# add dummy port to listen
# opener();
devops_status();