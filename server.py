from flask import Flask, jsonify, request
import redis

app = Flask(__name__)
r = redis.StrictRedis(host='localhost', port=6379, db=0)


@app.route('/proxies/', methods=['GET'])
def get_proxies():
    return jsonify(r.hgetall('proxies'))


@app.route('/proxies/', methods=['POST'])
def upload_proxy():
    proxy_ip = request.headers['X-Real-IP']
    system_identifier = request.form.get('system_identifier', None)
    if not system_identifier:
        return 'error: {}'.format(proxy_ip)
    r.hset('proxies', system_identifier, proxy_ip)
    return 'ok: {}'.format(proxy_ip)


if __name__ == '__main__':
    app.run()
