Clustrix Monitoring
================================

Add monitoring for clustrix in graphite and collectd

Usage
================================

```
DEBUG=1 ./bin/clustrix-graphite
```

Config
===============================

Change the following and create the config at /etc/clustrix/monitoring.conf.
Alternatively run the following.

```
cat > /etc/clustrix/monitoring.conf <<-EOF
statsd_hostname = metrics.example.com
dsn = "dbi:mysql:test:10.10.10.10:3306"
user = "stats"
pass = ""

;<monitor key_name>
;	SELECT X AS name, v AS value
;</monitor>
EOF
```

Will add custom queries that can be pushed to graphite or collectd

Examples
================================
```
global disk storage utilization

SELECT nodeid<
, devid
, wal_used_bytes + perm_used_bytes + temp_used_bytes AS used
, total_bytes
, 100 * (wal_used_bytes + perm_used_bytes + temp_used_bytes) / total_bytes AS percent
FROM system.device_space_stats
ORDER BY nodeid, devid;

SELECT * FROM stats WHERE name LIKE "tps_%" ORDER BY name, nodeid;
SELECT * FROM stats WHERE name LIKE "qps_%" ORDER BY name, nodeid;

SELECT name, value
FROM system.cluster_session_stats
GROUP BY name;
```

Screen shots
================================
![Clustrix Graphite Dashboard](https://raw.github.com/ajohnstone/clustrix-graphite/master/docs/img/graphite.dashboard.png)
![Clustrix Graphite Metrics](https://raw.github.com/ajohnstone/clustrix-graphite/master/docs/img/graphite.metrics.png)
