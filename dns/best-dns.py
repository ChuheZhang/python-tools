import dns.resolver
import timeit

# 定义DNS服务器列表
dns_servers = [
    ("Google DNS", "8.8.8.8"),
    ("Google DNS 2", "8.8.4.4"),
    ("Cloudflare DNS", "1.1.1.1"),
    ("OpenDNS", "208.67.222.222"),
    ("Quad9 DNS", "9.9.9.9"),
    ("AliDNS", "223.5.5.5"),
    ("AliDNS 2", "223.6.6.6"),
    ("Tencent DNS", "119.29.29.29"),
    ("114DNS", "114.114.114.114"),
    ("114DNS 2", "114.114.115.115"),
    ("Baidu DNS", "180.76.76.76"),
    ("DNSPod", "119.28.28.28"),
    ("Hurricane Electric", "74.82.42.42"),
    ("Comodo Secure DNS", "8.26.56.26"),
    ("Comodo Secure DNS 2", "8.20.247.20"),
]

# 使用dns.resolver测试响应时间
def test_dns(dns_ip):
    resolver = dns.resolver.Resolver()
    resolver.nameservers = [dns_ip]  # 设置DNS服务器
    domain = "example.com"  # 使用测试域名
    try:
        start_time = timeit.default_timer()
        resolver.query(domain, "A")  # 发送查询请求
        end_time = timeit.default_timer()
        return (end_time - start_time) * 1000  # 返回响应时间（毫秒）
    except Exception:
        return float('inf')  # 失败则返回无穷大

# 主函数，测试所有DNS的响应时间并找出最快的
def find_best_dns():
    results = []
    for name, ip in dns_servers:
        response_time = test_dns(ip)
        results.append((name, ip, response_time))
        print(f"{name} 的响应时间：{response_time:.2f} ms")

    # 按照响应时间排序，取出最小的
    best_dns = min(results, key=lambda x: x[2])
    print(f"\n最快的DNS服务器是：{best_dns[0]} ({best_dns[1]}), 响应时间为：{best_dns[2]:.2f} ms")

if __name__ == "__main__":
    find_best_dns()
