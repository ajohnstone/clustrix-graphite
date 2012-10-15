Clustrix Monitoring
================================

Add monitoring for clustrix in graphite and collectd

Usage
================================

```
DEBUG=1 ./bin/clustrix-graphite
```

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
