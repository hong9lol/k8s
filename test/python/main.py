import http.client
import threading
import time
import sys
import os

sum_of_request = 0
sum_of_response_success = 0
sum_of_response_fail = 0
test_run_flag = True


def request_thread():
    global sum_of_request
    global sum_of_response_success
    global sum_of_response_fail

    conn = http.client.HTTPConnection('127.0.0.1', 7080, timeout=1)
    sum_of_request = sum_of_request + 1
    try:
        conn.request("GET", "/")
        conn.getresponse()
        sum_of_response_success = sum_of_response_success + 1
    except Exception as e:
        #print(e)
        sum_of_response_fail = sum_of_response_fail + 1


def run_request_test(interval):
    global sum_of_request
    global sum_of_response_success
    global sum_of_response_fail
    global test_run_flag

    test_run_flag = True
    sum_of_request = 0
    sum_of_response_success = 0
    sum_of_response_fail = 0

    _interval = float(interval / 1000)
    while test_run_flag:
        threading.Thread(target=request_thread).start()
        time.sleep(_interval)


def cal():
    print(" - total requests:" + str(sum_of_request))
    print(" - requests(handled):" + str(sum_of_response_success + sum_of_response_fail))
    print(" - requests(not handled):" + str(sum_of_request - sum_of_response_success + sum_of_response_fail))
    print(" - total responses(Code 200): " + str(sum_of_response_success))
    print(" - total responses(Code Error): " + str(sum_of_response_fail))
    global test_run_flag
    test_run_flag = False
    sys.exit(0)


def start_timer():
    timer = threading.Timer(10, cal)
    timer.start()


def runtime_resource_change():
    os.system(_1980m)
    os.system(check_resource)

if __name__ == '__main__':
    interval_ms = 1

    pod_name ='nginx-deployment-54cfc5777d-kgkhl'
    _500m = """kubectl patch pod """ + pod_name + """ --patch '{"spec":{"containers":[{"name":"my-nginx-container", "resources":{"requests":{"cpu":"400m"}, "limits":{"cpu":"500m"}}}]}}'"""
    _1980m = """kubectl patch pod """ + pod_name + """ --patch '{"spec":{"containers":[{"name":"my-nginx-container", "resources":{"requests":{"cpu":"1880m"}, "limits":{"cpu":"1980m"}}}]}}'"""
    _1990m = """kubectl patch pod """ + pod_name + """ --patch '{"spec":{"containers":[{"name":"my-nginx-container", "resources":{"requests":{"cpu":"1890m"}, "limits":{"cpu":"1990m"}}}]}}'"""
    check_resource = """kubectl get pod """ + pod_name + """ -ojson | jq '.spec.containers[0].resources'"""

    os.system(_500m)
    os.system(check_resource)
    print("TEST with CPU: 500m")
    start_timer()
    run_request_test(interval_ms)

    time.sleep(100)
    print("==========================================================")
    print("")

    os.system(_1990m)
    os.system(check_resource)
    print("TEST with CPU: 1990m")
    start_timer()
    run_request_test(interval_ms)

    time.sleep(100)
    print("==========================================================")
    print("")

    os.system(_1990m)
    os.system(check_resource)
    print("TEST with CPU: 1990m, 1980")
    start_timer()
    threading.Timer(5, runtime_resource_change).start()
    run_request_test(interval_ms)


