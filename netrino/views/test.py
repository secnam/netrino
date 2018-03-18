
from luxon import g
from luxon import register_resource
from luxon import register_resources

@register_resource('GET', '/v1/test', 'admin')
def test(req, resp):
    test = {}
    test['test'] = 'this is a test'
    return test


@register_resource('POST', '/v1/test', 'admin')
def test_post(req, resp):
    return req.json

