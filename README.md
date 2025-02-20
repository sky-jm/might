# Just a random mite minimal example

## How to run the example
### Step 1: Create recorder_data:
```bash
mite scenario test create_user:create_user_scenario --config=configurations:basic_config
```


### Step 2: Use earlier recorded data as datapool
```
$ mite scenario test signin:signin_scenario --config=create_user:justtestsecrets --report

# [...]


==================== MITE Benchmark Report ====================

+---------+--------+--------+--------+---------+-------------+----------+----------+----------+----------+
|         |  Avg   |  Min   |  Max   | Std Dev | +/- Std Dev | 50 %tile | 90 %tile | 98 %tile | 99 %tile |
+---------+--------+--------+--------+---------+-------------+----------+----------+----------+----------+
| Latency | 0.13ms | 0.08ms | 5.40ms |  0.08ms |    95.26%   |  0.12ms  |  0.16ms  |  0.29ms  |  0.39ms  |
+---------+--------+--------+--------+---------+-------------+----------+----------+----------+----------+

+---------+--------+-------+-------+---------+-------------+
|         |  Avg   |  Min  |  Max  | Std Dev | +/- Std Dev |
+---------+--------+-------+-------+---------+-------------+
| Req/Sec | 951.60 | 19.47 | 4.81K |  1.85K  |    80.00%   |
+---------+--------+-------+-------+---------+-------------+

=========================== Summary ===========================
40222 requests in 32.96s, 1.46 MB data transferred

```
