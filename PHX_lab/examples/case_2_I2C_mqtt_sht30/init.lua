-- version 0.1
set_sntp_server(0, "nz.pool.ntp.org")
set_time_zone("NZDT-12")

init_i2c_master(41, 42)
HW_SHT30 = add_i2c_device(100, 0x44)     -- 100kHz

mqtt_open('mqtt://broker.emqx.io:1883')  -- free broker
