# 业务处理: 使用python sdk调用支付宝的支付接口
# 初始化

from alipay import AliPay

a = '-----BEGIN RSA PRIVATE KEY-----\n' + 'MIIEowIBAAKCAQEAyFkm/SWDTEV+f5Bjsin1y3nXDqTkjMf0XhpDNkagf9RXVcwv83eHNx81A6RdzciNCETbC1uTpDHwlwMjdqK6JrqZRHY6HGuyTg6+p0QEWaMZ5RNkBgJ/9Ot3VsTp2k6F+upC7D0QpJ6wmGbFDgResSXYX4vA1MyQXfASmVVPjiP8zOEEnAmlU5YMafIcM3YelMM5QpVQu39Po43lNzfklk3meyBAaxlAqMpbHEEqu9APKUeRGA7kYa7JxnW/lkjU+sPi78r1ULiTtxj7xQpHSsARCs5RBIt+EHB13kvOGqsd9vrYMfq4PP1UhkuMF734QV8pgvjNSSIWsUER7URCuQIDAQABAoIBAG7oq6TH939pmTWVARvIDsGtmVgKAFvO9YCCmWKaho89RXvBpWnqaXgiVn7FpwgcVbaWJ4yKDZl/6+gtXJx4SQTXl7FGobTKCdMcZn7CMIZOvC8MJPsOtzcmgtIOAEdR4OmedZ3B0EzRbIFxovS3hpQal0WNYBpthB38oM8xYvEUDnAJ+OISSg5UcMy1aUbLpFGlN42Q1M54FeLu6hJ9hgByD/a3/jORFesuMcy6A4QEmcS47ARS1Z3gMIB72qVCsWFK8rO2LU4aw5KpDllt4hnjvkZdyU1R38M/9fJmmYSwKGLU7337mNC386Ckdw/lNeEhQ9HCXVVg4e11IwqiQ2ECgYEA/6cGK+fDu75T7yENbCygqTJVYKIiTFcfsS/OKMc7NG+c38oxyu5+eH+rHQJgdIsMzeX16xLZNaf50uM1A0DPUWH/4rR9WN3YFRMD+rq0rEkKmcfdIsJsr7NiCUdf8B1en4/Wp1Duc91LwN8kaFLTMvA/G46+isKugp8Hl0qcZu8CgYEAyJ7hY192iwZzZrfF/jyKE3aSIo5wZ1qER9Y4VYT9P8Ya+sZThp9TiB3NlLsgx9EUVR+8jy13btG2q1pjQsoeaeJKCoPVws3uFlb+z+lWe9kUhra/nr2qpyaydX3wPhmuZf7XSjRYmIKTAbnWTj7DGiw2iwaHtycB5LF54oEzMNcCgYEA0fsZGZTaculIPYBTawdYysAZ2i4xp6xjzoAqf9nsagxGuJV1wm2TmVuba09ZdEAFu1RnYbZwjB61Fp8iGtLvtbOdnlKLJiPI6L5epWEXJu8zcs3zdypkZQgcvOxQA4PMBZj6QSE7ShV4tClT2RA2gn9MBlF/da+j8Iu4i25v+icCgYB0L+eyiH/75iGBdJ8bLW599SaPEtUwVjDT9dGsXZfZjl7jq2aGSdGzvCbqozFJ5+GRpw6qERfhO11CgdeIv8u7YM2mp1FuP5tKntl2CdoHYeJMXpw9T/T8VyH1f5laLb9d3KhMlmJU+RIwZrMhn6GYj9CK1Z5VySaEjvBa6J6AAwKBgDKMWng3Oy4jCcEsBB7bQA9LgVaZNCdC2ns64BGmp1MH60Mmotpuu58Tg27t34oDXKY7KzViEUEfhjnTRo1L4ftzf5U7vCqIfyzOoMdaZ+5Ltjkh9OKAkB0vAZtljCOYDeMOQh1i0pVizKpBsdnKwot+lGGrTwp6ApJYxILfn1ff' + '\n-----END RSA PRIVATE KEY-----'
b = '-----BEGIN PUBLIC KEY-----\n'+'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAtb3Po9lM1geIMSYYbCQNT1ZSkojGN/pnAgqhgUhT8EAxza2Xd3lW4Xc9S4evxsiZMETKYXSmyKOAYewQsm3FdmwH5jV1gYGAqJFtXXkbyDnh545w7g9oV+U4FEb2GFupttWn7KKzUir8ydlt4MzstWEoBg4XGv3Av0LClu0xp62qbv+4kbi5lApYGN3F91lqWGngmIYvyJ0eyl/gT7nnB+mru6jk52EFt4YQyPoypHkR1MLi4FdS4ZJ/pizIBvCVhMit8GUBFPXxY149De3AWwrQvFI91BeD17/TjwjiVBz0kLieJ+FjNzgoHg2VvBLlfVIdA/fjnQooBTNVAfS8bwIDAQAB' + '\n-----END PUBLIC KEY-----'

alipay = AliPay(
    appid="2021000117633511",
    app_notify_url=None,
    app_private_key_string=a,
    alipay_public_key_string=b,
    sign_type="RSA2",
    debug=True)

# 调用接口
# total_pay = order.total_price + order.transit_price


order_string = alipay.api_alipay_trade_page_pay(
    out_trade_no=str(123123),
    total_amount=str(10000),
    subject='text',
    return_url="https://baidu.com",
    notify_url="https://baidu.com")

# 返回应答
pay_url = "https://openapi.alipaydev.com/gateway.do?" + order_string
print(pay_url)

