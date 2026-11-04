-- version 0.1
set_sntp_server(0, "nz.pool.ntp.org")
set_time_zone("NZDT-12")

pwm_init(0, 32, 100, 0)     -- pwm num, pin num, 100Hz, init value
pwm_fade_enable()
